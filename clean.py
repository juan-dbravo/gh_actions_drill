import os

# Ensure the clean output directory exists
os.makedirs("data/clean", exist_ok=True)

# Write dummy cleaned data
with open("data/clean/data_cleaned.csv", "w") as f:
    f.write("Those who dream by day are cognisant of many things which escape those who dream only by night\n")

print("✅ data_cleaned.csv written")