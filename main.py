import http.client
import json

#This is the function that gets the user's activity from the git-hub repo
def get_activity(username):
    host = "api.github.com"
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", f"/users/{username}/events/public", headers={"Host":host, "Accept":"application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28", "User-Agent":"RashnerdUX",},)
    response = conn.getresponse()
    print(f"Connection code - {response.status}")

    parsed_data = json.load(response)
    return parsed_data

def show_activity(response):
    activity_list = []
    error_no = 0
    for item in response:
        try:
            activity_repo = item["repo"]["name"]
            activity_type = item["type"]
            activity_dict = {"type":activity_type, "repo":activity_repo}
            activity_list.append(activity_dict)
        except (KeyError, IndexError):
            print("The message can't be found")
            error_no+=1
    print(f"Number of errors during request - {error_no}")
    return activity_list

def output_print(activities_list):
    print("Let's parse the activities")

    #This ensures that the output has no repeat of events performed on the same repo
    processed_activities = set()

    #This ensures that every commit made to a repo is counted and there are no repeats
    push_repo_counts = {}

    #This is the list of outputs to be returned
    user_activity = []

    for item in activities_list:
        repo_name = item["repo"]
        event_type = item["type"]

        if event_type == "PushEvent":
            if repo_name in push_repo_counts:
                push_repo_counts[repo_name] += 1
            else:
                push_repo_counts[repo_name] = 1
        else:
            activity_key = (repo_name, event_type)
            if activity_key not in processed_activities:
                if event_type == "ForkEvent":
                    user_activity.append(f"Forked the repo - {repo_name}")
                elif event_type == "CreateEvent":
                    user_activity.append(f"Created a new repository called {repo_name}")
                elif event_type == "DeleteEvent":
                    user_activity.append(f"Deleted a repository - {repo_name}")
                elif event_type == "IssuesEvent":
                    user_activity.append(f"Attended to some issues on {repo_name}")
                elif event_type == "PullRequestEvent":
                    user_activity.append(f"Pulled some files from {repo_name} to local repo")

                processed_activities.add(activity_key)

    for repo_name, count in push_repo_counts.items():
        user_activity.append(f"Pushed {count} commits to the repo - {repo_name}")

    user_activity.append("Among other events that weren't captured due to my laziness")

    return user_activity


#This is the start of the program
print("Hello, this is a Github App for checking your activity on the app\nTo begin, please enter your Git username")
username = input("Enter your username here: ")
data = get_activity(username)
data_list = show_activity(data)
user_data = output_print(data_list)

print("Here's the Output")
for line in user_data:
    print(line)

