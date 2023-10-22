# Useful docker commands

## Build the docker image
+ make sure to change the version

docker build breaks:1.0.0 .

## Run a container for manual testing and remove it
docker run -it --rm breaks:1.0.0 /bin/bash

## Attach to a volume
docker run -it --rm /local/path/file-location:/location/in/container breaks:1.0.0 /bin/bash
