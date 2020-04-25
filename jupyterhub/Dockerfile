FROM jupyterhub/jupyterhub:1.2

COPY jupyterhub_config.py .

#RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/1.1.0/examples/cull-idle/cull_idle_servers.py

RUN pip install \
    dockerspawner==0.11.1 \
    oauthlib==3.1.0\
    jupyterhub-ltiauthenticator\
    jupyterhub-dummyauthenticator
    #jhub_cas_authenticator==1.0.0
