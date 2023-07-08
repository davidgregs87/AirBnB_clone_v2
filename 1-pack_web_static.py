#!/usr/bin/python3
""" A python script to archive the html folder """
from fabric.api import *
from datetime import datetime
import os

def do_pack():
	"""pack up all our files into an archive"""
	date = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
	file_path = 'versions/web_static_{}.tgz'.format(date)
	print('Packing web_static to {}'.format(file_path))
	if not os.path.exists('versions'):
                local('mkdir versions')
	
	extract = local('tar -cvzf {} web_static/'.format(file_path))
	if extract.succeeded:
		size = os.path.getsize(file_path)
		print('web_static packed: {} -> {}Bytes'.format(file_path, size))
		return file_path
	else:
		return None 
