#!/usr/bin/python3
"""Export data from an API to JSON format.
"""
from json import dumps
import requests


def get_tasks_from_employee(response, employee):
    """Get all the tasks of an employee
    """
    # Creates a list to stores all the tasks of the employee
    employee_tasks = list()

    # Find the tasks that belongs to this employee
    for task in response:
        if task.get('userId') == employee.get('id'):
            task_data = {
                'username': employee.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed'),
            }

            employee_tasks.append(task_data)

    # Returns the list of tasks
    return employee_tasks


if __name__ == '__main__':
    # Main formatted names to API uris and filenames
    api_url = 'https://jsonplaceholder.typicode.com'
    users_uri = '{api}/users'.format(api=api_url)
    todos_uri = '{api}/todos'.format(api=api_url)
    filename = 'todo_all_employees.json'

    # Users Response
    u_res = requests.get(users_uri).json()

    # Users TODO Response
    t_res = requests.get(todos_uri).json()

    users_tasks = dict()

    # Stores all the tasks of each employee in the API data
    for user in u_res:
        user_id = user.get('id')

        # A list of all tasks of current employee
        user_tasks = get_tasks_from_employee(t_res, {
            'id': user_id,
            'username': user.get('username')
        })

        # Inserting the list of all tasks of current employee
        # to a dictionary that stores all the employees with their tasks.
        users_tasks[user_id] = user_tasks

    # Create the new file with all the information
    # Filename example: `todo_all_employees.json`
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps(users_tasks))
