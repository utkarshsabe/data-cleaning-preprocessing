import pandas as pd

# Read CSV file
df = pd.read_csv("student_data.csv")

# Display original data
print("Original Dataset:")
print(df)

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Correct inconsistent data
df["Gender"] = df["Gender"].str.capitalize()

# Convert Age to integer
df["Age"] = df["Age"].astype(int)

# Save cleaned data
df.to_csv("cleaned_student_data.csv", index=False)

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df)