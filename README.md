Todo-list project built with DJango using function based views

Environment Setup $ git clone https://github.com/panosker/todo_function.git

$ cd Todo_list

If virtualenv is not installed :

$ python -m venv venv

Create a virtual environment

$ virtualenv venv

Activate the environment everytime you open the project

Windows venv activation: # In cmd.exe venv\Scripts\activate.bat # In PowerShell venv\Scripts\Activate.ps1

Linux and MacOS venv activation: $ source venv/bin/activate

$ ls ( make sure that you are in the same folder with the manage.py)

$ python3 manage.py runserver
