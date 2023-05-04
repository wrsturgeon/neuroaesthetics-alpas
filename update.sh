#!/bin/sh

set -eux

git pull
git submodule update --init --remote --recursive
