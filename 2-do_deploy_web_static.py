#!/usr/bin/python3
'''module:
deploy a web static archive to web servers
'''

from fabric.api import env, put, run
from os.path import exists, isfile
import os
import argparse

env.hosts = ['100.26.133.155', '35.175.63.49']


def do_deploy(archive_path):
<<<<<<< HEAD
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
=======
    '''function:
    distributes an archive to your web servers
    '''

    if not exists(archive_path) and not isfile(archive_path):
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('archive_path', type=str,
                        help='path to the archive file')
    parser.add_argument('-u', '--username', type=str,
                        help='SSH username')
    parser.add_argument('-i', '--private-key', type=str,
                        help='Path to SSH private key')
    args = parser.parse_args()

    if args.username:
        env.user = args.username

    if args.private_key:
        env.key_filename = args.private_key

    do_deploy(args.archive_path)
>>>>>>> e021049e37e948864c4886c0eb955e3699b59f76
