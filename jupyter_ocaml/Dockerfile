FROM jupyter/scipy-notebook:latest

ENV OPAM_VERSION  2.1.0
ENV OCAML_VERSION 4.12.0
ENV HOME          /home/opam

USER root
RUN apt-get update && \
    apt-get upgrade -y && \
    echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
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

RUN sudo apt-get install -y libzmq3-dev zlib1g-dev libgmp-dev zlib1g  libzmq5 libgmp10 libcairo2-dev && \
    sudo apt-get install -y  texlive-xetex texlive-fonts-recommended texlive-plain-generic pandoc && \
    mkdir -p /home/opam/.jupyter && \
    opam install -y 'merlin>=3.0.0' ocaml-migrate-parsetree jupyter && \
    opam install -y archimedes jupyter-archimedes graphics 

RUN    eval `opam env` && \
    ocaml-jupyter-opam-genspec && \
    jupyter kernelspec install --user --name ocaml-jupyter "$(opam config var share)/jupyter" && \
    \
    rm -rf $HOME/.opam/archives \
           $HOME/.opam/repo/default/archives \
           $HOME/.opam/$OCAML_VERSION/man \
           $HOME/.opam/$OCAML_VERSION/build 

USER root
WORKDIR /tmp

RUN apt-get install -y git 
RUN git clone https://github.com/XaverKlemenschits/jupyter-c-kernel.git

#COPY ./ jupyter_c_kernel/

RUN pip install --no-cache-dir -e jupyter-c-kernel/ > piplog.txt
RUN cd jupyter-c-kernel && install_c_kernel --user > installlog.txt


USER opam

RUN pip install  ipython-sql

RUN  sudo apt-get remove -y m4 pkg-config zlib1g-dev libgmp-dev libzmq3-dev python3-dev python3-pip && \
    sudo apt-get autoremove -y && \
    sudo apt-get autoclean



VOLUME /notebooks
#VOLUME /home/opam/.jupyter
WORKDIR /notebooks

COPY entrypoint.sh /
RUN sudo  chmod +x /entrypoint.sh
COPY .ocamlinit    /home/opam/.ocamlinit

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "start-notebook.sh" ]
#CMD [ "jupyter", "notebook", "--no-browser", "--ip=*" ]
