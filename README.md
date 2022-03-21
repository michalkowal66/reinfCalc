# reinfCalc

## About the Reinforcement Calculator

Reinforcement Calculator is a desktop application that can be used for dimensioning of simple reinforced concrete elements.
The app is written in Python, PyQt5 and built-in Python libraries.
The application is still in development, current and upcoming functionalities can be viewed in further sections.

## App's Tech
1. Current
    - [Python3] - Main coding language of the application
    - [PyQt5] - Framework used for creating app's GUI
2. Planned
    - *[Django] - Web framework planned to be used for application interface* 

## Using the calculator
  
After installing all required modules listed in `requirements.txt` file and downloading the current code, the application 
can be started by running `main.py` script. 

### Choosing the element to work with

Once started, a main window of the application shows up letting user to choose from 4 types of reinforced concrete elements:
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

### *Running calculations*

*This function is currently unavailable.*

### *Generating a report*

*This function is currently unavailable.*

### Saving and loading results

At any time of working with the element, users can save their progress using save option by selecting `File`->`Save` from the menu bar,
or using `ctrl+s` keyboard shortcut.
The application uses JavaScript Object Notation to save the information about the user's progress. 

### Dummy data

In the current development stage of the application does not allow performing any calculations. 
However, one of four exemplary files can be loaded to preview planned form of output data.
The dummy files can be loaded by selecting appropriate file in `File`->`<element>_example.rcalc`.

## App features - current and planned

- [x] Graphical User Interface
- [x] Built-in resources
- [x] Saving and opening files
- [ ] [Planned] Computing engine
- [ ] [Planned] Application interface - using Django

   [Python3]: <https://www.python.org/> 
   [Django]: <https://www.djangoproject.com/>
   [PyQt5]: <https://riverbankcomputing.com/software/pyqt/intro> 