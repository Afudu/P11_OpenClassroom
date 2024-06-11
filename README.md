# OpenClassrooms - Python Developer Path

**Project 11:** Enhance a Python Web Application With Testing and Debugging

**Student:** Abdoul Baki Seydou

**Date:** 20/05/2024

# Project Scope
The project involves enhancing the Python web application used by Güdlft, a company that organizes regional competitions.

The application is built with Flask - a Python framework, and stores data in JSON files 
to avoid database dependencies.

The enhancements are broken into phases, following the functional requirements, with a focus on testing, 
debugging and adding new features.

**Phase 1:**

The code for the initial phase is placed in this [repo](https://github.com/OpenClassrooms-Student-Center/Python_Testing)
and addresses the following functionalities for club secretaries:

  * Login: They can log in using their email.

  * Viewing Competition List: They can view a list of upcoming competitions.

  * Booking Places:** They can select a competition and use points to book places.

     Points used will be deducted from their total.

     Each place booked reduces the competition places and the club's points by 1.

     Booking Restrictions: Secretaries cannot book more than the available spots, 
     more than they can purchase, exceed 12 spots per competition, or book past competitions.

     If the booking is successful, a confirmation message is displayed; else,
     an explicit error message is displayed.

  * Logout: They can log out of the system.

**Phase 2:**

The second phase introduces:

  * Public Points Board: A public, read-only board displaying the points available for each club
   without requiring login.

  * Performance Requirements: Efficient build and rendering times, ensuring competition lists are retrieved 
in no more than 5 seconds, and no more than 2 seconds to update the points total.

# Immediate Tasks:

  1.	**Bug Fixing:** Resolve the bugs in Phase 1 and implement error handling.

  2.	**Phase 2 Implementation:** Add the functionalities and requirements specified for Phase 2.

# Requirement

Latest version of Python must be installed.

You can download the latest version for your system from : https://www.python.org/downloads/

# Installation

The following commands rely on the knowledge of how to use the terminal (Unix, macOS) or the command line (Windows).

**1 - Get the code**

  * $ git clone https://github.com/Afudu/P11_OpenClassroom.git

**2 - Move to the folder**

  * Unix/macOS/Windows: cd P11_OpenClassroom

**3 - Create a virtual environment**

  * Unix/macOS: python3 -m venv pythonenv
  * Windows: py -m venv pythonenv
  
    * Note: you can create the virtual environment in another folder, then move to that folder to run the command above.
    * Example: in the above command, our virtual environment created is called pythonenv - you can give a different name.

**4 - Activate the virtual environment created**

  * Unix/macOS: $ source pythonenv/bin/activate

  * Windows: pythonenv\Scripts\activate

**5 - Securely upgrade pip**

  * Unix/macOS/Windows: pip install --upgrade pip

**6 - Install all dependencies**

  * Unix/macOS/Windows: pip install -r requirements.txt

# Running the application

**Move to the folder**

  * Unix/macOS/Windows: cd Python_testing

**Start the server**

  * Unix/macOS
    * export FLASK_APP=server
    * export FLASK_ENV=development
    * flask run

  * Windows:
    * set FLASK_APP=server
    * set FLASK_ENV=development
    * flask run

After the server has started,  navigate to http://127.0.0.1:5000/ to check the app.

The email addresses to log in with are in the file clubs.json located in the Python_Testing folder.

# Testing
The application functionalities have been tested with pytest - a Python testing framework, 
and coverage - a tool for measuring code coverage of Python programs, with a code coverage of 98%.

The tests are categorized and located in the tests/ folder.

**Test Execution:** Unix/macOS/Windows

* To run all the tests use:
  * pytest

* To measure the code coverage of all tests use:
  * coverage run -m pytest

*  To view a simple coverage report in the terminal or command line:
   * coverage report

* To run a single test use: 
  * pytest followed by the path to the test
  * Example: pytest .\tests\unit_tests\test_logout.py
    
# Performance Test
The performance of the application has been tested with Locust, with the rendering times adhering
to the functional requirements : less than 5 seconds to retrieve data, and less than 2 seconds to update data.

To run a performance test, with the application server running:

1 - Move to the folder where the file locustfile.py located
   * cd tests\performance_tests\

2 - Run locust

3 Then go to http://localhost:8089/

4 - Enter the host url http://127.0.0.1:5000/ , default number of users = 6, then click start.

# PEP 8 adherence

The folder 'flake_report' in the repository contains an HTML report generated by flake8-html which displays no errors.
A new report can be generated by running the following command in the terminal (Unix, macOS) 
or command line (Windows): flake8

The file setup.cfg in the root of the repository contains the settings used to generate the report.

# Reporting
The test coverage, performance test, and PEP 8 adherence reports are located in the reports/ folder located in the root 
of the repository.