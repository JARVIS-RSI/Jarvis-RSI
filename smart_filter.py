import pandas as pd

def extract_specific_data(source_file, target_name):
    try:
        df = pd.read_excel(source_file)
        filtered = df[df['Name'].str.contains(target_name, case=False)]
        output = f"{target_name}_data.xlsx"
        filtered.to_excel(output, index=False)
        return f"Data for {target_name} saved in {output}"
    except Exception as e:
        return f"Error: {e}"
