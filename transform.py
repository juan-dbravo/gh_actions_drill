import os

# Ensure the transform outpud directory exists
os.makedirs("data/transformed", exist_ok=True)

# Simulate reading cleaned data
with open("data/clean/data_cleaned.csv", "r") as infile:
    lines = infile.readlines()

# Simulate writing transformed data
with open("data/transformed/data_transformed.csv", "w") as outfile:
    for line in lines:
        outfile.write(line.upper())  # Just a dummy transformation


print("✅ Transformed data saved to data/transformed/data_transformed.csv")
