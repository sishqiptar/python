import pandas as pd

def find_missing_integers(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Find the integer that exists in column "B" but not in column "A"
    missing_b = set(df[1]) - set(df[0])
    print("Integer in column 'B' but not in column 'A':", missing_b.pop())

    # Find the integer that is missing from both columns
    missing_both = set(df[0]) ^ set(df[1])
    print("Integer missing from both columns:", missing_both.pop())

# Test the program with the provided "sample.csv"
find_missing_integers("sample (1).csv")