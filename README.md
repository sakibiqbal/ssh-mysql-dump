# ssh-mysql-dump

Project name: MySQL remote dump 
Author: Sakib Iqbal 
Author email: mail@sakibiqbal.com 
Short description: Script to dump mysql database into local from remote server. 
Script Language: Python 2.7 
Dependancy: paramiko, setuptools 

Idel scenario and dependency:
 - Server hosted MySQL
 - Server with ssh access
 - ssh user with write permission at it's ~ folder.
 - mysqldump command should be enabled in the server.

How to run the script:
 - In shell, run "easy_install paramiko"
 - Goto the script directry
 Method 1:
 - Run the script with this command: "python mysql-remote-dump.py"
 - Fill up the form
 Method 2:
 - Run the script with this command: "python mysql-remote-dump.py <host> <host user> <host password> <DB name> <DB user> <DB pass>"
 
Form documentation:
 - Host name: Remote server host name. Ex. example.com
 - Server user name: Remote server ssh username
 - Server password: Remore server ssh password
 - Database Name: Remote server mysql database name
 - Database user name: Remote server mysql database username
 - Database password: Remote server mysql database password
