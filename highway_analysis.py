import pandas as pd
import matplotlib.pyplot as plt

# 1. Read data
df = pd.read_csv("china_highways.csv")

# 2. Show basic information
print("China Highway Network Dataset:")
print(df)

print("\nTotal highways:", len(df))

# 3. Count highways by network type
type_counts = df["network_type"].value_counts()

print("\nHighways by network type:")
print(type_counts)

# 4. Create comparison chart
plt.figure(figsize=(8, 5))

type_counts.plot(kind="bar")

plt.title("China National Highway Network Structure")
plt.xlabel("Network Type")
plt.ylabel("Number of Highways")

plt.xticks(rotation=0)

plt.tight_layout()

# 5. Save chart
plt.savefig(
    "highway_network_structure.png",
    dpi=300
)

plt.show()

print("\nChart saved as:")
print("highway_network_structure.png")