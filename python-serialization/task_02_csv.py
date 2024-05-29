import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.

    :param csv_filename: The name of the CSV file to be converted.
    :return: True if the conversion was successful, False otherwise.
    """
    try:
        # Open the CSV file and read the data
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        # Serialize the list of dictionaries to JSON
        with open('data.json', mode='w') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"File not found: {csv_filename}")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
