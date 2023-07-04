```python
import os
import json

# Shared dependencies
app_config = "app_config.json"
setup_status = "setup_status.txt"
setup_message = "setup_message.txt"

def setup_app():
    try:
        with open(app_config) as config_file:
            config_data = json.load(config_file)
            
        # Setup process based on the config_data
        # This is a placeholder for the actual setup process
        # Add your setup code here

        with open(setup_status, 'w') as status_file:
            status_file.write('Setup completed successfully')
        
        with open(setup_message, 'w') as message_file:
            message_file.write('Setup completed without any issues')
            
    except Exception as e:
        with open(setup_status, 'w') as status_file:
            status_file.write('Setup failed')
        
        with open(setup_message, 'w') as message_file:
            message_file.write('Setup failed with error: ' + str(e))

if __name__ == "__main__":
    setup_app()
```