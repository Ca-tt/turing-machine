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
        

    # ? save / load from file logic wrappers
    def _save_to_file(self):
        input_string = self.input_entry.get()
        # ? read rules to update self.rules
        self.read_rules()
        self.save_to_file(input_string, self.rules)


    def _load_from_file(self):
        input_string, loaded_rules = self.load_from_file()
        print("🐍 input_string", input_string)
        print("🐍  loaded_rules ", loaded_rules)

        if input_string is not None:
            # Set input field text
            self.input_entry.delete(0, "end")
            self.input_entry.insert(0, input_string)

        if loaded_rules is not None:
            # Set rules
            self.rules = loaded_rules

            # Clear existing rule entries, set new texts for them
            for entry, (left_part, right_part) in zip(
                self.rule_entries, self.rules.items()
            ):
                # print("🐍  key",left_part)
                # print("🐍  value",right_part)
                regexp = r"['() ]"

                old_state = sub(regexp, "", left_part[0])
                read_value = sub(regexp, "", left_part[1])

                new_state = right_part[0]
                write_value = right_part[1]

                direction = right_part[2]

                rule_text = (
                    f"{old_state},{read_value} -> {new_state},{write_value},{direction}"
                )
                entry.delete(0, "end")
                entry.insert(0, rule_text)

            self.set_tape_text()
