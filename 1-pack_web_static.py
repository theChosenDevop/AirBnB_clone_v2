#!/usr/bin/python3
"""
This module generates a .tgz archive from the contents of the web_static AirBnB
Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Packs web_static files into .tgz archive"""
    try:
        current_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None
