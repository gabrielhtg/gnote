#!/bin/bash

cd ~
rm -rf gnote
sed -i '/gnote/d' .bashrc
sed -i '/gnote/d' .zshrc

