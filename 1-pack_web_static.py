#!/usr/bin/python3
""" A python script to archive the html folder """
from fabric.api import *
from datetime import datetime
import os

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
		size = os.path.getsize(result)
		print('web_static packed: {} -> {}Bytes'.format(file_path, size))
		return file_path

