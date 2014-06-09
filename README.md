RepeatedQuerying
================

A Django app such that a browser makes an ajax request each 5 seconds

To use this app:

1. Clone the repo

2. Go to settiings.py, change the username and password of the database to your mysql username and password

3. Log in to your mysql, execute the command: "create database demoapp2"

4. cd to the directory of your app

5. run "python manage.py syncdb"

6. Execute command "mysql -p" and then enter your passwor. Use command "use demoapp2" to change the database to the one we are using. Now use command "insert into newapp_counter values(1,0);" to create an entry for the counter variable.

7. run "python manage.py runserver"

8. Open 127.0.0.1:8000. Here you go!
