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

# build docker image
build:
    docker build -t pydev .

# run built docker container
run *opt:
    # docker run {{ opt }} -p 4000:80 -v data:/usr/src/app/data pydev
    docker run {{ opt }} -v $(pwd)/data:/usr/src/app/data pydev

# login to the built container
login:
    docker exec -it pydev bash
