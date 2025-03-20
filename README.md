# Sales Data Generator

## This Python script generates realistic sales-related datasets for Power BI analysis. It creates sample data for:

- Products (including categories, subcategories, prices, and costs)
- Stores (locations and store names)
- Customers (age, city, and IDs)
- Sales transactions (with quantity, value, and cost calculations)
- Planned budget (monthly planned sales for three years)

### How to Use

- Install dependencies: pip install pandas numpy
- Run the script: python generate_sales_data.py

Find the CSV files in the generated_data directory.

### Relationships between the tables:

1. Products (products.csv): Each product has a unique ProductID, along with attributes such as category, subcategory, price, and cost. This table serves as a reference for product details.
2. Stores (stores.csv): Each store has a unique StoreID and is associated with a city. This table represents the locations where sales transactions occur.
3. Customers (customers.csv): Each customer has a unique CustomerID, an associated city, and an age. This table represents the buyers.
4. Sales (sales.csv): This is the fact table that captures transactions. It includes:

- TransactionID: Unique identifier for each sale.
- Date: Date of the transaction.
- ProductID: Links to the products.csv table.
- StoreID: Links to the stores.csv table.
- CustomerID: Links to the customers.csv table.
- Quantity: Number of products purchased.
- Value: Computed as Quantity * Price.
- Total_Cost: Computed as Quantity * Cost.
  
5. Planned Budget (budget.csv): This table contains planned sales data per month for each product. It includes:
- Month: The period (YYYY-MM format).
- ProductID: Links to the products.csv table.
- Planned_Sales: The expected sales value for that month.

### Table Relationships of Data:
- sales.csv is the central fact table, connected to products.csv, stores.csv, and customers.csv through their respective ID fields.
- budget.csv is related to products.csv through ProductID and can be used for variance analysis (planned vs. actual sales).

This setup follows a star schema approach, optimizing f.eg. for Power BI analytics.




Please use *Diagram.py* to generate simple diagram of relationsh of model.

