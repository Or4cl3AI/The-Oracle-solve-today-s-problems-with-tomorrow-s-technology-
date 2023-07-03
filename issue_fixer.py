```python
import json

# Shared dependencies
config_data = {}
issue_data = {}
app_status = ""

def load_config():
    global config_data
    with open('config_data.json', 'r') as file:
        config_data = json.load(file)

def load_issues():
    global issue_data
    with open('issue_data.json', 'r') as file:
        issue_data = json.load(file)

def update_app_status(status):
    global app_status
    app_status = status
    with open('app_status.txt', 'w') as file:
        file.write(app_status)

def fix_issue(issue_id):
    global issue_data
    if issue_id in issue_data:
        issue_data[issue_id]['status'] = 'fixed'
        with open('issue_data.json', 'w') as file:
            json.dump(issue_data, file)
        update_app_status('issue_fixed')
        print(f"Issue {issue_id} has been fixed.")
    else:
        print(f"No issue found with id {issue_id}.")

if __name__ == "__main__":
    load_config()
    load_issues()
    for issue in issue_data:
        if issue_data[issue]['status'] != 'fixed':
            fix_issue(issue)
```
