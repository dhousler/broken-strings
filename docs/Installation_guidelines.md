# Nextflow - workflow manager Installation
nextflow version 23.10.0.5889

**Installation:**  
**Install java**
```
sudo apt update
sudo apt install default-jdk
java - version
```
openjdk version "11.0.20.1" 2023-08-24  
**Install curl**
```commandline
sudo apt install curl
```
Install Nextflow
```commandline
mkdir temp
cd temp
curl -s https://get.nextflow.io | bash
sudo cp nextflow /usr/bin
sudo chmod 755 /usr/bin/nextflow
nextflow -version
```

## Docker 
This can be installed following the official documentation:
https://docs.docker.com/engine/install/ubuntu/

## bedtools
https://bedtools.readthedocs.io/en/latest/content/installation.html
```commandline
sudo apt-get install bedtools
```