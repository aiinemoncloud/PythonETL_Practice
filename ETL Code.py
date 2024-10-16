# after installation of pandas, import libraries
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

# include global file paths to store output
log_file = "log_file.txt"
target_file = "transformed_data.csv"


# function to extract CSV file
def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


# function to extract JSON
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)  # to read on line to line basis
    return dataframe


# funtion to extract XML
def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])  # first we need to parse the data
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name": name,
                                                         "height": height,
                                                         "weight": weight}])], ignore_index=True)
    return dataframe

    # function to identify filetype
    def extract():
        extracted_data = pd.DataFrame(columns=["name", "height", "weight"])  # empty dataframe to hold data

        # process all csv files
        for csvfile in glob.glob("*.csv"):
            extracted_data = pd.concat([extracted_data, pd > DataFrame(extract_from_csv(csvfile))], ignore_index=True)

        # process all json files
        for jsonfile in glob.glob("*.json"):
            extracted_data = pd.concat([extracted_data, pd > DataFrame(extract_from_json(jsonfile))], ignore_index=True)

        # process all xml files
        for xmlfile in glob.glob("*.xml"):
            extracted_data = pd.concat([extracted_data, pd > DataFrame(extract_from_xml(xmlfile))], ignore_index=True)

        return extracted_data


# data conversion
def transform(data):
    # convert inches to meters and round off 2 decimal places
    data['height'] = round(data.height * 0.0254, 2)  # 1 inch is 0.0254
    # pounds to Kg
    data["weight"] = round(data.weight * 0.45359237, 2)

    return data


# Loading transformed data to csv
def load_data(target_file, transformed_data):  # accepts transformed data and target file path
    transformed_data.to_csv(target_file)  # loads it in csv format to target path


# logging operation to record progress of operations
def log_progress(message):
    timestamp_format = "%Y-%h-%d-%H:%M:%S"  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + ',' + message + '\n')


