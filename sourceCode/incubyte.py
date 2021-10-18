# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 18:02:50 2021

@author: Mastermind
"""
import mysql.connector
import pandas as pd
import numpy as np
from datetime import datetime

#reading sample text file
data = np.loadtxt("E:\\Pooja_DBDA\\test\\data.txt", dtype='str',delimiter="|")

# connecting mysql server
database = mysql.connector.connect(host="localhost",user="root",passwd= "1qazZAQ!",database="hospital2")
cursor = database.cursor()


#iterating throught read data and storing it in mysql database
for i in range(1,len(data)):
    #converting string to date format given for Open_Date|
    opendt = datetime.strptime(data[i][4], '%Y%m%d').strftime('%Y-%m-%d')
    
    #converting string to date format given for Last_Consulted_Date|
    consuldt = datetime.strptime(data[i][5], '%Y%m%d').strftime('%Y-%m-%d')
    
    #converting string to date format given for DOB|
    dob = datetime.strptime(data[i][10], '%m%d%Y').strftime('%Y-%m-%d')

    #Formating query with placeholders
    add_info = "INSERT INTO patients (Customer_Name ,Customer_Id ,Customer_Open_Date ,Last_Consulted_Date, Vaccination_Type, Doctor_Consulted ,State ,Country, Date_of_Birth, Active_Customer) VALUES ('{}', '{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(data[i][2],data[i][3], opendt,consuldt, data[i][6], data[i][7],data[i][8], data[i][9],dob,data[i][11])

    cursor.execute(add_info)
    
    #Committing tracsaction
    database.commit()
    
    
#get data from hospital1
cursor = database.cursor(buffered=True)
query2 = "select * from patients"
cursor.execute(query2)


# fetching tables
table_rows = cursor.fetchall()

# fitting into pandas dataframe
df = pd.read_sql('SELECT * FROM patients', con=database)  

# setting default index
df.set_index(['Customer_ID'], inplace=True)  


#Creating function for getting all records from specified country
def get_data(country):                      
    data = df.loc[df['Country'] == country]
    print(data)


#Store fetched records into csv file
def store_file(country):                   
    data = df.loc[df['Country'] == country]
    data.to_csv('E:\\Pooja DBDA\\interview\\incubyte' + "_"+country + ".csv")
    print("File has been created to the specified path")


# calling functions
get_data("USA")
store_file("USA")

