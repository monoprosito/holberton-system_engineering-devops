#!/usr/bin/python3
"""Queries the Reddit API and
prints the titles of the first
10 hot posts listed for a given
subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first
    10 hot posts listed for a given
    subreddit.
    """
    # Set the Default URL strings
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)

    # Set an User-Agent
    user_agent = {'User-Agent': 'Python/requests'}

    # Set the Query Strings to Request
    payload = {'limit': '10'}

    # Get the Response of the Reddit API
    res = requests.get(api_uri, headers=user_agent,
                       params=payload, allow_redirects=False)

    # Checks if the subreddit is invalid
    if res.status_code in [302, 404]:
        print('None')
    else:
        res_json = res.json()

        if res_json.get('data') and res_json.get('data').get('children'):
            # Get the 10 hot posts of the subreddit
            hot_posts = res_json.get('data').get('children')

            # Print each hot post title
            for post in hot_posts:
                if post.get('data') and post.get('data').get('title'):
                    print(post.get('data').get('title'))
