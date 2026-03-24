import pandas as pd

# Load dataset
df = pd.read_csv("content_data.csv")

# Basic analysis
print("Total Content:", len(df))
print("\nCategory Distribution:\n", df['category'].value_counts())

# Flagged content
flagged = df[df['flagged'] == 'Yes']
print("\nFlagged Content:", len(flagged))

# Violations
violations = df[df['decision'] == 'Removed']
print("\nPolicy Violations:", len(violations))

# Insights
print("\nTop Violating Category:")
print(violations['category'].value_counts().idxmax())
