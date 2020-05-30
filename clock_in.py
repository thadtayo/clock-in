'''
Script that allows me to log in my hours easier.
py clock_in.py --start -s to start
py clock_in.py --stop -p to stop
py clock_in.py -m "Message here."
'''
import click
import datetime
from datetime import date

@click.command()
@click.option('--start', '-s', is_flag=True)
@click.option('--stop', '-p', is_flag=True)
@click.option('--message', '-m', type=str)
def clock(start, stop, message):
    f = open('timesheet.txt', 'a')
    if start:

        now =  datetime.datetime.now()
        m = open('metadata.txt', 'r+')
        last_time = m.read()
        if last_time != '':
            print('Already ran start.')
            exit()
        f.write('START: ' + str(now) + '\n')
        m.write(str(now))
    
    if stop:
        now = datetime.datetime.now()
        m = open('metadata.txt', 'r+')
        last_time = m.read()
        if last_time == '':
            print('Run start first.')
            exit()
        f.write('STOP: ' + str(now) + '\n')
        
        last_time = datetime.datetime.strptime(last_time, '%Y-%m-%d %H:%M:%S.%f')
        delta_time = now - last_time
        f.write('TIME WORKED: ' + str(delta_time) + '\n')

        m.truncate(0)

    
    if message:
        f.write(message + '\n')



if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    clock()