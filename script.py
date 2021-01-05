###--- IMPORTS ---###
import time
from datetime import datetime

###--- GLOBAL VARIABLES ---###

host = '/etc/hosts'

redirect = '127.0.0.1'

to_block = [
    'www.facebook.com',
    'facebook.com'
]

###--- FUNCTION(S) ---###


def block(start_time, end_time):
    global host, redirect, to_block

    while True:
        if datetime(datetime.now().year, datetime.now().month, datetime.now().day, start_time) < datetime.now() < datetime(datetime.now().year, datetime.now().month, datetime.now().day, end_time):
            print("You should be working...")
            with open(host, 'r+') as hostfile:
                hosts = hostfile.read()

                for site in to_block:
                    if site not in hosts:
                        hostfile.write(redirect + ' ' + site + '\n')
        else:
            with open(host, 'r+') as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)

                for host in hosts:
                    if not any(site in host for site in to_block):
                        hostfile.write(host)

                hostfile.truncate()
            print('Nice')
        time.sleep(3)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    block(8, 5)
