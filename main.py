import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv("data of gurugram real Estate.csv")

# first we will clean the dataset

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
# print(df.columns.tolist())

df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
# print(df["price"])
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
# print(df["area"])
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)
# print(df["rate_per_sqft"])
df["rera_approval"] = (
    df["rera_approval"]
    .str.strip()
    .str.lower()
    .map({"approved by rera": True, "not approved by rera": False})
)
# print(df["rera_approval"])

df["flat_type"] = df["flat_type"].str.strip().str.lower()
# print(df["flat_type"])
df = df.dropna().drop_duplicates()

# print(df)
# print(df.info())
# problem 1. Which is the costliest flat in the dataset?

costliest_flat = df.loc[df["price"].idxmax()]
print(costliest_flat)

# problem 2. Which locality has the highest average price?
locality_avg_price = df.groupby("locality")["price"].mean()

# printing locality has the highest average price
print(f"Priceliest locality is {locality_avg_price.idxmax()} with average price of {locality_avg_price.max()}")

# problem 3. Which locality has the highest rate per square foot?
locality_avg_rate = df.groupby("locality")["rate_per_sqft"].mean()
print(f"Locality with highest rate per square foot is {locality_avg_rate.idxmax()} with average rate of {locality_avg_rate.max()}")

# problem 4. Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df["status"] == "Ready to move"]["price"].mean()
under_construction_avg_price = df[df["status"] == "Under Construction"]["price"].mean()
if ready_to_move_avg_price > under_construction_avg_price:
    print(
        f"Ready-to-move properties cost more than under-construction properties. Average price of ready-to-move properties is {ready_to_move_avg_price} while average price of under-construction properties is {under_construction_avg_price}"
    )

# problem 5. Do RERA-approved properties command a price premium?
# print(df["rera_approval"].value_counts(dropna=False))

rera_approved_avg_price = df[df["rera_approval"] == True]["price"].mean()
rera_not_approved_avg_price = df[df["rera_approval"] == False]["price"].mean()

if rera_approved_avg_price > rera_not_approved_avg_price:
    print(
        f"RERA-approved properties command a price premium. "
        f"Avg price: {rera_approved_avg_price:.2f} vs {rera_not_approved_avg_price:.2f}"
    )
else:
    print(
        f"No price premium. "
        f"RERA-approved avg: {rera_approved_avg_price:.2f}, "
        f"Non-RERA avg: {rera_not_approved_avg_price:.2f}"
    )

# problem 6. How does area (sqft) impact property price?
# ploting hit charts for How does area (sqft) impact property price?
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["area"], y=df["price"], alpha=0.3)
plt.title("Area (sqft) vs Price")
plt.xlabel("Area (sqft)")
plt.ylabel("Price")
# plt.show()

# problem 7. Which BHK configuration is the most expensive on average?
bhk_avg_price = df.groupby("flat_type")["price"].mean()
print(f"Most expensive BHK configuration is {bhk_avg_price.idxmax()} with average price of {bhk_avg_price.max()}")

# problem 8. Which property type (Apartment, Floor, Plot) is the costliest?
property_type_avg_price = df.groupby("property_type")["price"].mean()
print(f"Costliest property type is {property_type_avg_price.idxmax()} with average price of {property_type_avg_price.max()}")

# problem 9. Do certain builders or companies consistently price higher?
builder_avg_price = df.groupby("company_name")["price"].mean()
print(f"Builder with highest average price is {builder_avg_price.idxmax()} with average price of {builder_avg_price.max()}")

# problem 10. Are larger homes always more expensive per square foot?
larger_homes_avg_rate = df.groupby("area")["rate_per_sqft"].mean()
print(f"Larger homes have an average rate per square foot of {larger_homes_avg_rate.max()}")
