#!/bin/bash

chmod +x ~/gnote/gnote
chmod +x ~/gnote/uninstall.sh
chmod +x ~/gnote/update.sh
mkdir ~/gnote/list/
echo "alias note=\"~/gnote/gnote\"" >> ~/.bashrc
echo "alias note=\"~/gnote/gnote\"" >> ~/.zshrc
