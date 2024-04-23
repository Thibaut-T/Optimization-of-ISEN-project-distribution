# Optimization of the ISEN Distribution Project

This project focuses on optimizing the ISEN (Institut Supérieur de l'Électronique et du Numérique) distribution system. It involves data scraping from an .xlsx file using Python, generating .txt and .lp files, and includes an application to create a PDF containing project details.

## Overview

The project comprises several components:

1. **Project creation:** Fill in all the projects to generate an xml to initialize a moodle and a pdf to send to the students.

2. **Solver:** From the responses of the students create an lp model and solve it.

3. **Corrections and final decision:** From the solver's solution generate allow the user to do some minor correction and xlsx file with all the result.

## Tools and Technologies

- **Python:** Used extensively for data scraping, file handling, and application development.
- **Libraries and Modules:** Potentially employed libraries such as `pandas` for data manipulation, `openpyxl` for handling .xlsx files, and `reportlab` for PDF generation, `customtkinter` and `tkinter` for the graphic part, `pulp` for linear programming and `pyinstaller` for executable generation.
- **Optimization Algorithms:** Algorithms might be integrated into the .lp file generation, depending on project requirements.

## How to Use

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/ISEN-distribution-optimization.git
    cd ISEN-distribution-optimization
    ```

2. **Setup:**
    - Ensure Python and necessary libraries are installed.
    - Install required libraries:

      ```bash
      pip install pandas openpyxl reportlab random2 pyinstaller customtkinter pulp
      ```

3. **Run the App:**
    - Execute the Python file main.py.

4. **Explore Generated Files:**
    - Check the `common` directory for the generated .lp and .xlsx files.

## Dev explanation

1. **How dose it work:** This app use customtkinter classes to work. The main script is in main.py and inherits from CTK main window. From here on all the other modules are loaded. The other modules are classes that inherits from CTK frames, menu and topbar don't move but may be reloaded due to a change in the application while all the other classes are used as differents sub-windows for the main part of the app. they are all loaded in the dict `allFrames` and the current frame is loaded in the `mainFrame` variable. To change the frame you generaly use `show_frame`,`next_frame` or `previous_frame`. Modules have an action file that will handle their actions that are not related to tkinter. If they don't this needs to be done.

2. **Modules:**

- **topBar** Top bar with help, previous and next buttons.
- **menu** Left menu with the differents buttons.
- **projectCreation** This module is a form to allow the user to add or modify projects.
- **projectManagement** This module lists of all the projects.
- **exportToMoodle** Allow the user to download the pdf xml file.
- **solverInputFile** Upload the results from moodle.
- **solverProcess** Make and solve a model made from the previous file.
- **solverOutputManagement** You can correct minor problems here and see the results of the solver.
- **exportStudentDistribution** You can export the last files here.

3. **File generated:** All the files generated are either to download or in common, during use it is recommended to not modify common files.

- **./common/answerProjects.xlsx** All answers from moodle.
- **./common/currentCreation.txt** Temporary variable to know what project is being modified.
- **./common/dataProjects.txt** All the data from the different projects.
- **./common/recap.xlsx**  Every information needed after the output of the solver
- **./common/resultSolver.csv** Matrix of the output of the solver.
- **./common/solver.lp** File generated to be solved, no use just informationnal.
- **./common/table_xxx.xlsx** Files of the choices made by the students after the verifiction and need modification of the algorythm.

## License

This project is licensed under the ISEN license
