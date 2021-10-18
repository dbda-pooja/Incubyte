# Incubyte
🔹Overview:
This repository made to demonstrate implementation of given assessment.Also, a dummy database has been created to demonstarte a simple data flow in different formats from server to the local system, using country-based row filteration. For demonstrating working of data pipeline different tools are used which are listed below

🔸Concepts:
*Data processing
ETL

🔸Tools & Technologies:
* Python
* MySQL Workbench
* Spyder
* Pandas
* MySQL connector

🔹Working:

* step 1: Firstly MySQL database has been created with specified schema.
* step 2: <a href="https://github.com/dbda-pooja/Incubyte/blob/master/sourceCode/incubyte.py">incubyte.py </a>python script, reading sample text file
* step 3: connecting mysql server
* step 4: iterating throught read data and storing it in mysql database
* step 5: The retrieved data is fitted into pandas dataframe for further table manipulation.
* step 6: get_data() & store_file() functions are called to fetch the desired data rows and generating .csv and string file formats to specified path, accepting country names as            parameters for filtering rows.
         For example: get_file("IND") generates<a href="https://github.com/dbda-pooja/Incubyte/blob/master/Output/incubyte_IND.csv"> incubyte_IND.csv </a> to the specified local path. <a href="https://github.com/dbda-pooja/Incubyte/blob/master/Output"> CLick here </a> to see sample output files.
* step 7: git push and commit is done by using GitBash.


* To install mysql.connector:

   pip install mysql.connector
* To install pandas:

   pip install pandas

🔹References:
* MySQL Connector Python
* Pandas docs


