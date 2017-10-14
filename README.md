# 27DaysForms

©2015 Center for Transformative Change, All Rights Reserved

INSTALLATION

You need Anaconda installed, or if you really insist on using python / pip /
etc. you can probably just figure it out. Get the miniconda installer here, and
choose the 3.5 (or later) version:

    https://conda.io/miniconda.html

Then set up the packages needed for my programs (`$` means you type it into a
terminal, where you should see an actual `$` before your cursor):

    $ conda create -n nDC -c mmcauliffe --file conda-packages.txt

Or, if you already have Anaconda set up how you like, you can make a separate
environment:

    $ conda create -n nDC -c mmcauliffe --file conda-packages.txt

You will also need to make a `secrets.ini` file. You can copy
`sample-secrets.ini`, it has hints for how to find the two pieces of
information the script needs!

USAGE

All commands can be run via make. See Makefile for a description of what
different sub-commands will do. The basic, "do everything" command is:

    $ make all

