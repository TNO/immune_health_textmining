import indra
import os

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64/"
os.environ["PATH"] = "/usr/lib/jvm/java-8-openjdk-amd64/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# Set path to REACH jar file
os.system('sed -i "s|REACHPATH =|REACHPATH = /reach/target/scala-2.11/reach-1.5.1-SNAPSHOT-FAT.jar |g" /root/.config/indra/config.ini')
os.system('sed -i "s|REACH_VERSION =|REACH_VERSION = 1.5.1 |g" /root/.config/indra/config.ini')

# Set pah to EIDOS jar file
os.system('sed -i "s|EIDOSPATH =|EIDOSPATH = /eidos/target/scala-2.12/eidos-assembly-0.2.2-SNAPSHOT.jar |g" /root/.config/indra/config.ini')

cores = input("How many cores do you want to use?: ")

os.system('snakemake --cores '+str(cores)+' --snakefile /workdir/Snakefile')

exit()