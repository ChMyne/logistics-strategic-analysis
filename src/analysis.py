import pandas as pd
import matplotlib.pyplot as plt

# Load logistics dataset
data = pd.read_csv("data/logistics_data.csv")

# Display first five records
print("First five records:")
print(data.head())

# Calculate KPIs
total_orders = len(data)

on_time_orders = len(data[data["on_time"] == "Yes"])
on_time_delivery_rate = (on_time_orders / total_orders) * 100

average_delivery_time = data["delivery_time"].mean()

average_transportation_cost = data["transportation_cost"].mean()

low_inventory_orders = len(data[data["inventory_level"] < 30])
stockout_risk_rate = (low_inventory_orders / total_orders) * 100

# Display results
print("\n----- LOGISTICS KPIs -----")
print(f"Total Orders: {total_orders}")
print(f"On-Time Delivery Rate: {on_time_delivery_rate:.2f}%")
print(f"Average Delivery Time: {average_delivery_time:.2f} days")
print(f"Average Transportation Cost: ₹{average_transportation_cost:.2f}")
print(f"Low Inventory Risk Rate: {stockout_risk_rate:.2f}%")

# Average delivery time by warehouse
warehouse_delivery = data.groupby("warehouse")["delivery_time"].mean()

print("\nAverage Delivery Time by Warehouse:")
print(warehouse_delivery)

# Create chart
warehouse_delivery.plot(
    kind="bar",
    title="Average Delivery Time by Warehouse"
)

plt.xlabel("Warehouse")
plt.ylabel("Average Delivery Time (Days)")
plt.tight_layout()

plt.savefig("delivery_time_by_warehouse.png")

print("\nAnalysis completed successfully.")
