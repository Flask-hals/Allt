import requests

def load():
   site = requests.get("https://www.ida.liu.se/~TDP003/current/projekt/datalagertester/data.json")
   if site.status_code != 200:
       return None
   else:
       data = site.json()
       print(data)
       return data
data = load()

def get_project_count(data):
    print(len(data))
get_project_count(data)

def get_project(data, project_id):
    for projects in range(len(data)):
        if project_id == data[projects]["project_id"]:
            print(data[projects])
get_project(data, 3)
