# inet_4031_adduser_script
**Program Description**
This Python script automates the process of adding new users to a Linux system. Traditionally, having to add a user typically involves running /usr/sbin/adduser to create the user account, setting a password with /usr/bin/passwd, and assigning the user to groups using /usr/sbin/adduser <username> <group>. This script replicates this by reading from an input file provided with all the end users names so that manual operations are no longer required.
**
Program User Operation**
This script reads user data from standard input (from a file) and creates user accounts, sets passwords, and assigns users to groups. To use the program, you can edit the create-users.input file to add as many users as you need. The script processes each line of input, so comments '#' and without 5 fields won't be processed.

**Input File Format**
The input file must be a plain text file with one user per line, where each line contains five fields separated by colons (:). The fields are as follows:

Username (Field 1): The  username for account.
Password (Field 2): The password for the account.
Last Name (Field 3): The user’s last name, used in the GECOS field.
First Name (Field 4): The user’s first name, used in the GECOS field.
Groups (Field 5): A comma-separated list of groups the user belongs to. If no groups are desired, use '-' called hyphens.
**Command Excuction**
Set the Python file to be executable. Changing the modification using chmod x is an option. Then run the command ./create-users.py < createusers.input 

**Dry Run**
Dry run does not work at this moment. 
