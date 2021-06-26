# YAML file contains all the Validation and Convertion
# methods for different formats.
import json
import yaml

class Yaml():

    # Validation component contains logic for Validating
    # if Input Text conforms to this Language.
    def validate(self, some_string):
        try:
            yaml_data = yaml.load(some_string)
        except:
            return False
        return True

    # Every Convertion Format must start with 'convert_to_'
    # followed by format name.
    def convert_to_json(self, input_string):
        yaml_data = yaml.load(input_string)
        json_data = json.dumps(yaml_data)
        return json_data
