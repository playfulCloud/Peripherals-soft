import serial
import threading
from xmodem import XMODEM

def read_from_port(port):
    while True:
        data = port.read_until(b'\r')
        if data:
            try:
                print(data.decode('utf-8'), end='')
            except UnicodeDecodeError:
                print(data, end='')

def getc(size, timeout=1):
    return modem_port.read(size) or None

def putc(data, timeout=1):
    modem_port.write(data)
    time.sleep(0.1)  # give some time to buffer

# Create a port object connected to device 'COM1'. 'timeout=5' sets the read timeout to 5 seconds.
modem_port = serial.Serial(port='COM1', xonxoff=True, dsrdtr=True, timeout=5)
print('Port opened!\n')

# Start the listening thread
t = threading.Thread(target=read_from_port, daemon=True, args=(modem_port,))
print('Starting a listening thread...')
t.start()

# Initialize XMODEM protocol
modem = XMODEM(getc, putc)

# Main program loop
while True:
    message = input("Enter command or 'exit': ")
    
    if message == 'exit':
        modem_port.close()
        break
    elif message == 'send':
        filename = input("Enter the filename to send: ")
        with open(filename, 'rb') as file_to_send:
            modem.send(file_to_send)
        print("File sent.")
    elif message == 'receive':
        filename = input("Enter the filename to save as: ")
        with open(filename, 'wb') as file_to_receive:
            modem.recv(file_to_receive)
        print("File received.")
    else:
        modem_port.write((message + '\r').encode('utf-8'))
