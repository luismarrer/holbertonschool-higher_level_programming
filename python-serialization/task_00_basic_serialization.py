import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    :param data: A Python dictionary with data.
    :param filename: The filename of the output JSON file. If the file already exists, it should be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file to a Python dictionary.

    :param filename: The filename of the input JSON file.
    :return: A Python dictionary with the deserialized data from the file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
