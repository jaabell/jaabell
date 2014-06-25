#!/bin/bash
. $HOME/.virtualenv/pelican/bin/activate
make html
make serve