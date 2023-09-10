#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers and deploy it
"""
from fabric.api import env, put, run, local
from os.path import exists

env.hosts = ['100.26.11.65', '54.90.23.236']  # Replace with your server IPs
env.user = 'ubuntu'  # Replace with your SSH username


def do_deploy(archive_path):
  if not exists(archive_path):
    return False

  try:
    # Uploads the archive to /tmp/ directory on the server
    put(archive_path, '/tmp/')

    # Get the archive filename without extension
    archive_filename = archive_path.split('/')[-1]
    archive_name = archive_filename.split('.')[0]

    # Create the folder /data/web_static/releases/<archive_name>
    run('mkdir -p /data/web_static/releases/{}/'.format(archive_name))

    # Uncompress the archive into /data/web_static/releases/<archive_name>
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
      archive_filename, archive_name))

    # Remove the uploaded archive from /tmp/
    run('rm /tmp/{}'.format(archive_filename))

    # Delete the current symbolic link if it exists
    run('rm -rf /data/web_static/current')

    # Create a new symbolic link /data/web_static/current linked to the new version
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
      archive_name))
    print("Deployment successful!")
    return True

  except Exception as e:
    return False
