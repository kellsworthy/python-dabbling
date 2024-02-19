# python-dabbling

### An experimental repository for dabbling in Python. Created to learn Python for data science _and_ Python for app development.
  

## *notes-for-myself*

See [this link](https://www.markdownguide.org/basic-syntax/) for a markdown guide.  
See [this link](https://www.jcchouinard.com/gitignore-template/) for a template to have GitHub ignore specific files/repositiories.

When saving changes to GitHub...

1. Ensure any files/projects/repositories you do not want to commit to GitHub have a *gitignore* file.
2. Save all changes.
3. Stage changes for any files you want to commit.
4. Add a commit comment to provide context for the commit and then click the commit button.
5. Push the commit to GitHub.

## *understanding-poetry*
  
See [this link](https://hackersandslackers.com/python-poetry-package-manager/) for a rundown of how to use Poetry and [this link](https://realpython.com/dependency-management-python-poetry/) for further explanations of its dependency management features. 

When starting a **new** Python project...

1. Use `poetry new --src [name]` in the **project's** integrated terminal to create a src project folder structure (remove the `--src` to create a flat project folder structure instead). It will look like the following:

> projname *(project folder)*  
> ├─ pyproject.toml *(Poetry file)*  
> ├─ README.md *(markdown file)*  
> ├─ src *(import subfolder)*  
> &nbsp;│ &nbsp; &nbsp; &nbsp; └── projname  
> &nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; └── _ _init _ _.py  
> └─ tests *(testing subfolder)*  
> &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; └── _ _init _ _.py  

2. Remove any unnecessary files/folders.
    - The Poetry file, *pyproject.toml*, is critical. It contains the project's metadata, defines dependencies and version requirements, xxx
    - The *README.md* file is a typical markdown file used to provide a description/further context to a project.
    - The package subfolder contains the *_ _ init _ _.py* file that tells Python to treat this project as a package (therefore allowing importing).
    - The testing subfolder contains an initial test file, *test_projname.py*, that already runs a test against your project to make sure its importable.

3. Use `poetry run which python3` in the **project's** integrated terminal to verify the project is using a virtual environment.
    - If created manually with Visual Studio Code, the file path will include *.venv*.
    - If created by Poetry, the file path will include *.virtualenvs*.

4. Use `poetry add [package]` to install packages to the project's virtual environment and write dependencies to the *poetry.lock* file.

5. Ensure that VS Code is using the correct interpreter.
    - Use `poetry env info --path` in the **project's** integrated terminal to find the virtual environment path.
    - In VSCode, use the **Python: Select Interpreter** command, then copy/paste the path in the **Enter interpreter path...** option.

When continuing a **current** Python project...

1. Always ensure the parent project contains a *pyproject.toml* file.

2. Use `poetry run which python3` in the **project's** integrated terminal to verify the project is using a virtual environment.
    - If created manually with Visual Studio Code, the file path will include *.venv*.
    - If created by Poetry, the file path will include *.virtualenvs*.
