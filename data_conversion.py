import camelot
import os
import pandas as pd
import re


def extract_year(file_name):
    pattern = r"\b\d{4}\b"
    match = re.search(pattern, file_name)
    if match:
        return match.group()
def pdf_to_csv():
    directory = "./Turkey Car Sales Report"
    output_directory = "./Turkey Car Sales Table Data"
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            tables = camelot.read_pdf(f"{directory}/{filename}")
            filename = filename.split(".")
            filename[0] = extract_year(filename[0])
            filename[1] = "csv"
            filename = ".".join(filename)
            tables[0].to_csv(f"{output_directory}/{filename}")
    csv_cleanup()

def csv_cleanup():
    directory = "./Turkey Car Sales Table Data"
    for filename in os.listdir(directory):
        df = pd.read_csv(f"{directory}/{filename}")
        for index, value in df.iloc[:, 0].items():
            if type(value) == float or type(value) == int:
                df = df.drop(index)
            elif value == "ALFA ROMEO":
                df.drop(df.index[:index], inplace=True)
            elif "TOPLAM" in value:
                df = df.drop(index)
        df = df.reset_index(drop=True)
        df.columns.values[0] = "MARKA"
        df.columns.values[3] = "SATIŞ"
        df = df.iloc[:, [0, 3]]
        df.to_csv(f"{directory}/{filename}")
