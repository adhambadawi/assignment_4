# assignment_4

# PostgreSQL Database Interaction Application

This application is designed to interact with a PostgreSQL database using a provided schema. It includes functions for CRUD (Create, Read, Update, Delete) operations on a 'students' table.

## Database Schema

Table name: students
Fields:
- student_id: Integer, Primary Key, Auto-increment
- first_name: Text, Not Null
- last_name: Text, Not Null
- email: Text, Not Null, Unique
- enrollment_date: Date

## Initial Data

The 'students' table is initially populated with the following data:

```sql
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');


Application Functions:- 

getAllStudents():
Retrieves and displays all records from the 'students' table.

addStudent(first_name, last_name, email, enrollment_date):
Inserts a new student record into the 'students' table.

updateStudentEmail(student_id, new_email):
Updates the email address for a student with the specified student_id.

deleteStudent(student_id):
Deletes the record of the student with the specified student_id.


Instructions:
Set Up PostgreSQL Database:

Install PostgreSQL on your system.
Create a new database, e.g., "university_db."
Use the provided schema to create the "students" table within the "university_db" database.
Insert the initial data into the "students" table.


Develop the Application:

Choose a programming language for your application (the provided example uses Python with psycopg2).
Update the database connection parameters in the application code.
Run the application to interact with the PostgreSQL database.


Run the Application:

Ensure that the required libraries (e.g., psycopg2) are installed.
Execute the application code, observing the output.
Running the Example

Install the required Python packages:

bash

pip install psycopg2-binary
Update the database connection parameters in the application code.

Run the application:

bash:

python your_application_file.py

Note
Replace 'your_application_file.py' with the actual filename of your application code.

 
Remember to replace placeholders such as 'your_application_file.py' with the actual filename of your application code. Additionally, you might want to include any additional instructions or information specific to your project.
