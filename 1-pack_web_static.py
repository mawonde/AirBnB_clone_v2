#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the web_static """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(path))
        return path
    except:
        return None
