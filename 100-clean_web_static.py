#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives, using the function do_clean
"""

from fabric.api import env, run, local
from os.path import exists
from datetime import datetime


env.hosts = ['54.146.82.137', '54.237.106.250']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1
    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs rm -f --'.format(number + 1))
    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf --'.format(number + 1))
