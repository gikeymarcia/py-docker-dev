import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
import os

def list_files():
    # Print the current working directory
    print(f"Current Working Directory: {os.getcwd()}")

    # Walk through the directory
    for root, dirs, files in os.walk("."):
        # Skip .git directory
        if '.git' in root:
            continue

        print(f"\nDirectory: {root}")
        for file in files:
            print(f" - {file}")

def extract_tables_from_html(file_path):
    # Reading the HTML file
    with open(file_path, 'r') as html_file:
        content = html_file.read()
        print(content)

    # Using BeautifulSoup to parse HTML content
    soup = BeautifulSoup(content, 'lxml')

    # Extracting tables
    tables = soup.find_all('table')
    extracted_tables = []

    for i, table in enumerate(tables):
        # Parsing each table with Pandas and converting to a DataFrame
        df = pd.read_html(StringIO(str(table)))[0]
        extracted_tables.append(df)

        # Optional: Save each table as a CSV file
        df.to_csv(f'data/table_{i}.csv', index=False)

        # Save each table as an Excel file
        df.to_excel(f'data/table_{i}.xlsx', engine='openpyxl')

    return extracted_tables

if __name__ == "__main__":
    print('hello from app.py')
    list_files()
    file_path = 'data/input.html'
    tables = extract_tables_from_html(file_path)

    # Just for demonstration: print the first table
    if tables:
        print("First Extracted Table:")
        print(tables[0])

# vim: foldlevel=4 :
