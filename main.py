from jira import JIRA

# Replace these with your Jira details
JIRA_SERVER = 'https://yorkhackathonteam4.atlassian.net/'  # Your Jira instance URL
EMAIL = 'yorkhackathonteam4@gmail.com'                   # Your Jira login email
API_TOKEN = 'ATATT3xFfGF0wC7r1J3HB7kGYulggoJ7fdZ3NLzHEXwqxBZoyCYB-JQAdQVWoiqfaleo4cjo0qgmJ464KB2CUIGlZwbkVcJRmsJQNvTyoC73NUFUF0AmLKVXJNNHFbQlKbv3SZe4hHthzxm7KXP3rhjP5lD-fcPGUxYsp4H4cdm2EA1Fay8k6TE=8DFE29A6'
                  # Your Jira API token (not password)

# Connect to Jira
jira = JIRA(server=JIRA_SERVER, basic_auth=(EMAIL, API_TOKEN))

# Get all projects
projects = jira.projects()

# Print project key and name
for project in projects:
    print(f"{project.key}: {project.name}")


# Project key
project_key = 'WEAT'  # Replace with the actual project key

# JQL query to get "To Do" issues in the project
jql_query = f'project = {project_key} AND status = "To Do" ORDER BY created DESC'

# Fetch issues
issues = jira.search_issues(jql_query)

# Print issue keys and summaries
print(f'"To Do" issues in project {project_key}:')
for issue in issues:
    print(f"{issue.key}: {issue.fields.summary}")