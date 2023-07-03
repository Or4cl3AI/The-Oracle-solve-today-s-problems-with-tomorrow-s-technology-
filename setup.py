```python
import json

# Shared dependencies
config_data = {}
issue_data = {}
app_status = "Not Setup"
setup_complete = False

def load_config():
    global config_data
    with open('config.json') as json_file:
        config_data = json.load(json_file)

def init_setup():
    global app_status
    load_config()
    # Assuming the config_data has a key 'setup' which needs to be True for setup to be complete
    if config_data.get('setup', False):
        app_status = "Setup Complete"
        setup_complete = True
        print("Setup Complete")
    else:
        app_status = "Setup Incomplete"
        print("Setup Incomplete")

if __name__ == "__main__":
    init_setup()
```