#!/usr/bin/python3
""" A python script to archive the html folder """
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """pack up all our files into an archive"""
    date = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(date)
    print('Packing web_static to {}'.format(archive_path))
    if os.path.exists(archive_path) is True:
        return True
    local('mkdir versions')
    extract = local('tar -cvzf {} web_static'.format(archive_path))
    if extract.failed:
        return archive_path
    size = os.path.getsize(archive_path)
    print('web_static packed: {} -> {}Bytes'.format(archive_path, size))
