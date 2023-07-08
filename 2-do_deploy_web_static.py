#!/usr/bin/python3
"""
A fabric scipt that generates a .tgz archive file from my web_static folder
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['100.26.133.155', '35.175.63.49']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Deploy archives """
    if os.path.exists(archive_path):
        # upload the archive to the /tmp/ directory of the webserver
        put(archive_path, '/tmp/')
        # get the name of the file with .tgz
        file_name = archive_path.split('/')[-1]
        # get name without .tgz
        xfile_name = file_name.split('.')[0]
        file_path = '/data/web_static/releases/' + xfile_name
        # create archive folder
        run('mkdir -p {}'.format(file_path))
        # uncompress the archive to the folder file_name
        run('tar -xzf /tmp/{} -C {}'.format(file_name, file_path))
        # delete the uploaded archive
        run('rm /tmp/{}'.format(file_name))
        # move files
        run('mv {}/web_static/* {}'.format(file_path, file_path))
        # delete folder
        run('rm -rf {}/web_static/'.format(file_path))
        # delete symbolic link from webserver
        run('rm -rf /data/web_static/current')
        # create sym link
        run('ln -s {} /data/web_static/current'.format(file_path))
        print('New version deployed!')
        return True
    else:
        return False
