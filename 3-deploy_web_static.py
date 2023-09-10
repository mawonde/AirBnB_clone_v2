#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers and deploy it
"""
from fabric.api import env, put, run, local
from datetime import datetime
from os.path import exists
import shlex

env.hosts = ['100.26.11.65', '54.90.23.236']  # Replace with your server IPs
env.user = 'ubuntu'  # Replace with your SSH username


def deploy():
  """ Deploys the static website """
  try:
    archive_path = do_pack()
  except:
    return False

  return do_deploy(archive_path)


def do_pack():
  try:
    if not exists("versions"):
      local('mkdir versions')
    t = datetime.now()
    f = "%Y%m%d%H%M%S"
    archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
    local('tar -cvzf {} web_static'.format(archive_path))
    return archive_path
  except:
    return None


def do_deploy(archive_path):
  """ Deploys """
  if not exists(archive_path):
    return False
  try:
    name = archive_path.replace('/', ' ')
    name = shlex.split(name)
    name = name[-1]

    web_name = name.replace('.', ' ')
    web_name = shlex.split(web_name)
    web_name = web_name[0]

    releases_path = "/data/web_static/releases/{}/".format(web_name)
    tmp_path = "/tmp/{}".format(name)

    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(releases_path))
    run("tar -xzf {} -C {}".format(tmp_path, releases_path))
    run("rm {}".format(tmp_path))
    run("mv {}web_static/* {}".format(releases_path, releases_path))
    run("rm -rf {}web_static".format(releases_path))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(releases_path))
    print("New version deployed!")
    return True
  except:
    return False
