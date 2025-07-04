import pandas as pd
import os
import datetime
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

# ✅ Logger
def log(msg):
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

# ✅ Extract
def extract_data(filepath):
    log(f"Reading file: {filepath}")
    return pd.read_csv(filepath)

# ✅ Transform
def transform_data(df):
    log("Filling missing values with 0...")
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    all_cols = numeric_cols + categorical_cols

    transformer = ColumnTransformer([
        ('fill_missing', SimpleImputer(strategy='constant', fill_value=0), all_cols)
    ], remainder='passthrough')

    pipeline = Pipeline(steps=[
        ('transformer', transformer)
    ])

    df_transformed = pipeline.fit_transform(df)
    return pd.DataFrame(df_transformed, columns=all_cols)

# ✅ Save
def load_data(df, output_path):
    df.to_csv(output_path, index=False)
    log(f"Saved cleaned data to: {output_path}")

# ✅ Process One File
def process_file(input_path, output_folder):
    try:
        df = extract_data(input_path)
        df_cleaned = transform_data(df)

        filename = os.path.basename(input_path)
        output_path = os.path.join(output_folder, f"cleaned_{filename}")
        load_data(df_cleaned, output_path)
    except Exception as e:
        log(f"Error processing {input_path}: {e}")

# ✅ Process All Files in Folder
def run_pipeline_on_folder(input_folder, output_folder):
    log("🚀 Starting batch processing...")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith(".csv"):
            file_path = os.path.join(input_folder, file)
            process_file(file_path, output_folder)

    log("✅ Finished processing all CSV files.")

# ✅ Run Script
if __name__ == "__main__":
    input_folder = r"C:\Users\cheth\OneDrive\Desktop\CSV Files"
    output_folder = r"C:\Users\cheth\OneDrive\Desktop\CSV Files\Cleaned"

    run_pipeline_on_folder(input_folder, output_folder)
