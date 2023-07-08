#!/usr/bin/python3
""" A python script to archive the html folder """
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """pack up all our files into an archive"""
    date = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    archive_path = 'web_static_{}.tgz'.format(date)
    print('Packing web_static to versions/{}'.format(archive_path))
    if not os.path.exists('versions'):
        local('mkdir versions')

    extract = local('tar -cvzf versions/{} web_static/'.format(archive_path))
    if extract.succeeded:
        path = 'versions/{}'.format(archive_path)
        size = os.path.getsize('versions/{}'.format(archive_path))
        print('web_static packed: {} -> {}Bytes'.format(archive_path, size))
        return path
    else:
        return None
