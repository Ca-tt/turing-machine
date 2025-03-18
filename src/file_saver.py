import json
from os.path import relpath, normpath, abspath, join, dirname


class FileSaver:
    def __init__(self, json_file_name="turing.json"):
        base_dir = dirname(abspath(__file__))
        files_dir = join(base_dir, "..", "files")

        # Construct the full path
        self.file_path = join(files_dir, json_file_name)


    def save_to_file(self, input_string: str, rules: dict[tuple[str, str], tuple[str, str]]):
        # Convert tuple keys to strings
        converted_rules = {str(k): v for k, v in rules.items()}
        
        data = {"input": input_string, "rules": converted_rules}

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
                print("data successfully saved!")
        except Exception as e:
            print(f"Error saving file: {e}")


    def load_from_file(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Convert rule keys back to tuples
            rules_deserialized = {tuple(k.split(",")): v for k, v in data["rules"].items()}

            return data["input"], rules_deserialized
        except Exception as e:
            print(f"Error loading file: {e}")
            return None, None
