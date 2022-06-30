# GNOTE
         ________  ___     __  ________  ________  _______
        / ______/ /   |   / / / ____  / /__  ___/ / _____/
       / /____   / /| |  / / / /   / /    / /    / /____
      / //__ /  / / | | / / / /   / /    / /    / _____/
     / /__/ /  / /  | |/ / / /___/ /    / /    / /_____
    /______/  /_/   |___/ /_______/    /_/    /_______/

This is a program that works to create notes while using the terminal. 

## Features

- Add new note or edit a note
- See the contents of the note
- Removing note
- Show all notes
- Copy a note content
  
## Installation

Before installing this program, you must have some dependencies. In this case, I'm using Arch Linux.
1. Open your terminal.
2. Install pyperclip
   ```
   pip install pyperclip
   ```
3. Update your database.
   ```
    sudo pacman -Syy
   ```
4. Install xclip.
   ```
    sudo pacman -S xclip
   ```
5. Install nano. Usually already installed by default in Arch.
   ```
    sudo pacman -S nano
   ```
6. Install git.
   ```
    sudo pacman -S git
   ```
7. Go to your home directory.
   ```
    cd ~
   ```
8. Clone this repository or download archive file from package section, extract that file in home directory.
   ```
    git clone https://github.com/gabrielhtg/gnote.git
   ```
9. Go to gnote directory.
   ```
    cd gnote
   ```
10. Change install.sh permission.
    ```
    chmod +x install.sh
    ```
11. Run install.sh file.
    ```
    ./install.sh
    ```
12. Re-open your terminal.
13. Type `note version`
14. The output should be `GNOTE v.1.2`
    
## How to use

1. Open your terminal.
2. To add or edit a note.
   ```
   note add [note_name]
   ```
3. To see the contents of a note.
   ```
   note view [note_name]
   ```
4. To delete Note.
   ```
   note remove [note_name]
   ```
5. To show all the notes available.
   ```
   note list
   ```
6. To copy the contents of a note.
   ```
   note copy [note_name]
   ```

## Uninstalling

1. Go to gnote directory.
   ```
   cd ~/gnote/
   ```
2. Change install.sh permission.
    ```
    chmod +x uninstall.sh
    ```
3. Run uninstall.sh
   ```
   ./uninstall.sh
   ```

## <b>About Me</b>

I'm a student at Del Institute of Technology. <br>
Bachelor of Informatics study program. <br>


<button><a href="https://www.instagram.com/gabrielhtg77/">My Instagram</a></button>
<br>
<button><a href="https://www.del.ac.id/">Institut Teknologi Del</a></button>
