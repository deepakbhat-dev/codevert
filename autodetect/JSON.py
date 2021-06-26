# JSON file contains all the Validation and Convertion
# methods for different formats.
from collections import OrderedDict
import pyaml
import json

class Json():

    # Validation component contains logic for Validating
    # if Input Text conforms to this Language.
    def validate(self, some_string):
        try:
            json_data = json.loads(some_string)
        except:
            return False
        return True

    # Every Convertion Format must start with 'convert_to_'
    # followed by format name.
    def convert_to_yaml(self, input_string):
        json_data = json.loads(input_string, object_pairs_hook=OrderedDict)
        yaml_data = pyaml.dump(json_data)
        return yaml_data
