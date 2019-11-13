import os

# os.system('docker build -t indra-docker-test .')
os.system('docker run -v $(pwd):/workdir -ti --rm indra-docker-test')
