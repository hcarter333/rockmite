import getpass
import telnetlib
import time
import sys
import signal

HOST = "telnet.reversebeacon.net"

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    tn.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print("Opening rnb tn");
tn = telnetlib.Telnet(HOST, 7000)

print(tn)
print("About to call read_until\n")
tn.read_until(b"Please enter your call: ", 17)
print("Sending callsign\n");
tn.write(b"KD0FNR\n")
print("Callsign sent\n");

#for x in range(2):
#print(tn.read_until(b"DX de", 5).decode('ascii'))
print("starting interact")
tn.interact()
print("done with interact")
