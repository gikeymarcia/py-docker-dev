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

def extract_tables_with_context(file_path):
    # Reading the HTML file
    with open(file_path, 'r') as html_file:
        content = html_file.read()

    # Using BeautifulSoup to parse HTML content
    soup = BeautifulSoup(content, 'lxml')

    # Extracting tables
    tables = soup.find_all('table')
    extracted_tables = []

    for i, table in enumerate(tables):
        # Attempt to find the title attribute or a nearby header for context
        title = table.get('title') or table.find_previous(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']).get_text(strip=True)

        # Parsing each table with Pandas and converting to a DataFrame
        df = pd.read_html(StringIO(str(table)))[0]
        extracted_tables.append((title, df))

        # Pretty-print the context and the table
        print(f"Context: {title}")
        print(df)

        # Save each table as an Excel file using the title or index as filename
        filename = f"data/{title or f'table_{i}'}.xlsx"
        df.to_excel(filename, engine='openpyxl')

    return extracted_tables

if __name__ == "__main__":
    list_files()
    file_path = 'data/input.html'
    tables = extract_tables_with_context(file_path)

    # Just for demonstration: print the first table
    if tables:
        print("First Extracted Table:")
        print(tables[0])

# vim: foldlevel=4 :
