# reinfCalc

## About the Reinforcement Calculator

Reinforcement Calculator is a desktop application that can be used for dimensioning of simple reinforced concrete elements.
The app is written in Python, PyQt5 and built-in Python libraries.

## App's Tech

 - [Python3] - Main coding language of the application
 - [PyQt5] - Framework used for creating app's GUI
 - [Django] - Web framework used for project's web application 

## Using the calculator

### Installation

In order to work with the application, its source code must be downloaded and dependencies installed.

First, download the source code or copy repository to the desired location.

Next, install all the required modules using: `<path to python script>\python -m pip install -r requirements.txt`

Use of virtual environment for running the script is advised in order to avoid conflicts between modules.
Instructions on creating a virtual environment in Python can be found in [Python docs on venv installation].

Finally, run script `main.py`, to run the application.

### Choosing the element to work with

Once started, a main window of the application shows up letting user choose from 4 types of reinforced concrete elements:
- Plate
- Beam
- Column
- Foundation foot

In order to begin working with a certain element its corresponding button must be clicked.

### Providing necessary data

Next step is to provide all necessary information about the element, which differ depending on the chosen element type.
All fields must be filled bearing in mind units stated in the corresponding labels.

### Using built-in resources

For users' convenience a set of tables containing useful technical parameters has been included in the application.
It can be accessed either by selecting `Resources`->`Included Data` from the menu bar, or using `ctrl+i` keyboard shortcut.

### Running calculations

All the applications are done server-side, in order to obtain the results for the task user has to ensure that following conditions are fulfilled:
- The server is online
- The user has stable internet connection

If so, in order to obtain the simplified results user has to press a `Run calculations` button.

### Generating a report

Users can access the details of a last calculated task via the application pressing a `Generate report` button.

Doing so will open the default web browser and load a report page for the last calculated task.

If the user is not logged in the login page will be displayed first and redirect the user after successful authentication.

### Saving and loading results

At any time of working with the element, users can save their progress using save option by selecting `File`->`Save` from the menu bar,
or using `ctrl+s` keyboard shortcut.
The application uses JavaScript Object Notation to save the information about the user's progress. 

### Dummy data

One of four exemplary files can be loaded to preview form of output data.
The dummy files can be loaded by selecting appropriate file in `File`->`<directory location>/app/demo/<element>_example.rcalc`.

## App features

- [x] Graphical User Interface
- [x] Built-in resources
- [x] Saving and opening files
- [x] Computing engine
- [x] Web application - using Django

   [Python3]: <https://www.python.org/> 
   [Django]: <https://www.djangoproject.com/>
   [PyQt5]: <https://riverbankcomputing.com/software/pyqt/intro> 
   [Web application]: <>
   [Python docs on venv installation]: <https://docs.python.org/3/library/venv.html>