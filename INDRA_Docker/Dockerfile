### docker build --no-cache=true -t indra-docker-prod .
### docker run -v $(pwd):/workdir -ti --rm indra_docker snakemake --snakefile /workdir/Snakefile
### docker run -v $(pwd):/workdir -ti --rm indra_docker python workdir/scripts/import_indra.py
### python Start_INDRA.py

FROM continuumio/miniconda3

MAINTAINER remon.dulos@tno.nl

# Update Conda
RUN conda update conda

# Upgrade pip version
RUN conda install -c anaconda pip

# Install Snakemake
RUN conda install -c bioconda snakemake

# Install NLTK (Text mining package)
RUN conda install -c anaconda nltk

# Install Cython
RUN conda install -c anaconda cython

# Install indra from Github
RUN git clone https://github.com/sorgerlab/indra.git && cd indra && pip install --ignore-installed .

# Remove enum34 (Since python 3.6 the enum34 library is no longer compatible with the standard library.)
RUN pip uninstall -y enum34

# Instal Jnius
# RUN conda install -c conda-forge pyjnius=1.1.3
RUN conda install -c conda-forge pyjnius

# Install matplotlib
RUN conda install -c conda-forge matplotlib 

# Install additional dependencies
# RUN pip install indra[biopax]
RUN pip install indra[be]
RUN pip install indra[trips_offline]
RUN pip install indra[reach_offline]
RUN pip install indra[eidos_offline]
RUN pip install indra[geneways]
RUN pip install indra[sbml]

# Install GNU
RUN apt-get update && apt-get install -y gnupg

# Install method driver for HTTPS
RUN apt-get install apt-transport-https

RUN apt-get install nano

RUN git clone https://github.com/clulab/reach.git

RUN conda install -c bioconda sbt

RUN echo "mainClass in assembly := Some(\"org.clulab.reach.ReachCLI\")" >> reach/build.sbt

RUN cd reach/ sbt -Dsbt.ivy.home=/pmc/reach/.ivy2 compile compile && sbt -Dsbt.ivy.home=/pmc/reach/.ivy2 assembly

RUN conda install -c anaconda maven

# Install CoreNLP from Stanford NLP
RUN git clone https://github.com/stanfordnlp/CoreNLP.git && cd CoreNLP/ && mvn package

#TODO: add /CoreNLP/target/ to $CLASSPATH
RUN mkdir -p /lib/classes
ENV CLASSPATH /lib/classes:/CoreNLP/target/

RUN apt-get install nano

# Remove enum34 (Since python 3.6 the enum34 library is no longer compatible with the standard library.)
RUN pip uninstall -y enum34

# Install JAVA 8
RUN apt-get update && apt-get install -y openjdk-8-jdk

# add reach jar to /root/.config/indra/config.ini
# NOTE TO SELF: CHECK VERSION OF JAR FILE !
# NOTE 2: ALSO IN workdir/scripts/import_indra.py
RUN sed -i "s|REACHPATH =|REACHPATH = /reach/target/scala-2.11/reach-1.5.1-SNAPSHOT-FAT.jar |g" /indra/indra/resources/default_config.ini
RUN sed -i "s|REACH_VERSION =|REACH_VERSION = 1.5.1 |g" /indra/indra/resources/default_config.ini

RUN conda install -c conda-forge pyjnius=1.1.3

# # Install EIDOS
RUN git clone https://github.com/clulab/eidos.git
WORKDIR /eidos
RUN sbt assembly
WORKDIR /

# # add EIDOS jar to /root/.config/indra/config.ini
# # NOTE 2: ALSO IN workdir/scripts/import_indra.py
RUN sed -i "s|EIDOSPATH =|EIDOSPATH = /eidos/target/scala-2.12/eidos-assembly-0.2.2-SNAPSHOT.jar |g" /indra/indra/resources/default_config.ini

ENV CLASSPATH=/eidos/target/scala-2.12/eidos-assembly-0.2.2-SNAPSHOT.jar:${CLASSPATH}
ENV CLASSPATH=/reach/target/scala-2.11/reach-1.5.1-SNAPSHOT-FAT.jar:${CLASSPATH}

# # RUN echo blabla
# RUN mkdir -p /eidos/src/main/resources/org/clulab/wm/eidos/w2v/
# COPY workdir/EIDOS/vectors.txt /eidos/src/main/resources/org/clulab/wm/eidos/w2v/vectors.txt
# RUN sed -i "s|useW2V = false|useW2V = true |g" /eidos/src/main/resources/eidos.conf

RUN conda uninstall numpy
RUN conda install -c conda-forge numpy

# Install Snakemake
RUN conda install -c bioconda snakemake

ENTRYPOINT ["python","workdir/scripts/import_indra.py"]
