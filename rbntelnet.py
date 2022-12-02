import getpass
import telnetlib

HOST = "telnet.reversebeacon.net"

tn = telnetlib.Telnet(HOST, 7000)
print(tn)
print("About to call read_until\n")
tn.read_until(b"Please enter your call: ", 17)
print("Sending callsign\n");
tn.write(b"KD0FNR\n")
print("Callsign sent\n");


print(tn.read_until(b"KD0FNR", 17).decode('ascii'))
