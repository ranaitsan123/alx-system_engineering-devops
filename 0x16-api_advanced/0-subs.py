#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers for the subreddit. Returns 0 if the subreddit is invalid.
    """
    # Reddit API URL for the subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid issues with the API
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Invalid subreddit or other error, return 0
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print(f"{subreddit_name} has {subscribers_count} subscribers.")
