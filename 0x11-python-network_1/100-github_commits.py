#!/usr/bin/python3
"""ASASDSDFGSDF JSDIFJDS IFJDSFDSF"""

if __name__ == '__main__':
    import requests
    from sys import argv
    req = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = req.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
