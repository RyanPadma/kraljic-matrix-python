# 🤖 Kraljic Matrix Automation in Python

This project automates Kraljic Matrix analysis using Python and pandas, integrating supplier, price, shipment, and product quality data. It calculates composite risk and revenue metrics, classifies suppliers and products into Kraljic Matrix quadrants, and visualizes the results to support strategic sourcing and supply risk management.

---

## ✨ Features

- 🔗 **Data Integration:** Combines price, supplier, shipment, and product quality datasets.
- 🧹 **Automated Preprocessing:** Cleans, standardizes, and encodes data for analysis.
- ⚖️ **Composite Risk Calculation:** Aggregates risk, lead time, and defect rate into a single metric.
- 🗂️ **Kraljic Matrix Classification:** Assigns suppliers and products to Strategic, Leverage, Bottleneck, or Non-Critical quadrants.
- 📊 **Visualization:** Generates clear, color-coded Kraljic Matrix plots for both suppliers and products.

---

## ⚙️ Requirements

- 🐍 Python 3.7+
- 📦 numpy
- 📦 pandas
- 📦 scikit-learn
- 📦 matplotlib


Install all dependencies with:
pip install -r requirements.txt

---

## 🗃️ Data Files

Place the following CSV files in the project directory:
- `price_data.csv`
- `supplier_data.csv`
- `shipment_data.csv`
- `product_quality_data.csv`

> **Note:** Use anonymized or synthetic data if your real data is confidential. Each file should have columns matching those referenced in the code.

---


## 🚀 How to Run

1. ✅ Ensure all required CSV files are present in the directory.
2. 📥 Install dependencies:
    ```
        pip install -r requirements.txt
    ```
3. Run the script:
    ```
    Kraljic_Matrix_Project.py
    ```
4.  📊 The script will output tables of supplier and product Kraljic categories and display two scatter plots:
    - Supplier Kraljic Matrix
    - Product Kraljic Matrix

---

## 📋 Example Output

**Console Output:**
###  📊  Example: Supplier Kraljic Matrix Category Table

| supplier_id | kraljic_category        |
|-------------|------------------------|
| 0           | Strategic Supplier     |
| 1           | Leverage Supplier      |
| 2           | Bottleneck Supplier    |
| 3           | Non-Critical Supplier  |

### Example: Product Kraljic Matrix Category Table

| product_id | kraljic_category     |
|------------|---------------------|
| 0          | Strategic Item      |
| 1          | Leverage Item       |
| 2          | Bottleneck Item     |
| 3          | Non-Critical Item   |





**Visualizations:**
-  📈 Supplier Kraljic Matrix 
  ![Supplier Kraljic Matrix](https://github.com/user-attachments/assets/44dd042c-e571-4221-a63d-c279924bde7b)
-  📈 Product Kraljic matrix
  ![Product Kraljic Matrix](https://github.com/user-attachments/assets/16702730-18fa-4271-968c-4d0c7ab69584)
---

##  🧭 Kraljic Matrix Quadrants

# 🧭 Kraljic Matrix – Supplier vs Product Strategy Comparison

| **Quadrant** | **Supplier Perspective** | **Product Perspective** |
|--------------|-------------------------|-------------------------|
| **🟧 Strategic (High Risk, High Impact)** | - Build **long-term partnerships & alliances**.<br>- Engage in **joint development & innovation**.<br>- **Monitor supplier health** & mitigate dependence risk.<br>- Consider **dual sourcing or vertical integration**. | - Secure **long-term contracts & guaranteed supply**.<br>- **Collaborate in design & innovation** with suppliers.<br>- Maintain **inventory buffers** for risk mitigation.<br>- **Redesign products** to reduce dependence where possible. |
| **🟩 Leverage (Low Risk, High Impact)** | - Use **competitive bidding, tenders, and auctions**.<br>- **Consolidate volumes** to maximize bargaining power.<br>- Maintain **flexible contracts** to switch suppliers easily.<br>- **Benchmark & renegotiate prices** regularly. | - Focus on **cost optimization & negotiation**.<br>- **Aggregate demand** to get bulk discounts.<br>- Use **multiple sourcing** to maintain flexibility.<br>- Drive **product standardization** to expand sourcing options. |
| **🟥 Bottleneck (High Risk, Low Impact)** | - Maintain **good relationships**; be a "preferred customer".<br>- Hold **safety stock or buffer inventory**.<br>- Search for **alternative suppliers or substitute technologies**.<br>- **Support supplier capability improvement** if critical. | - Keep **inventory buffers or consignment stock**.<br>- Seek **design changes or product substitutions** to reduce dependency.<br>- Use **supplier-managed inventory (SMI)** for reliability. |
| **🟦 Non-Critical (Low Risk, Low Impact)** | - **Automate procurement** via e-catalogs or e-procurement.<br>- **Long-term contracts with few suppliers** to simplify management.<br>- Consider **outsourcing procurement** or VMI. | - Simplify purchasing with **blanket POs or catalog buying**.<br>- **Standardize products** to reduce complexity.<br>- Focus on **process efficiency & TCO** rather than price only. |



---

## Contact

For questions or collaboration, please open an issue or contact Nurcahyo Padma(mailto : nurcahyo.satria14@gmail.com).

