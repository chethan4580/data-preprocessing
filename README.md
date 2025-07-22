Data Preprocessing
This project performs automated data preprocessing on multiple CSV files in a folder. It reads each file, fills missing values with zero, and saves the cleaned version to a new folder.

Features
Processes all .csv files in a specified input folder

Fills missing numeric and categorical values with 0

Saves output files in a separate Cleaned folder with cleaned_ prefix

Folder Structure
markdown
Copy
Edit
CSV Files/
├── file1.csv
├── file2.csv
└── Cleaned/
    ├── cleaned_file1.csv
    └── cleaned_file2.csv
How to Use
Install required packages:

bash

pip install pandas scikit-learn
Update these paths in the script:

python

input_folder = r"C:\Path\To\CSV Files"
output_folder = r"C:\Path\To\CSV Files\Cleaned"

Run the script:

bash
python pipeline.py

Process Overview

Extract: Reads each CSV file
Transform: Replaces missing values using SimpleImputer
Load: Saves cleaned data to the output folder




