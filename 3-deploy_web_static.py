#!/usr/bin/python3
""" A python script to archive the html folder """
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['100.26.133.155', '35.175.63.49']


def do_pack():
    """pack up all our files into an archive"""
    if os.path.exists('versions'):
        pass
    else:
        local('mkdir versions')
    date = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    file_path = 'versions/web_static_{}.tgz'.format(date)
    print('Packing web_static to {}'.format(file_path))
    result = local('tar -cvzf {} web_static/'.format(file_path))
    if result.failed:
        return None
    else:
        size = os.path.getsize(file_path)
        print('web_static packed: {} -> {}Bytes'.format(file_path, size))
        return file_path



def do_deploy(archive_path):
    '''function:
    distributes an archive to your web servers
    '''

    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        no_ext = os.path.splitext(archive_filename)[0]

        # upload the archive to the /tmp/ directory of the web server:
        put(archive_path, '/tmp/')

        # unarchive - uncompress the archive to the folder:
        release_folder = '/data/web_static/releases/' + no_ext + '/'
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        # delete the archive from the web server
        # move files to proper locations:
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}web_static/* {}'.format(release_folder, release_folder))

        run('rm -f /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_folder))

        print('New version deployed!')
        return True

    except Exception:
        return False


def deploy():
    """A script that creates and distributes an archive to your web servers, using the function deploy:"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
