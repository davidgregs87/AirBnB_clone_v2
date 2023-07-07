#!usr/bin/python3
""" A python script to archive the html folder """
from fabric.api import *
from datetime import datetime
import os

def do_pack():
	"""pack up all our files into an archive"""
	if not os.path.exists('versions'):
		local('mkdir versions')
	date = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
	result = local('tar -cvzf versions/web_static_{}.tgz web_static/'.format(date))
	path = 'versions/web_static_{}.tgz'.format(date)
	if result.failed:
		return None
	else:
		return path

