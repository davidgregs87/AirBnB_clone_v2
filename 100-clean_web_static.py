#!/usr/bin/python3
"""A script that deletes out of date archives"""
from fabric.api import *

env.hosts = ['100.26.133.155', '35.175.63.49']



def do_clean(number=0):
    '''function:
    deletes out-of-date archives
    '''

    number = int(number)
    if number < 0:
        return False
    elif number == 0 or number == 1:
        number_to_keep = 1
    else:
        number_to_keep = number

    # delete unnecessary archives in the versions folder
    with lcd('versions'):
        local('ls -lt | tail -n +{} | xargs rm -rf'.format(number_to_keep + 1))

    # delete unnecessary archives in the /data/web_static/releases folder
    with cd('/data/web_static/releases'):
        run('ls -lt | tail -n +{} | xargs rm -rf'.format(number_to_keep + 1))
