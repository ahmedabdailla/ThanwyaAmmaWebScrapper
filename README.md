# ThanwyaAmmaWebScrapper

Supersimple, 

```python
pip install mysql.connector
pip install selenium
pip install requests
```

open main.py and edit the MySQL for MySQL DB
and then Import the DB attached

Note : the MySQL Data located twice, be sure to change both of them. because the application runs on 2 threads. to make the process faster
```python
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="123456789",
                    database="thanwyascrape"
                )
```

<b>Search for variable called Number1, set it to the starting number you wish to count from. and Number2 to the starting Number + 1</b>
then run the application. simply.

This is a webscrapping using multithread and selenium for a website called " http://natega2.youm7.com/ " that's deitcated to present the National High School results every year for National Egyptian High School. 

The Students ID is formed of 6 numbers, you can start from 150000 to 600000 and it would be working.
The multithread handles the Student ID by the way that's one thread is for prime numbers and the other for odd numbers. that's why Number2 is Number1+1 because when we add 2 to each one we keep one odd and one for prime. 
