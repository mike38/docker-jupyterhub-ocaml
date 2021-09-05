FROM jupyterhub/jupyterhub:main

COPY jupyterhub_config.py .

#RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/1.1.0/examples/cull-idle/cull_idle_servers.py

#RUN pip install --upgrade pip

RUN pip install \
    dockerspawner \
    oauthlib \
    jupyterhub-ltiauthenticator\
    jupyterhub-dummyauthenticator
    #jhub_cas_authenticator==1.0.0
    #dockerspawner==0.11.1 \
    #oauthlib==3.1.0\
