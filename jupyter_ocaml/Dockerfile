FROM jupyterhub/singleuser:1.2 

ENV OPAM_VERSION  2.0.6
ENV OCAML_VERSION 4.10.0
ENV HOME          /home/opam

USER root
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get  install -y sudo patch unzip curl make gcc libx11-dev m4 bubblewrap pkg-config  && \
    adduser --disabled-password --home $HOME --shell /bin/bash --gecos '' opam && \
    \
    echo 'opam ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers && \
    curl -s -L -o /usr/bin/opam "https://github.com/ocaml/opam/releases/download/$OPAM_VERSION/opam-$OPAM_VERSION-$(uname -m)-$(uname -s)" && \
    chmod 755 /usr/bin/opam 
    
RUN su opam -c "opam init -a -y --comp $OCAML_VERSION --disable-sandboxing" && \
    rm $HOME/.profile $HOME/.opam/opam-init/init.* && \
    find $HOME/.opam -regex '.*\\.\\(cmt\\|cmti\\|annot\\|byte\\)' -delete && \
    rm -rf $HOME/.opam/archives \
           $HOME/.opam/repo/default/archives \
           $HOME/.opam/$OCAML_VERSION/build

USER opam
WORKDIR $HOME
#RUN sudo apt-get update && \
#    sudo apt-get upgrade -y && \
#    sudo apt-get install -y zlib1g libgmp10 libzmq5 python3 \
#                            m4 pkg-config gcc zlib1g-dev libgmp-dev libzmq3-dev python3-dev python3-pip && \
#    \
#    sudo pip3 install --upgrade pip && \
#    pip3 install --user --no-cache-dir 'setuptools>=18.5' 'six>=1.9.0' jupyter && \
#    mkdir -p /home/opam/.jupyter && \
#   

RUN sudo apt-get install -y libzmq3-dev zlib1g-dev libgmp-dev zlib1g  libzmq5 libgmp10 && \
    mkdir -p /home/opam/.jupyter && \
    opam install -y 'merlin>=3.0.0' ocaml-migrate-parsetree jupyter 

RUN    eval `opam env` && \
    ocaml-jupyter-opam-genspec && \
    jupyter kernelspec install --user --name ocaml-jupyter "$(opam config var share)/jupyter" && \
    \
    rm -rf $HOME/.opam/archives \
           $HOME/.opam/repo/default/archives \
           $HOME/.opam/$OCAML_VERSION/man \
           $HOME/.opam/$OCAML_VERSION/build && \
    \
    sudo apt-get remove -y m4 pkg-config gcc zlib1g-dev libgmp-dev libzmq3-dev python3-dev python3-pip && \
    sudo apt-get autoremove -y && \
    sudo apt-get autoclean

VOLUME /notebooks
#VOLUME /home/opam/.jupyter
WORKDIR /notebooks

COPY entrypoint.sh /
RUN sudo  chmod +x /entrypoint.sh
COPY .ocamlinit    /home/opam/.ocamlinit
#RUN sudo chown -hR opam:opam /home/opam/.jupyter
#RUN sudo chown -hR opam:opam /notebooks
#COPY .jupyter      /home/opam/.jupyter

#EXPOSE 8888

#ENTRYPOINT ["/opt/conda/bin/tini" "-g" "--"]
#CMD ["echo"]
ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "start-notebook.sh" ]
#CMD [ "jupyter", "notebook", "--no-browser", "--ip=*" ]
