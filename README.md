# Academic Calendars for Northeastern University
Website showing the academic calendars for Northeastern University.

## Objective
The objective of this project is to convert the academic calendar pdfs provided by Northeastern University to a website with navigation for each pdf.

## Tools used
The project uses Python 3.8 and the dependencies are provided as a Pipfile for pipenv. The project was created using the PyCharm IDE on a Mac.

### Installation
- ghostscript
  - before creating the project, install ghostscript
  - Open Terminal and run `brew install tcl-tk ghostscript`
  - [Ghostscript Installation](https://camelot-py.readthedocs.io/en/master/user/install-deps.html)

### Dependencies listed in pipfile
- flask
- camelot (extract tables from pdfs)
  - run `pipenv install "camelot-py[cv]"` in PyCharm Terminal to install camelot
  - [Camelot Installation](https://camelot-py.readthedocs.io/en/master/user/install.html#install)
  - Using PyCharm Preferences, Project Interpreter to install camelot can cause *ModuleNotFoundError: No module named 'cv2'* error when running a python file with `import camelot`
    - if this happens, run `pipenv uninstall --all`
    - install Flask from the Preferences window
    - install camelot with above command for camelot

## Research
### How to license a repository
[How to license a repository (GitHub)](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository)

[Choose A License (recommended by GitHub)](https://choosealicense.com/)

### How to extract a calendar spanning 3 semesters from a pdf url
[Academic Calendar Used](https://registrar.northeastern.edu/app/uploads/2020-2021-GR-Expanded-Calendar-List.pdf)
#### Extract tables from PDFs
[Compare Camelot with other Table Extraction Tools](https://github.com/atlanhq/camelot/wiki/Comparison-with-other-PDF-Table-Extraction-libraries-and-tools)

### How to get a list of pdf urls for all academic calendars for Northeastern University
[Academic Calendar Home Page](https://registrar.northeastern.edu/group/calendar/)

