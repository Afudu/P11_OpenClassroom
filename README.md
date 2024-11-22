# OpenClassrooms - Python Developer Path

**Project 11:** Enhance a Python Web Application With Testing and Debugging

**Student:** Abdoul Baki Seydou

**Date:** 20/05/2024

## Abstract
The project involves enhancing the Python web application used by Güdlft, 
a company that organizes regional competitions.

The application is built with Flask - a Python framework, and stores data in JSON files 
to avoid database dependencies.

The initial code is placed in this [repo](https://github.com/OpenClassrooms-Student-Center/Python_Testing/)
and should allow the following functionalities to the club secretaries:

  * They can log in using their email.

  * They can view a list of upcoming competitions.

  * They can select a competition and use points to book places.

     - Points used will be deducted from their total.

     - Each place booked reduces the competition places and the club's points by 1.

     - Booking Restrictions: Secretaries cannot book more than the available spots, 
     more than they can purchase, exceed 12 spots per competition, or book past competitions.

     - If the booking is successful, a confirmation message is displayed; else,
     an explicit error message is displayed.

  * They can log out of the system.

## Enhancements and immediate tasks

The enhancements are broken into phases, with a focus on testing, 
debugging and adding new features.

**Phase 1:**
The first phase involves testing and fixing the bugs in the initial code.
 

**Phase 2:**
The second phase introduces new functionalities to be added to the application:

  * Public Points Board: a public, read-only board displaying the points available for each club
   without requiring login.

  * Efficient build and rendering times: ensuring competition lists are retrieved 
in no more than 5 seconds, and no more than 2 seconds to update the points total.

  * Additional functionalities.

All the bugs fixed and features added have been created in separate branches, following the naming convention:
````<feature/bug>/descriptive-name````.

## Requirement

Latest version of Python must be installed.

You can download the latest version for your system from : https://www.python.org/downloads/

## Installation

The following commands rely on the knowledge of how to use the terminal (Unix, macOS) or the command line (Windows).

**1 - Get the code**

  * Unix/macOS/Windows

    ```bash
    git clone https://github.com/Afudu/P11_OpenClassroom.git
    ```

**2 - Move to the folder**

  * Unix/macOS/Windows

    ```bash
    cd P11_OpenClassroom
    ```  

**3 - Create a virtual environment**

  * Unix/macOS

    ```bash
    python3 -m venv pythonenv
    ```
    
  * Windows

    ```bash
    py -m venv pythonenv
    ```
  
  * Note: you can create the virtual environment in another folder, then move to that folder to run the command above.
  * Example: in the above command, our virtual environment created is called pythonenv. 
    You can give a different name.

**4 - Activate the virtual environment created**

  * Unix/macOS

    ```bash
    source pythonenv/bin/activate
    ```

  * Windows

    ```bash
    pythonenv\Scripts\activate
    ```

**5 - Securely upgrade pip**

  * Unix/macOS/Windows

    ```bash
    py -m pip install --upgrade pip
    ```

**6 - Install all dependencies**

  * Unix/macOS/Windows

    ```bash
    pip install -r requirements.txt
    ```

## Running the application

**Move to the folder**

  * Unix/macOS/Windows

    ```bash
    cd Python_testing
    ```

**Start the server**

  * Unix/macOS

    ```bash
    export FLASK_APP=server
    export FLASK_ENV=development
    flask run
    ```

  * Windows

    ```bash
     set FLASK_APP=server
     set FLASK_ENV=development
     flask -app server run
    ```

After the server has started,  navigate to http://127.0.0.1:5000/ to check the app.

The email addresses to log in with are in the file clubs.json located in the Python_Testing folder.

## Testing
The application functionalities have been tested with ```pytest``` - a Python testing framework, 
and ```coverage``` - a tool for measuring code coverage of Python programs, with a code coverage of 97%, 
which is above the requirement of 60%.

The tests are categorized and located in the ```tests``` folder.

  * To run all the tests use:
  
    ```bash
    pytest
    ```

* To measure the code coverage of all tests use:
  
    ```bash
    coverage run -m pytest
    ```

*  To view a simple coverage report use:

     ```bash
      coverage report
     ```

* To run a single test use: 

   ```pytest [followed by the path to the test file]```

   * Examples: 
  
     * Unix/macOS
      ```pytest ./tests/unit_tests/test_logout.py```
    
     * Windows:
     ```pytest .\tests\unit_tests\test_logout.py```

 
   * Note : when running the tests, the test data is not saved in the JSON files to preserve data integrity after tests. 

## Performance Test

The performance of the application has been tested with ```Locust```, with the rendering times adhering
to the functional requirements : less than 5 seconds to retrieve data, and less than 2 seconds to update data.

To run a performance test, with the application server running:

1. Move to the folder where the file ```locustfile.py``` is located.

   * Unix/macOS/Windows

     ```bash 
      cd tests\performance_tests
     ```

2. Run the locust command:

   * Unix/macOS/Windows

     ```bash
      locust
     ```

3. Then go to http://localhost:8089/

4. Type the host url http://127.0.0.1:5000/ , default number of users = 6, then click start.

## PEP 8 adherence

The folder ```flake_report``` in the repository contains an HTML report generated by flake8-html which displays no errors. 

A new report can be generated by running the command below.

  * Unix/macOS/Windows

    ```bash
    flake8
    ```

The file ```setup.cfg``` in the root of the repository contains the settings used to generate the report.

## Reports
The test coverage, performance test, and PEP 8 adherence reports are located in the ```reports``` folder located in the root 
of the repository.