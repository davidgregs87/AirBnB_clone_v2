#!/usr/bin/python3
"""
A fabric scipt that generates a .tgz archive file from my web_static folder
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['100.26.133.155', '35.175.63.49']


def do_deploy(archive_path):
    """ Deploy archives """
    if os.path.isfile(archive_path):
        # upload the archive to the /tmp/ directory of the webserver
        put(archive_path, '/tmp/')
    else:
        return False
    # get the name of the file with .tgz
    file_name = archive_path.split('/')[-1]
    # get name without .tgz
    xfile_name = file_name.split('.')[0]
    file_path = '/data/web_static/releases/' + xfile_name
    # create archive folder
    if run('mkdir -p {}'.format(file_path)):
        return True
    False    # uncompress the archive to the folder file_name
    if run('tar -xzf /tmp/{} -C {}'.format(file_name, file_path)):
        return True
    False
    # delete the uploaded archive
    if run('rm /tmp/{}'.format(file_name)):
        return True
    False
    # move files
    if run('mv {}/web_static/* {}'.format(file_path, file_path)):
        return True
    False
    # delete folder
    if run('rm -rf {}/web_static/'.format(file_path)):
        return True
    False
    # delete symbolic link from webserver
    if run('rm -rf /data/web_static/current'):
        return True
    False
    # create sym link
    if run('ln -s {} /data/web_static/current'.format(file_path)):
        return True
    False
    print('New version deployed!')
