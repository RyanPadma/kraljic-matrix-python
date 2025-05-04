# Kraljic Matrix Automation in Python

This project automates Kraljic Matrix analysis using Python and pandas, integrating supplier, price, shipment, and product quality data. It calculates composite risk and revenue metrics, classifies suppliers and products into Kraljic Matrix quadrants, and visualizes the results to support strategic sourcing and supply risk management.

---

## Features

- **Data Integration:** Combines price, supplier, shipment, and product quality datasets.
- **Automated Preprocessing:** Cleans, standardizes, and encodes data for analysis.
- **Composite Risk Calculation:** Aggregates risk, lead time, and defect rate into a single metric.
- **Kraljic Matrix Classification:** Assigns suppliers and products to Strategic, Leverage, Bottleneck, or Non-Critical quadrants.
- **Visualization:** Generates clear, color-coded Kraljic Matrix plots for both suppliers and products.

---

## Requirements

- Python 3.7+
- numpy
- pandas
- scikit-learn
- matplotlib

Install all dependencies with:
pip install -r requirements.txt

---

## Data Files

Place the following CSV files in the project directory:
- `price_data.csv`
- `supplier_data.csv`
- `shipment_data.csv`
- `product_quality_data.csv`

> **Note:** Use anonymized or synthetic data if your real data is confidential. Each file should have columns matching those referenced in the code.

---

## How to Run

1. Ensure all required CSV files are present in the directory.
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the script:
    ```
    Kraljic_Matrix_Project.py
    ```
4. The script will output tables of supplier and product Kraljic categories and display two scatter plots:
    - Supplier Kraljic Matrix
    - Product Kraljic Matrix

---

## Example Output

**Console Output:**
Supplier Kraljic Matrix Category Table (Rule-Based):
supplier_id kraljic_category
0 0 Strategic Supplier
1 1 Leverage Supplier
...

Product Kraljic Matrix Category Table (Rule-Based):
product_id kraljic_category
0 0 Strategic Item
1 1 Leverage Item
...


**Visualizations:**
- Supplier Kraljic Matrix 
  ![Supplier Kraljic Matrix](https://github.com/user-attachments/assets/44dd042c-e571-4221-a63d-c279924bde7b)
- Product Kraljic matrix
  ![Product Kraljic Matrix](https://github.com/user-attachments/assets/16702730-18fa-4271-968c-4d0c7ab69584)
---

## Kraljic Matrix Quadrants

- **Strategic:** High risk, high revenue impact
- **Leverage:** Low risk, high revenue impact
- **Bottleneck:** High risk, low revenue impact
- **Non-Critical:** Low risk, low revenue impact


---

## Contact

For questions or collaboration, please open an issue or contact Nurcahyo Padma(mailto:nurcahyo.satria14@gmail.com).

