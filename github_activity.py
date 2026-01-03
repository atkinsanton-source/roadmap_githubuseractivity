import requests
import sys
import json

def main():
    if len(sys.argv) >=1:
        try:
            username =  sys.argv[1]
            activity(username)
        except IndexError:
            print("Usage: python github_activity.py <username>")           
    else:
        print("Usage: python github_activity.py <username>")

def activity(username):
    url = (f"https://api.github.com/users/{username}/events")
    r = requests.get(url)
    data = r.json()
    counter_pushevents = 0
    counter_watchevents = 0
    counter_createevents = 0
    counter_issuesevent = 0
    counter_forkedevents = 0
    counter_public = 0
    if r.status_code == 200:
        for x in data:
            repo = x["repo"]["name"]
            if x["type"] == "PushEvent":
                counter_pushevents += 1
                print(f"{username} pushed to {repo}.")
            elif x["type"] == "WatchEvent":
                counter_watchevents += 1
                print(f"{username} starred {repo}.")
            elif x["type"] == "IssuesEvent":
                counter_issuesevent += 1
                action_issued = x["payload"]["action"]
                print(f"{username} {action_issued} a issue in {repo}.")
            elif x["type"] == "CreateEvent":
                counter_createevents += 1
                ref_type = x["payload"]["ref_type"]
                print(f"Created {ref_type} in {repo}.")
            elif x["type"] == "ForkEvent":
                counter_forkedevents += 1
                print(f"Forked {repo}")
            elif x["type"] == "PublicEvent":
                counter_public += 1
                print(f"{username} made {repo} public.")
        print(f"Overall stats: Pushed --> {counter_pushevents}, Starred -->{counter_watchevents}, Issued --> {counter_issuesevent}, Created -->{counter_createevents}, Forked --> {counter_forkedevents}, Publicized --> {counter_public}")

    else:
        print("User not found or API error.")





    #pushevents_list = [[x["type"], x["repo"]["name"]] for x in data if x["type"] == "PushEvent"]
    #watchevents_list = [[x["type"], x["repo"]["name"]] for x in data if x["type"] == "WatchEvent"]
    #createevents_list = [[x["type"], x["repo"]["name"]] for x in data if x["type"] == "CreateEvent"]
    #print(f"Amount of events pushed: {len(pushevents_list)}, Amount of events watched: {len(watchevents_list)}, Amount of events created: {len(createevents_list)}")


if __name__ == "__main__":
    main()
