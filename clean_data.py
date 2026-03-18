from pathlib import Path
import pandas as pd

downloads = Path.home() / "Downloads"

input_file = downloads / "input.csv"
output_file = downloads / "cleaned_data.csv"

df = pd.read_csv(input_file)

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()
df = df.dropna(how="all")

df.to_csv(output_file, index=False)

print(f"Cleaned data saved to: {output_file}")
