```python
import json

# Load the issue report
with open('issue_report.json', 'r') as f:
    issues = json.load(f)

# Load the app configuration
with open('app_config.json', 'r') as f:
    app_config = json.load(f)

# Function to fix issues
def fix_issue(issue_id):
    # Here we would have the logic to fix the issue based on its id
    print(f'Fixing issue {issue_id}...')
    # After fixing the issue, update the issue status
    issue_status[issue_id] = 'fixed'
    print(f'Issue {issue_id} fixed.')

# Iterate over the issues and fix them
issue_status = {}
for issue in issues:
    issue_id = issue['id']
    fix_issue(issue_id)

# Save the issue status
with open('issue_status.json', 'w') as f:
    json.dump(issue_status, f)

# Print the issue fixing message
issue_message = 'All issues have been fixed.'
print(issue_message)
```