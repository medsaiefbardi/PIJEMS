import pandas as pd

def clean_data(file_path, output_path):
    """Clean raw data and save the processed data."""
    df = pd.read_csv(file_path)

    # Example: Remove duplicates
    df = df.drop_duplicates()

    # Example: Fill missing values
    df.fillna("N/A", inplace=True)

    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
    return df
