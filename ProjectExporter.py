import datetime
import os
import csv

from atlassian import Jira

url = os.getenv('JIRA_URL')
username = os.getenv('CONFLUENCE_USER')
password = os.getenv('CONFLUENCE_API_TOKEN')    #api token

print("Using URL=" + url)
print("Using User=" + username)
print("Using PW=" + password)

# This creates connection object where you provide your confluence URL  and credentials.
jira = Jira(
    url,
    username,
    password,   # api token
    )

projects = []
filelocation = "/Users/jt/Google Drive/My Drive/Jira Export/Projects/"
#get all the projects on the Jira server and write out to CSV
projects = jira.projects()
with open(filelocation + 'Jira_Projects-' + str(datetime.date.today()) + '.csv', 'w') as file:
    #create the header row
    print("creating header row")
    header = []
    header.append("key")
    header.append("name")
    header.append("id")
    header.append("projectTypeKey")
    header.append("archived")
    header.append("lastIssueUpdate")
    writer = csv.writer(file)
    writer.writerow(header)

    #now write a row for each project
    for project in projects:
        new_data = []
        print("processing project: " + project['name'])
        #write each project into a csv file
        new_data.append(project['key'])
        new_data.append(project['name'])
        new_data.append(project['id'])
        new_data.append(project['projectTypeKey'])
        if 'archived' in project:
            new_data.append(str(project['archived']))
        # issues = jira.sea ("project = " + project['key'] + ", maxResults = 1, fields = 'updated'")
        #for issue in issues:
        #    new_data.append(issue.fields.updated)
        writer = csv.writer(file)
        writer.writerow(new_data)
print("done processing projects")