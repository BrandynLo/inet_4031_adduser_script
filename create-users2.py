#!/usr/bin/python3
import os
import re
import sys

def main():
    # Prompt for dry-run mode
    dry_run = input("Would you like to run in dry-run mode? (Y/N): ").strip().upper() == 'Y'
    
    for line in sys.stdin:
        match = re.match("^#", line)
        fields = line.strip().split(':')
 	#Loops through input from imported standard input (user keyboard or a certain file using <)
        #Check for lines that begin with '#', and if so, it will not be used.
        #Splits the lines with a ':' to organize the names into lists.
	if match:
            if dry_run:
                print(f"Has a '#', so it was Skipped")
            continue

        if len(fields) != 5:
	 #If the line is a match (meaning it doesn't have a #), or is exactly 5 fields long, continue forward.
            if dry_run:
                print(f"Not exactly 5 fields, Skipped")
            continue
#Take all the initial fields and put them into a user,password, and geco to organize/format.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')
 #Split to organize multiple users and passwords that are seperated from one another ex: user01 passwd, user02
        print("==> Creating account for %s..." % username)
#Prints to the end user that the cmd is being processed/made
        cmd_create = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
#Makes it so that the user has a disabled password and has certain GECOS information labeled.
	if dry_run:
            print(f"Dry-run would output {cmd_create}")
        else:
            os.system(cmd_create)
   #Prints out the command to see the cmd being run, and also executes the command by the import sys (cmd) for user creation.

        print("==> Setting the password for %s..." % username)
        cmd_passwd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        if dry_run:
            print(f"Dry-run would output {cmd_passwd}")
 #Informs you that that it has set the user password
        else:
            os.system(cmd_passwd)
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd_group = "/usr/sbin/adduser %s %s" % (username, group)
		if dry_run:
                    print(f"Dry-run would output {cmd_group}")
                else:
                    os.system(cmd_group)
#Sets the users password by echoing the password and setting it as the password for the user.
 #It will print out the cmd command and execute the os.system(cmd) command to set the password for the user.
if __name__ == '__main__':
    main()

