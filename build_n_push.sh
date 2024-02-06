#!/bin/bash
docker buildx build --push -t username/imagename:tag . --platform linux/amd64
