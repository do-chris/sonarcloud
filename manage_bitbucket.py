#!/usr/local/bin/python3
import requests
import json
import os
from requests.auth import HTTPBasicAuth

space_key  = os.getenv('space_key')
space_name = os.getenv('space_name')
space_desc = os.getenv('space_desc')
username   = os.getenv('username')
password   = os.getenv('atlassian_cli_pw')
url = "https://ddevops-bitbucket.prod-aws-atlassian.com"
auth = HTTPBasicAuth(username, password)
headers = {"X-Atlassian-Token":"no-check"}

def api_execute(api_call, call, json_data="Optional"):
    if call == "get":
        req = requests.get(url + api_call, headers=headers, auth=auth)
    elif call == "post":
        req = requests.post(url + api_call, headers=headers, auth=auth)
    elif call == "delete":
        req = requests.delete(url + api_call, headers=headers, auth=auth)
    elif call == "json":
        req = requests.post(url + api_call, headers=headers, json=json_data, auth=auth)
    return req.status_code, req.text

def list():
    data = api_execute("/rest/api/1.0/admin/users?limit=1000", "get")
    for users in data['values']:
        print("Name : " + users['displayName'])
        print("Email: " + users['name'])
        print("Deletable: " + str(users['deletable']))
        try:
            print("Access: " + str(users['lastAuthenticationTimestamp']) + "\n")
        except:
            print("Access: Not logged in\n")

def add_user(name, password, displayname, emailaddress, addtodefaultgroup):
    data = api_execute("/rest/api/1.0/admin/users?name=" + name + "&password="
            + password + "&displayName=" + displayname + "&emailAddress="
            + emailaddress + "&addToDefaultGroup=" + addtodefaultgroup, "post")
    return data

def delete_user(name):
    data = api_execute("/rest/api/1.0/admin/users?name=" + name, "delete")
    return data

def add_group(name):
    data = api_execute("/rest/api/1.0/admin/groups?name=" + name, "post")
    return data

def delete_group(name):
    data = api_execute("/rest/api/1.0/admin/groups?name=" + name, "delete")
    return data

def add_to_group(name,groups):
    json_data = {"user":name, "groups":[groups]}
    headers = {'Content-type': 'application/json'}
    data = api_execute("/rest/api/1.0/admin/users/add-groups", "json", json_data)
    return data

def create_project(space_key, space_name, space_desc):
    json_data = {"key":space_key, "name":space_name, "description":space_desc}
    headers = {'Content-type': 'application/json'}
    data = api_execute("/rest/api/1.0/projects", "json", json_data)
    return data

if __name__ == "__main__":
    print(create_project(space_key, space_name, space_desc))
    space_name = space_name.replace(' ','')
    print(add_group(f"Project-{space_name}"))
