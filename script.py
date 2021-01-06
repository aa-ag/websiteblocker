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
            with open(host, 'r+') as file_:
                content = file_.readlines()
                file_.seek(0)
                for line in content:
                    if not any(site in line for site in to_block):
                        file_.write(line)

                file_.truncate()

            print('Facebook time')
        time.sleep(5)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    block(5, 11)
