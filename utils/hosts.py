#!/usr/bin/python3

from datetime import datetime
from time import sleep

# SELECT INTERVAL OF THE DAY TO BLOCK
START = 10
FINISH = 12

# interval of the current day to block
start_time = datetime(datetime.now().year,
                      datetime.now().month,
                      datetime.now().day, START)
finish_time = datetime(datetime.now().year,
                       datetime.now().month,
                       datetime.now().day, FINISH)

REDIRECT = '127.0.0.1'
HOSTS = '/etc/hosts'

# INSERT SITES TO BLCOK
forbidden_sites = ['pornhub.com', 'twitter.com']

while True:

    with open(HOSTS, 'r+', encoding='utf-8') as file:
        """
        IF TIME IN FORBIDDEN INTERVAL GO THROUGH FORBODDEN SITES,
        IF SITE NOT IN HOSTS -> ADD IT
        IF SITE IN HOSTS - > DO NOTHING
        ---
        IF TIME NOT IN FORBIDDEN INTERVAL GO THROUGH LIST OF HOSTS's LINES,
        IF SOME FORBIDDEN SITE IN LINE -> DO NOTHING
        IF SOME FORBIDDEN SITE NOT IN LINE -> ADD INITIAL CONTENT WITHOUT FORBIDDEN SITES
        IN FRONT OF HOSTS AND TRUNCATE ALL BEFORE THE COURSOR
        """
        if start_time < datetime.now() < finish_time:
            content = file.read()
            for site in forbidden_sites:
                if site not in content:
                    file.write(f'{REDIRECT}\t{site}\n')

        else:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in forbidden_sites):
                    file.write(line)
            file.truncate()

    sleep(5)
