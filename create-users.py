#!/usr/bin/python3

# INET4031
# Brandyn Lo
# Data Created 10/27/2025
# Date Last Modified 10/27/2925

#import OS for WIN/Linux  integration
#import RE for string integration
#import SYS for python variables
import os
import re
import sys


def main():
    for line in sys.stdin:
	#Loops through input from imported standard input (user keyboard or a certain file using <)
        #Check for lines that begin with '#', and if so, it will not be used.
        match = re.match("^#",line)

        #Splits the lines with a ':' to organize the names into lists. 
        fields = line.strip().split(':')

	#If the line is a match (meaning it doesn't have a #), or is exactly 5 fields long, continue forward.
	if match or len(fields) != 5:
            continue

        #Take all the initial fields and put them into a user,password, and geco to organize/format. 
	username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #Split to organize multiple users and passwords that are seperated from one another ex: user01 passwd, user02
        groups = fields[4].split(',')

        #Prints to the end user that the cmd is being processed/made
        print("==> Creating account for %s..." % (username))
        #Makes it so that the user has a disabled password and has certain GECOS information labeled.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #Prints out the command to see the cmd being run, and also executes the command by the import sys (cmd) for user creation. 

        os.system(cmd)

        #Informs you that that it has set the user password
        print("==> Setting the password for %s..." % (username))
        #Sets the users password by echoing the password and setting it as the password for the user.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #It will print out the cmd command and execute the os.system(cmd) command to set the password for the user.
        os.system(cmd)

        for group in groups:
            #Looks for if the group is not '-', it will not add the user to any groups we made. This is because '-' classifies it as unclassified in a group.  
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
