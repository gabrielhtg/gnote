#!/bin/bash

chmod +x ~/gnote/uninstall.sh
chmod +x ~/gnote/update.sh
mkdir ~/gnote/list/
echo "alias note=\"python3 ~/gnote/gnote.py\"" >> ~/.bashrc
echo "alias note=\"python3 ~/gnote/gnote.py\"" >> ~/.zshrc
