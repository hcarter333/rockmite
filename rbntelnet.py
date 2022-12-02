import getpass
import telnetlib
import time

HOST = "telnet.reversebeacon.net"

tn = telnetlib.Telnet(HOST, 7000)
print(tn)
print("About to call read_until\n")
tn.read_until(b"Please enter your call: ", 17)
print("Sending callsign\n");
tn.write(b"KD0FNR\n")
print("Callsign sent\n");

#for x in range(2):
#print(tn.read_until(b"DX de", 5).decode('ascii'))
tn.interact()
time.sleep(15.5)
#print(tn.read_eager().decode('ascii'))
#print(tn.read_until(b"DX de", 5).decode('ascii'))

tn.close()

#DX de DL1HWS-#:  14033.0  HZ1UAE         CW     7 dB  28 WPM
