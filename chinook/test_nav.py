import pandas as pd
import sqlite3
print('\n\n')


DB_FILE_PATH = 'chinook.db'
conn = sqlite3.connect(DB_FILE_PATH)
print('CONNECTION:', conn)
# IF DATABASE IS FROM CSV, SEE THIS: 
#  https://github.com/jacobpad/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/buddymove_holidayiq.py

curs = conn.cursor()
print('CURSOR:', curs)
 
# Set a query, execute it and return/print the results.
# query1 = 'SELECT * FROM "TABLE_NAME";'
query1 = '''
    SELECT * FROM albums;
'''
result1 = curs.execute(query1).fetchall() # need to have the `.fetchall()` to return useful data
print(query1)
print('RESULT 1:\n', result1)
print('\n') 

#
# Question 2: 
#   Which songs in this dataset were written by AC/DC?
#
print('QUESTION 2:\nWhich songs in this dataset were written by AC/DC?')
query2 = '''
    SELECT Name, Composer FROM tracks t
    WHERE Composer = 'AC/DC'
'''
result2 = curs.execute(query2).fetchall()
print(query2)
print('RESULT 2:\n', result2)
print('\n') 

#
# Question 3: 
#   How long would it take to listen to all the songs in our 
#       dataset that were written by Johannes Sebastian Bach?
#
print('QUESTION 3:\nHow long would it take to listen to all the songs in our dataset that were written by Johannes Sebastian Bach?')
query3 = '''
    SELECT t.Name, t.Milliseconds, t.Composer FROM tracks t 
    WHERE Composer = 'Johann Sebastian Bach';
'''
result3 = curs.execute(query3).fetchall()
print(query3)
print('RESULT 3:\n', result3)
print('\n') 

#
# Question 4: 
#   Find all customers with the first name 'Phil'.
#
print('QUESTION 4:\nFind all customers with the first name \'Phil\'.')
query4 = '''
    SELECT c2.FirstName, c2.LastName FROM customers c2 
    WHERE c2.FirstName = 'Phil'
'''
result4 = curs.execute(query4).fetchall()
print(query4)
print('RESULT 4:\n', result4)
print('\n') 

#
# Question 5: 
#   What is the first name, last name, title, and birthday of all the employees.
#
print('QUESTION 5:\nWhat is the first name, last name, title, and birthday of all the employees.')
query5 = '''
    SELECT e.FirstName, e.LastName, e.Title, e.BirthDate FROM employees e 
'''
result5 = curs.execute(query5).fetchall()
print(query5)
print('RESULT 5:\n', result5)
print('\n') 

#
# Question 6: 
#   Which tracks in our dataset were written by Jimi Hendrix?
#
print('QUESTION 6:\nWhich tracks in our dataset were written by Jimi Hendrix?')
query6 = '''
    SELECT t.Name, t.Composer FROM tracks t
    WHERE t.Composer = 'Jimi Hendrix'
'''
result6 = curs.execute(query6).fetchall()
print(query6)
print('RESULT 6:\n', result6)
print('\n') 




# COMMIT AND CLOSE
# pg_conn.commit()
# pg_curs.close()
print('\nWORK COMMITED AND CONNECTION CLOSED\n')

# ANOTHER EXAMPLE:
# https://github.com/jacobpad/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/Assignment_Part_1a.py