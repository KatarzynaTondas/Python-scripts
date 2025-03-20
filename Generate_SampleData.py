import pandas as pd
import numpy as np
import os

# Define the folder where files will be saved
SAVE_PATH = "your_path"
os.makedirs(SAVE_PATH, exist_ok=True)  # Create the folder if it does not exist

# 1. Generate product data
categories = {
    "Electronics": ["Laptops", "Smartphones", "Tablets"],
    "Clothing": ["T-Shirts", "Pants", "Jackets"],
    "Food": ["Fruits", "Drinks", "Sweets"],
    "Appliances": ["Washing Machines", "Refrigerators", "Mixers"]
}

product_list = []
product_id = 1

for category, subcategories in categories.items():
    for subcategory in subcategories:
        for i in range(1, 9):  # 8 products per subcategory = 100 products
            price = np.random.randint(20, 2000)
            cost = price * np.random.uniform(0.5, 0.9)  # Cost is 50-90% of the price
            product_list.append({
                "ProductID": product_id,
                "Name": f"{subcategory} Model {i}",
                "Category": category,
                "Subcategory": subcategory,
                "Price": price,
                "Cost": round(cost, 2)
            })
            product_id += 1

products = pd.DataFrame(product_list)

# 2. Generate store data
stores = pd.DataFrame({
    "StoreID": range(1, 6),
    "Name": [f"Store {i}" for i in range(1, 6)],
    "City": np.random.choice(["Warsaw", "Krakow", "Gdansk", "Wroclaw", "Poznan"], 5)
})

# 3. Generate customer data
customers = pd.DataFrame({
    "CustomerID": range(1, 51),
    "Name": [f"Customer {i}" for i in range(1, 51)],
    "Age": np.random.randint(18, 70, 50),
    "City": np.random.choice(["Warsaw", "Krakow", "Gdansk", "Wroclaw", "Poznan"], 50)
})

# 4. Generate sales data (3 years, 5000 transactions)
sales = pd.DataFrame({
    "TransactionID": range(1, 5001),
    "Date": pd.date_range(start="2021-01-01", periods=5000, freq="D"),
    "ProductID": np.random.choice(products["ProductID"], 5000),
    "StoreID": np.random.choice(stores["StoreID"], 5000),
    "CustomerID": np.random.choice(customers["CustomerID"], 5000),
    "Quantity": np.random.randint(1, 5, 5000)
})

# Add sales value and cost based on product data
sales = sales.merge(products[["ProductID", "Price", "Cost"]], on="ProductID", how="left")
sales["Value"] = sales["Quantity"] * sales["Price"]
sales["Total_Cost"] = sales["Quantity"] * sales["Cost"]
sales.drop(columns=["Price", "Cost"], inplace=True)

# 5. Generate budget plan (36 months, 3 years)
months = pd.date_range(start="2021-01-01", periods=36, freq="MS").strftime('%Y-%m')
product_ids = np.repeat(products["ProductID"].values, len(months))

budget = pd.DataFrame({
    "Month": np.tile(months, len(products)),
    "ProductID": product_ids,
    "Planned_Sales": np.random.randint(1000, 10000, len(product_ids))
})

# 6. Save files to the specified folder
products.to_csv(os.path.join(SAVE_PATH, "products.csv"), index=False)
stores.to_csv(os.path.join(SAVE_PATH, "stores.csv"), index=False)
customers.to_csv(os.path.join(SAVE_PATH, "customers.csv"), index=False)
sales.to_csv(os.path.join(SAVE_PATH, "sales.csv"), index=False)
budget.to_csv(os.path.join(SAVE_PATH, "budget.csv"), index=False)

print(f"CSV files have been generated in: {SAVE_PATH}")
