# -*- coding: utf-8 -*-
"""
Created on Sun May  4 14:13:20 2025

@author: ACER
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# -------------------------
# Load datasets
# -------------------------
price_df = pd.read_csv("price_data.csv")
supplier_df = pd.read_csv("supplier_data.csv")
shipment_df = pd.read_csv("shipment_data.csv")
product_quality_df = pd.read_csv("product_quality_data.csv")

# -------------------------
# Price Data Preprocessing
# -------------------------
price_df = (
    price_df.rename(columns={'price_fluct': 'price_fluctuation'})
    .dropna()
    .assign(
        price_usd=lambda x: np.where(x['currency'] == 'EUR', x['price'] * 1.08, x['price']),
        currency='USD'
    )
    .drop(columns=['price'])
    .rename(columns={'price_usd': 'price'})
)
price_df['product_id'] = price_df['product_id'].astype(str)

# -------------------------
# Supplier Data Preprocessing
# -------------------------
supplier_df = (
    supplier_df.dropna()
    .assign(
        supplier_id=lambda x: x['supplier_id'].astype('category').cat.codes,
        location=lambda x: x['location'].astype('category').cat.codes
    )
)
supplier_scaler = StandardScaler()
supplier_df[['risk_index', 'rating']] = supplier_scaler.fit_transform(
    supplier_df[['risk_index', 'rating']]
)

# -------------------------
# Shipment Data Preprocessing
# -------------------------
shipment_df['product_id'] = shipment_df['product_id'].astype(str)
shipment_df = (
    shipment_df.dropna()
    .merge(price_df[['product_id', 'price']], on='product_id', how='left')
    .assign(
        shipment_id=lambda x: x['shipment_id'].astype('category').cat.codes,
        supplier_id=lambda x: x['supplier_id'].astype('category').cat.codes,
        product_id=lambda x: x['product_id'].astype('category').cat.codes,
        on_time=lambda x: x['on_time'].astype('category').cat.codes,
        shipment_date=lambda x: pd.to_datetime(x['shipment_date']),
        revenue=lambda x: x['number_of_product_shipped'] * x['price']
    )
)
shipment_scaler = StandardScaler()
shipment_df['lead_time'] = shipment_scaler.fit_transform(shipment_df[['lead_time']])

# -------------------------
# Product Quality Preprocessing
# -------------------------
product_quality_df['product_id'] = product_quality_df['product_id'].astype(str)
product_quality_df = (
    product_quality_df.dropna()
    .assign(product_id=lambda x: x['product_id'].astype('category').cat.codes)
)
quality_scaler = StandardScaler()
product_quality_df[['quality_score', 'defect_rate']] = quality_scaler.fit_transform(
    product_quality_df[['quality_score', 'defect_rate']]
)

# -------------------------
# Combine Datasets
# -------------------------
combined_df = (
    shipment_df[['supplier_id', 'product_id', 'revenue', 'lead_time']]
    .merge(supplier_df[['supplier_id', 'risk_index']], on='supplier_id')
    .merge(product_quality_df[['product_id', 'defect_rate']], on='product_id')
)

# -------------------------
# Supplier-level Aggregation & Composite Risk
# -------------------------
supplier_features = combined_df.groupby('supplier_id').agg({
    'revenue': 'mean',
    'risk_index': 'mean',
    'lead_time': 'mean',
    'defect_rate': 'mean'
}).reset_index()

# Standardize all relevant columns
scaler = StandardScaler()
supplier_features[['revenue_std', 'risk_index_std', 'lead_time_std', 'defect_rate_std']] = scaler.fit_transform(
    supplier_features[['revenue', 'risk_index', 'lead_time', 'defect_rate']]
)

# Composite standardized risk: average of the standardized risk components
supplier_features['composite_risk_std'] = supplier_features[['risk_index_std', 'lead_time_std', 'defect_rate_std']].mean(axis=1)

# -------------------------
# Product-level Aggregation & Composite Risk
# -------------------------
product_features = combined_df.groupby('product_id').agg({
    'revenue': 'mean',
    'risk_index': 'mean',
    'lead_time': 'mean',
    'defect_rate': 'mean'
}).reset_index()

product_features[['revenue_std', 'risk_index_std', 'lead_time_std', 'defect_rate_std']] = scaler.fit_transform(
    product_features[['revenue', 'risk_index', 'lead_time', 'defect_rate']]
)

product_features['composite_risk_std'] = product_features[['risk_index_std', 'lead_time_std', 'defect_rate_std']].mean(axis=1)

# -------------------------
# Assign Kraljic Quadrants (Rule-Based)
# -------------------------
# For suppliers
conditions_sup = [
    (supplier_features['composite_risk_std'] >= 0) & (supplier_features['revenue_std'] >= 0),
    (supplier_features['composite_risk_std'] < 0) & (supplier_features['revenue_std'] >= 0),
    (supplier_features['composite_risk_std'] >= 0) & (supplier_features['revenue_std'] < 0),
    (supplier_features['composite_risk_std'] < 0) & (supplier_features['revenue_std'] < 0)
]
choices_sup = ['Strategic Supplier', 'Leverage Supplier', 'Bottleneck Supplier', 'Non-Critical Supplier']
supplier_features['kraljic_category'] = np.select(conditions_sup, choices_sup)

# For products
conditions_prod = [
    (product_features['composite_risk_std'] >= 0) & (product_features['revenue_std'] >= 0),
    (product_features['composite_risk_std'] < 0) & (product_features['revenue_std'] >= 0),
    (product_features['composite_risk_std'] >= 0) & (product_features['revenue_std'] < 0),
    (product_features['composite_risk_std'] < 0) & (product_features['revenue_std'] < 0)
]
choices_prod = ['Strategic Item', 'Leverage Item', 'Bottleneck Item', 'Non-Critical Item']
product_features['kraljic_category'] = np.select(conditions_prod, choices_prod)

# -------------------------
# Show Results
# -------------------------
print("Supplier Kraljic Matrix Category Table (Rule-Based):")
print(supplier_features[['supplier_id', 'kraljic_category']])

print("\nProduct Kraljic Matrix Category Table (Rule-Based):")
print(product_features[['product_id', 'kraljic_category']])

# -------------------------
# Visualization for Supplier Kraljic Matrix
# -------------------------
plt.figure(figsize=(10, 6))
supplier_colors = {
    'Strategic Supplier': 'orange',
    'Leverage Supplier': 'green',
    'Bottleneck Supplier': 'red',
    'Non-Critical Supplier': 'blue'
}
for category, color in supplier_colors.items():
    subset = supplier_features[supplier_features['kraljic_category'] == category]
    plt.scatter(
        subset['composite_risk_std'],
        subset['revenue_std'],
        label=f'{category} (n={len(subset)})',
        color=color,
        alpha=0.7
    )
plt.xlabel('Composite Standardized Risk')
plt.ylabel('Standardized Revenue Impact')
plt.title('Supplier Kraljic Matrix Classification (Composite Risk)')
plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.legend(title='Supplier Category')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# -------------------------
# Visualization for Product Kraljic Matrix
# -------------------------
plt.figure(figsize=(10, 6))
product_colors = {
    'Strategic Item': 'orange',
    'Leverage Item': 'green',
    'Bottleneck Item': 'red',
    'Non-Critical Item': 'blue'
}
for category, color in product_colors.items():
    subset = product_features[product_features['kraljic_category'] == category]
    plt.scatter(
        subset['composite_risk_std'],
        subset['revenue_std'],
        label=f'{category} (n={len(subset)})',
        color=color,
        alpha=0.7
    )
plt.xlabel('Composite Standardized Risk')
plt.ylabel('Standardized Revenue Impact')
plt.title('Product Kraljic Matrix Classification (Composite Risk)')
plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.legend(title='Product Category')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

