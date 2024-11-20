
### **Task1 : Sunday Sales Analysis for Silver Products**

#### **Objective**:
Analyze sales data from the `FactInternetSales` table and its related dimensions. Specifically, focus on high-income customers purchasing silver-colored products on Sundays.

#### **Requirements**:

1. **Filter Criteria**:
   - Consider sales that occurred on **Sundays**.
   - Include only products where:
     - `Color` is **Silver**.
     - Has **Size** information.
     - `Weight` is greater than **10**.
   - Include customers who:
     - Have a `YearlyIncome` greater than **100,000.0**.
     - Have more than **1 child**.

2. **Aggregations**:
   - Group by `CustomerKey` and `FirstName`.
   - Calculate the following metrics:
     - Total `TaxAmt` paid by each customer.
     - Average `SalesAmount`.
     - Average `TotalProductCost`.

3. **Sorting**:
   - Sort the result by `FirstName` in ascending order.

4. **Data Presentation**:
   - Drop the `CustomerKey` column from the final output.

---