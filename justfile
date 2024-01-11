#!/usr/bin/env -S just --justfile
# https://github.com/casey/just
# https://just.systems/man/en/chapter_3.html

# https://just.systems/man/en/chapter_26.html
# set dotenv-load

# logging
log := "warn"
export JUST_LOG := log


# View available options
l:
    just --list --unsorted

# Build docker image
build:
    docker build -t pydev:latest .

# Run docker container
run *opt:
    docker run {{ opt }} -v $(pwd):/usr/src/app pydev

# Show all images and continers
inspect *opt:
    docker images
    docker ps --all

# # BROKEN: Login to the built container
# login:
#     docker exec -it pydev bash

# remove generated data
clean:
    docker images prune
    sudo rm -v ./data/*.xlsx
