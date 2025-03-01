# GitHub Activity Tracker
Link to project info - https://roadmap.sh/projects/github-user-activity

This Python script retrieves and displays a user's public GitHub activity. It fetches event data from the GitHub API, parses it, and presents a summary of the user's actions.

## Features

* **Retrieves GitHub Activity:** Fetches public event data for a specified GitHub username using the GitHub API.
* **Parses Activity Data:** Extracts relevant information from the API response, including event types and repository names.
* **Summarizes Activity:** Generates a human-readable summary of the user's actions, including:
    * Counting the number of `PushEvent` occurrences for each repository.
    * Listing other event types (e.g., `ForkEvent`, `CreateEvent`) without repetition.
* **Error Handling:** Handles API connection errors and data parsing errors.

## Usage

1.  **Installation:**
    * Ensure you have Python 3 installed.
    * No external libraries are required; the script uses the standard Python libraries (`http.client` and `json`).

2.  **Running the Script:**
    * Save the Python code to a file (e.g., `github_activity.py`).
    * Run the script from your terminal: `python github_activity.py`.

3.  **Input:**
    * The script will prompt you to enter your GitHub username.

4.  **Output:**
    * The script will display a summary of your GitHub activity, including:
        * The number of commits pushed to each repository.
        * A list of other events (forks, creations, etc.) without repetitions.
        * A message indicating other events that were not captured.
        * The connection status code.
        * The number of errors during data requests.

## Code Explanation

### `get_activity(username)`

* This function makes a GET request to the GitHub API to retrieve the public events for the specified username.
* It uses the `http.client` library to establish an HTTPS connection.
* It sets the necessary headers, including the API version and user agent.
* It parses the JSON response from the API and returns the parsed data.
* It also prints the HTTP response status code.

### `show_activity(response)`

* This function parses the JSON response from the GitHub API.
* It extracts the event type and repository name for each event.
* It handles potential `KeyError` and `IndexError` exceptions during parsing.
* It also prints the number of errors that occured during the request.
* It returns a list of dictionaries, where each dictionary represents an event.

### `output_print(activities_list)`

* This function processes the list of activity dictionaries.
* It counts the number of `PushEvent` occurrences for each repository.
* It uses a set to prevent repetition of other event types.
* It generates a list of human-readable activity descriptions.
* It returns the list of activity descriptions.

### Main Execution

* The script prompts the user for their GitHub username.
* It calls the `get_activity()` function to retrieve the user's activity data.
* It calls the `show_activity()` to parse the data.
* It calls the `output_print()` function to generate the activity summary.
* It prints the activity summary to the console.

## Dependencies

* Python 3
* Standard Python libraries: `http.client`, `json`

## Notes

* The script only retrieves public events.
* Error handling is basic and can be improved.
* The script uses a user agent header to identify the request.
* The script uses the 2022-11-28 version of the github api.
