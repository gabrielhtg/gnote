#!/bin/bash

cd ~
mkdir ~/gnote-temp/
mv ~/gnote/list ~/gnote-temp/
rm -rf ~/gnote
git clone https://github.com/gabrielhtg/gnote.git
mv ~/gnote-temp/list ~/gnote
rm -rf ~/gnote-temp


