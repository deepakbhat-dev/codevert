import sys
from .JSON import Json
from .YAML import Yaml

# The Languages supported currently with the Object name
# must be added to this Dictionary to Run.
SUPPORTED_LANG = {"json": "Json", "yaml": "Yaml"}

# Class to hold logic for detecting the language of string.
class DetectFactory(object):
    def __init__(self, input_string):
        self.input_string = input_string
    def detect_text(self):
        detected_format = detect_string(self.input_string)
        return detected_format

def detect_string(random_string):
    # Try validate method on all supported languages until Validation
    # completes successfully.
    for lang in SUPPORTED_LANG:
        class_name = SUPPORTED_LANG[lang]
        class_obj = getattr(sys.modules[__name__], class_name)
        detect_obj = class_obj()                     # Object to be used for validating string
        if detect_obj.validate(random_string):
            return lang
    return "error"

# Class to hold logic for converting string to required language.
class ConvertFactory(object):
    def __init__(self, input_format, output_format, input_string):
        self.input_format = input_format
        self.output_format = output_format
        self.input_string = input_string
    def do_conversion(self):
        convert_obj = ConvertFinder(self.input_format, self.output_format,
                                        self.input_string)
        converted_data = convert_obj.convert()
        return converted_data

# Class that calls respective convertion method based on Required conversion
# format input by the user.
class ConvertFinder(object):
    def __init__(self, input_lang, output_lang, input_string):
        self.input_lang = input_lang
        self.output_lang = output_lang
        self.input_string = input_string
    def convert(self):
        class_name = SUPPORTED_LANG[self.input_lang]
        lang_obj = getattr(sys.modules[__name__], class_name)()  # Object to be used for converting string
        convert_required = "convert_to_" + str(self.output_lang.lower())
        try:
            # Call convertion method based on required output language.
            return getattr(lang_obj, convert_required)(self.input_string)
        except:
            return "error"
