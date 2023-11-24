import psycopg2             #a PostgreSQL adapter for Python
from psycopg2 import sql    #for building SQL queries

# Database connection parameters
db_params = { #dictionary
    'dbname': 'university_db',
    'user': 'postgres',
    'password': 'Adham@COMP3005',
    'host': 'localhost',
    'port': '5432'
}

#a function that takes an SQL query and optional values, connects to the database, executes the query, and returns the result.
#handles errors by rolling back the transaction in case of an exception.
def execute_query(query, values=None):
    connection = psycopg2.connect(**db_params) #Establishes a connection to the PostgreSQL database using the connection parameters
    cursor = connection.cursor() #Allows Python code to execute PostgreSQL command in a database session. 
                                 #Cursors are created by the connection. cursor() method: they are bound to the connection for the entire lifetime 
                                 #and all the commands are executed in the context of the database session wrapped by the connection
                                 #A cursor is used to execute SQL commands and fetch results.

    try: #Executes the SQL query using the cursor. If the values parameter is provided, it's used for parameterized queries.
        if values:
            cursor.execute(query, values) #deleteStudent for example
        else:
            cursor.execute(query) #getAllStudents for example

        result = cursor.fetchall() if cursor.description else None #Checks if the cursor has a description (metadata about the result set). If true, it fetches all the rows; otherwise, it sets result to None.
        connection.commit() #Commits the changes to the database
        return result

    except psycopg2.Error as e:
        print(f"Error: {e}")
        connection.rollback() #Rolls back the transaction to its state before the error occurred.
        raise #Raises the exception again to propagate it up the call stack.

    finally: #for cleanup
        cursor.close()
        connection.close()

def getAllStudents():
    query = "SELECT * FROM students;"
    return execute_query(query)

def addStudent(first_name, last_name, email, enrollment_date):
    query = sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) "
                    "VALUES ({}, {}, {}, {});").format(
        sql.Literal(first_name),
        sql.Literal(last_name),
        sql.Literal(email),
        sql.Literal(enrollment_date)
    )
    return execute_query(query)

def updateStudentEmail(student_id, new_email):
    query = sql.SQL("UPDATE students SET email = {} WHERE student_id = {};").format(
        sql.Literal(new_email),
        sql.Literal(student_id)
    )
    return execute_query(query)

def deleteStudent(student_id):
    query = sql.SQL("DELETE FROM students WHERE student_id = {};").format(sql.Literal(student_id))
    return execute_query(query)



# Example usage
if __name__ == "__main__":
    try:
        # Get all students
        print("All Students:")
        print(getAllStudents())

    except Exception as e:
        print(f"Application Error: {e}")

        # Add a new student
        addStudent("New", "Student", "new.student@example.com", "2023-09-03")

        # Update student email
        updateStudentEmail(1, "john.doe.new@example.com")

        # Delete a student
        deleteStudent(2)

        # Get all students after modifications
        print("All Students after modifications:")
        print(getAllStudents())

    except Exception as e:
        print(f"Application Error: {e}")

