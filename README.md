install GIT for your OS using the guide:

`https://www.atlassian.com/git/tutorials/install-git`

clone the git repository

`git clone https://gitlab.spd-ukraine.com/rnd-ml/duplicate-finder.git`

install python for your OS using the guide:

`https://realpython.com/installing-python/`

install library for virtual environments creation:

`pip install virtualenv`

go to the directory with repository

**FOR LINUX AND MACOS**
cd path/to/repository

**FOR WINDOWS**

cd path\to\repository

next you have to create virtual environment and install in it all required libraries

**FOR LINUX AND MACOS**

executing next command in terminal will create virtual environment with name 'venv':

`python3 -m venv path_to_venv/venv`

activate virtual environment with next command in terminal:

`source path_to_venv/venv/bin/activate`

install requirements from file _requirements.txt_ to virtual environment with next command in terminal:

`pip install -r requirements.txt`


**FOR WINDOWS**

executing next command in terminal will create virtual environment with name 'venv' 

`c:\>c:\path\to\installed\python -m venv c:\path\to\venv`

activate virtual environment with next command in terminal:

`source c:\path\to\venv\venv\bin\activate`

install requirements from file _requirements.txt_ to virtual environment with next command in terminal:

`pip install -r requirements.txt`


