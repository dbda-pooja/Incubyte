create database hospital2;

use hospital2;

create table if not exists patients(Customer_Name varchar(255) primary key not null,
									Customer_ID varchar(18) not null,
                                    Customer_Open_Date date not null,
                                    Last_Consulted_Date date,
                                    Vaccination_Type char(5),
                                    Doctor_Consulted char(255),
                                    State char(5),
                                    Country char(5),
                                    Post_Code int,
                                    Date_of_Birth date,
                                    Active_Customer char(1)
                                    );


select * from patients;  


drop table patients;