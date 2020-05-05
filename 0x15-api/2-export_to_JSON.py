#!/usr/bin/python3
"""Export data from an API to JSON format.
"""
from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    # Checks if the argument can be converted to a number
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    # Main formatted names to API uris and filenames
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.json'.format(emp_id=emp_id)

    # User Response
    u_res = requests.get(user_uri).json()

    # User TODO Response
    t_res = requests.get(todo_uri).json()

    # A list of all tasks of an user
    user_tasks = list()

    for elem in t_res:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': u_res.get('username')
        }

        user_tasks.append(data)

    # Create the new file for the user to save the information
    # Filename example: `{user_id}.json`
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({emp_id: user_tasks}))
