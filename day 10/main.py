import json
from webbrowser import get

def load_config(path= "config.json"):
    try:
        with open (path , "r") as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        print(f"Your file {path} is not found.")
        return None

config = load_config()
print(config)

#check username variable exist in config inside database in json
for key in config.get("database", {}):  # Iterate over keys in the database section
    if key == "port":                   # Check if the key is "port" is present in database section
        print(f"Port exists in database: {config['database']['port']}") # Print the port value  
        break
    