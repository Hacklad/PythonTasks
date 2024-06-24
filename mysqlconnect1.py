### Assignment:
# Create a DB and four tables and use primary keys for the ids(Autoincrement primary key)
import mysql.connector

daysaz = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "apexbank",
    auth_plugin = "mysql_native_password"
)

con_string = daysaz.cursor()
print("connected")

# con_string.execute("CREATE DATABASE APEXBANK")
con_string.execute("CREATE TABLE studentz_table (student_id INT (6) PRIMARY KEY AUTO_INCREMENT) ")
con_string.execute("CREATE TABLE DEPTz (student_id INT (6) PRIMARY KEY AUTO_INCREMENT, L_Name VARCHAR (20), F_Name VARCHAR (20), Dept_name VARCHAR (20)) ")
con_string.execute("CREATE TABLE Exam_scorez (student_id INT (6) PRIMARY KEY AUTO_INCREMENT, Matric_Num INT (6), Total_score INT (4)) ")
con_string.execute("CREATE TABLE TEACHERSz (staff_id INT (6), Full_Name VARCHAR (20) ) ")

### To show table content
con_string.execute("SHOW TABLES")
for table in con_string:
    print(table)

valuez = "INSERT INTO dept (student_id, L_name, F_name, Dept_name) VALUES (%s,%s,%s,%s)"

data_values = (
    (1, 'Iyanu','Arowosola','0911111'),
    (2, 'Isreal','sola','29911911')
)

con_string.executemany(valuez, data_values)
daysaz.commit()
con_string.execute("CREATE TABLE T2_DEPT (id INT NOT NULL AUTO_INCREMENT, DEPT VARCHAR (20), HOD VARCHAR (20) PRIMARY KEY (id))")
con_string.execute("CREATE TABLE T3_BRANCH (id INT NOT NULL AUTO_INCREMENT, BRANCHES VARCHAR (20), BRANCH_HEAD VARCHAR (20) PRIMARY KEY (id))")
con_string.execute("CREATE TABLE T4_SAL (id INT NOT NULL AUTO_INCREMENT, SALARIES VARCHAR (10) PRIMARY KEY (id))")