

import os
import getpass
os.system("tput setaf 4")
print("\t\t\tHello World ")
os.system("tput setaf 6")
print("\t\t\t ----------------------------------------------")

print("remote/local")
location = input()

#apass = "root"
#password = getpass.getpass("Enter Your Password")
#if apass != password:
 #   print("Authentication failed")
  #  exit()


if location == "remote":
    print("Tell me IP of remote system")
    IP = input()
    os.system("tput setaf 4")
    print("\t\t\tPlease ENTER TO CONTINUE : ")
    os.system("tput setaf 5")
    os.system("ssh-keygen -y")
    os.system("ssh-copy-id root@{}".format(IP))

while True:
        print("""press 1 : to see date 
press 2 : calander
press 3 : web server
press 4 : create user
press 5 : exit from command
Press 6 : Start docker Services
Press 7 : Create your blogs with wordpress
Press 8 " Stop the wordpress
        """)
        print("Enter Your Choice",end="")
        ch = input()
        print(ch)

        if location == "local":
            if int(ch)==1:
                os.system("date")6
            elif int(ch)==2:
                os.system("cal")
            elif int(ch)==3:
                os.system("systemctl start httpd")
                print("Your Server is Started")
            elif int(ch)==5:
                exit()
            elif int(ch)==4:
                print("Please enter the name of the user")
                i = input()
                os.system("useradd {}".format(i))
            elif int(ch)==7:
                os.system("docker-compose up -d")
                print("Your Services is Started")
            elif int(ch)==8:
                os.system("docker-compose stop")
            elif int(ch)==6:
                print("""1. Do want to See the images of docker")
                2. If the container is already launched to see the containers
                3. Do You want to launced any container""")
                p = int(input("Enter any number please"))
                if p==1:
                    os.system("docker images")
                elif p==2:
                    os.system("docker ps -a")
                elif p==3:
                    print("""press 1 : For Ubuntu
                    Press 2 : For CentOS 
                    press 3 : For Your own Created Image 
                    """)
	
