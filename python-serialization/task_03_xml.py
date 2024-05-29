import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to the given filename.

    :param dictionary: The Python dictionary to serialize.
    :param filename: The name of the file to save the XML data.
    """
    # Create the root element
    root = ET.Element("data")

    # Iterate through the dictionary items and add them as child elements to the root
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    # Write the XML tree to the provided filename
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Reads the XML data from the given filename and returns a deserialized Python dictionary.

    :param filename: The name of the file to read the XML data from.
    :return: A Python dictionary with the deserialized data.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Navigate through the XML elements to reconstruct the dictionary
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None

    except ET.ParseError:
        print(f"An error occurred while parsing the XML file: {filename}")
        return None
