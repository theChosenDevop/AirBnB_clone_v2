#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers,
using the function deploy
"""

from fabric.api import env, local, run
from os.path import exists
from datetime import datetime


env.hosts = ['54.146.82.137', '54.237.106.250']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Packs web_static files into .tgz archive"""
    try:
        current_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except pass:
        return None


def do_deploy(archive_path):
    """Deploys the web static"""
    if not exists(archive_path):
        return False

    archive_name = archive_path.split("/")[-1]
    archive_no_ext = archive_name.split(".")[0]

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
    except Exception:
        return False


def deploy():
    """Packs the web static files then deploys them"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
