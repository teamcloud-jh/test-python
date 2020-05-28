import mysql.connector
import datetime

def start_db():
  # start db connection
  database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='test-read-db'
  )

  print(f'Accessing database - {database}') 

  return database

def access_db(database):
  # read databese
  sql_select_Query = 'SELECT * FROM `test-read-db` ORDER BY `text` ASC'
  cursor = database.cursor()
  cursor.execute(sql_select_Query)
  records = cursor.fetchall()
  print(f'Records in table \n {records} \n\n')

  # read database
  # sql = "INSERT INTO `test-read-db` (`text`) VALUES ('Test text 2')"
  # # val = ("Test text 2")
  # cursor.execute(sql, val)
  # database.commit()
  # print(f'{cursor.rowcount} record inserted.\n')

  cursor.execute(sql_select_Query)
  records = cursor.fetchall()
  print(f'New records in table \n {records} \n\n')

  database.close()

  return records

def write_to_file(content):
  # write to file
  f = open("db-output.txt", "a")
  f.write(f'Database output at {datetime.datetime.now()}\n{content}\n')
  f.close()

  #open and read the file
  f = open("db-output.txt", "r")
  print(f.read()) 

mydb = start_db()

if mydb is not None:
  result = access_db(mydb)
  write_to_file(result)