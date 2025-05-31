from dotenv import load_dotenv
load_dotenv()
import os
from jira import JIRA
from getpass import getpass

def get_credentials():
    """Load Jira credentials from environment or prompt user."""
    server = os.getenv('JIRA_SERVER')
    email = os.getenv('JIRA_EMAIL')
    api_token = os.getenv('JIRA_API_TOKEN')
    return server, email, api_token

def connect_to_jira(server, email, api_token):
    """Connect to Jira and return a Jira instance."""
    try:
        jira = JIRA(server=server, basic_auth=(email, api_token))
        return jira
    except Exception as e:
        print(f"Failed to connect to Jira: {e}")
        exit(1)

def fetch_todo_issues_for_all_projects(jira):
    """Fetch and print 'To Do' issues for all accessible projects."""
    projects = jira.projects()
    for project in projects:
        project_key = project.key
        print(f'\n--- "To Do" Issues in Project {project_key}: {project.name} ---')

        jql_query = f'project = {project_key} AND status = "To Do" ORDER BY created DESC'
        try:
            issues = jira.search_issues(jql_query)
            if not issues:
                print("No 'To Do' issues found.")
            else:
                for issue in issues:
                    print(f"{issue.key}: {issue.fields.summary}")
        except Exception as e:
            print(f"Failed to retrieve issues for project {project_key}: {e}")

def main():
    server, email, api_token = get_credentials()
    jira = connect_to_jira(server, email, api_token)
    fetch_todo_issues_for_all_projects(jira)

if __name__ == "__main__":
    main()
