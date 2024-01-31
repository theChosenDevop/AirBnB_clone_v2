#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers, using the
function do_deploy
"""

from fabric.api import env, put, run
import os


env.hosts = ['54.146.82.137', '54.237.106.250']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deplys the static files"""
    if not os.path.exists(archive_path):
        return False

    archive_name = os.path.basename(archive_path)
    archive_no_ext = os.path.splitext(archive_name)[0]

    try:
        put(archive_path, '/tmp/')
        run('sudo mkdir -p /data/web_static/releases/{}/'
            .format(archive_no_ext))
        run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_name, archive_no_ext))
        run('sudo rm /tmp/{}'.format(archive_name))
        run('sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'
            .format(archive_no_ext, archive_no_ext))
        run('sudo rm -rf /data/web_static/releases/{}/web_static'
            .format(archive_no_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_no_ext))
        return True
    except pass:
        return False
