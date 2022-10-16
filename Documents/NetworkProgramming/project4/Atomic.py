import datetime
import socket
def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(datetime.datetime.now().strftime("%s"))
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch
s = socket.socket()
webserver = "time.nist.gov"
port = 37
s.connect((webserver, port))
ht = f"GET / HTTP/1.1\r\nHost: {webserver}\r\nConnection: close\r\n\r\n"
encodedht = ht.encode("ISO-8859-1")
s.sendall(encodedht)
data = b''
while True:
    c = s.recv(4096)
    if c == b'':
        break
    data += c
    value = int.from_bytes(data, "big")
    print(f"NIST TIME: {value}")
    print(system_seconds_since_1900())
    if len(c) == 0:
        s.close()
        break


