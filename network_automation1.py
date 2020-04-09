import getpass
import sys
import telnetlib

#chmod +x ./net_auto1 (to make script executable in linux

#
#Host = ""
from telnetlib import Telnet

user = raw_input("Enter your remote account: ")
password = getpass.getpass()

for n in range (72.77):
    HOST = "192.168.122." + str(n)
    tn = telnetlib.Telnet(HOST)  # type: Telnet

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
       tn.read_until("Password: ")
        tn.write(password + "\n")

        tn.write("enable\n")
        tn.write("cisco\n")
        tn.write("conf t\n")
        tn.write("int loopback 0\n")
        tn.write("ip address 1.1.1.1 255.255.255.255 \n")

        tn.write("conf t\n")

     for n in range (2,10):
         tn.write("vlan " + str(n) + "\n")
         tn.write("name Python_VLAN_" + str(n) + "\n")

         tn.write("end\n")

         tn.write("exit\n")

print tn.read_all()

#loop example for creating lots of vlan
