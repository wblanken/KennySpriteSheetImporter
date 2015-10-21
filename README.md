# Kenny Sprite Sheet Importer
A simple importer for sprite sheets in
the [Kenny donation collection](http://www.kenney.nl/projects/kga "Kenny Game Assets")
into [Unity](https://unity3d.com/ "Unity3d").

The program was created with Python 3.5 and Pillow 3.0

## Usage
The current iteration is very simple and requires some manual steps to be performed in Unity before running.

1. Import the sprite sheet into Unity
2. Perform an automatic slice of the sprites
3. Save changes
4. Run this application: `python main.py` or if installed as bellow: `Scripts\main.exe`

*Note: if using a virtualenv, activate the environment before running.*

## Installation
**Use of a virtual env is strongly recommended when installing this project**

If you don't wish to use a virtual environment skip to step 5:

1. Install [python 3.x](https://www.python.org/downloads/) and include pip
2. Install virtualenv: `pip install virtualenv`
3. Create the virtual environment: `virtualenv KennySpriteSheetEnv` and cd into the directory.
4. Activate the virtual environment: `Scripts\activate.bat`
5. Install this project: `pip install -e git+https://github.com/wblanken/KennySpriteSheetImporter.git#egg=KennySpriteSheetImporter`
6. Run the project from the Scripts folder: `main.exe`

## Feature Plans
* GUI interface
* Automated import of assets without manual steps in Unity.
* A standalone executable.