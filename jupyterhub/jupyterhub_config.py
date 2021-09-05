# JupyterHub configuration
#
## If you update this file, do not forget to delete the `jupyterhub_data` volume before restarting the jupyterhub service:
##
##     docker volume rm jupyterhub_jupyterhub_data
##
## or, if you changed the COMPOSE_PROJECT_NAME to <name>:
##
##    docker volume rm <name>_jupyterhub_data
##

import os
# Set the log level by value or name.
c.JupyterHub.log_level = 'DEBUG'

# Enable debug-logging of the single-user server
#c.Spawner.debug = True

# Enable debug-logging of the single-user server
#c.LocalProcessSpawner.debug = True

## Generic
c.JupyterHub.admin_access = True
#c.Spawner.default_url = '/lab'

## Authenticator
#c.LocalAuthenticator.create_system_users = True
#c.LocalAuthenticator.add_user_cmd = ['useradd', '-m'] 
#c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
#c.DummyAuthenticator.password = "ChampoForEver"
#from jhub_cas_authenticator.cas_auth import CASAuthenticator
#c.JupyterHub.authenticator_class = CASAuthenticator
#c.JupyterHub.bind_url = 'http://127.0.0.1:800/'
c.JupyterHub.base_url = os.environ['BASE_URL']

c.Authenticator.admin_users = { 'mike' }


## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']

c.DockerSpawner.name_template = "{prefix}-{username}-{imagename}-{servername}"
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-'+os.environ['BASE_URL']+'{username}': notebook_dir }



# Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'

c.JupyterHub.authenticator_class = 'ltiauthenticator.LTIAuthenticator'

c.LTI11Authenticator.consumers = {
os.environ['LTI_CLIENT_KEY']: os.environ['LTI_CLIENT_SECRET']
}      

c.LTI11Authenticator.username_key = "lis_person_name_full"

## Services
#c.JupyterHub.services = [
#    {
#        'name': 'cull_idle',
#        'admin': True,
#        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#    },
#]
