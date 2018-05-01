#!/bin/bash

rm -rf  build
rm -rf  ekphrasis.egg-info
rm -rf  dist

python setup.py sdist bdist_wheel

pip install --no-cache-dir --no-index --find-links=dist/ekphrasis-0.4.9.tar.gz ekphrasis --force-reinstall --no-deps -U
