import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': 'university_db',
    'user': 'postgres',
    'password': 'Adham@COMP3005',
    'host': 'localhost',
    'port': '5432'
}

def execute_query(query, values=None):
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        result = cursor.fetchall() if cursor.description else None
        connection.commit()
        return result

    except psycopg2.Error as e:
        print(f"Error: {e}")
        connection.rollback()
        raise

    finally:
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
        deleteStudent(3)

        # Get all students after modifications
        print("All Students after modifications:")
        print(getAllStudents())

    except Exception as e:
        print(f"Application Error: {e}")

