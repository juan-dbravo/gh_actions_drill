import os

# Ensure the final otput directory exists
os.makedirs("data/final", exist_ok=True)

# Simulate reading transformed data
with open("data/transformed/data_transformed.csv", "r") as infile:
    lines = infile.readlines()

# Simulate writing final loaded data
with open("data/final/final_output.csv", "w") as outfile:
    outfile.writelines(lines)

print("✅ Final output saved to data/final/final_output.csv")