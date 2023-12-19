# Voter Registration Project

The aim of this project is to maintain a voter database and address the issue of discrepancies between registered voters and voter turnout. The project implements a database management system to delete inactive voters (i.e., those who haven't voted in the past two elections) and a search algorithm that allows voters to find their polling unit using their voter ID.


### Installation
 You can install the necessary libraries with the following commands:
* `Pip install Faker `
* `Pip install Flask `
* `Pip install markupsafe`
* `Pip install jinja2`
* `pip install click`
* `Pip install itsdangerous`
* `Pip install pandas`


### Usage
 To use this project, you can do the following:

1. Add new Voters: you can test the project by adding new voters to the database. You can do this by running the fakefile.py. This file generates 100,000 new voters. You can change the number. After running this file run the displayDatabase.py file

2. Search for polling unit: You can test the search algorithm by searching for a voter using their voter ID, Name, and Date of birth.  You can do this by running the findingpollingunit.py and clicking on the link returned in the console. Open the CSV file to see the voter's information you could search.

3. Delete inactive voters: you can test the database management system by deleting inactive voters. You can do this by running the inactivevoters.py.
  


### Troubleshooting 

1. Error: "`ModuleNotFoundError: No module named 'the library name'`"
Solution: This error occurs when the library name in the error has not been installed. To fix this. Make sure all the libraries above have been installed.
 
2. Server Error - Port [port number] already in use
Solution: run this code on the terminal 
Lost -I: [port number]
Kill -9 <PID>



