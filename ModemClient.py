import time         #unused
import serial       #gives acess to pySerial library
import threading    #gives acess to thread creation code


#Function executed by the listening thread. 
#It reads byte data coming in from the serial port,
#translates it if it is able to and sends it to the console
#Parameter port determines what port object should this function listen to.
def read_from_port(port):   
    while True:
        data = port.read_until('\r'.encode('utf-8'))
        try:
            data = data.decode('utf-8')
            if data == '':      #Sometimes the modem sends empty data packets, we filter them out.
                continue
            print(data)
        except:
            continue            #Ignore untranslatable data packets.        


modem_port = serial.Serial(port='COM1', xonxoff=True, dsrdtr=True, timeout=5)   #Create a port object connected to device 'COM1'. 'timeout=5' sets the read timeout to 5 seconds.
print('Port opened!\n')
t = threading.Thread(target=read_from_port, daemon=True, args=(modem_port,))    #Create a thread executing the read_from_port() function. Reading from the port blocks the current thread, so it has to be done this way.
print('Made a listening thread!')
t.start()
while True:
    message=input()             #Read the message to be sent from keyboard
    if message == 'exit':       #If it says 'exit', stop the application
        exit()
    else:                       #Otherwise, send it trough the serial port.
        modem_port.write((message + '\r').encode('utf-8'))  #Note: the commands sent and recieved from the modem have to end with a carriage return symbol ('\r') instead of a newline sumbol ('\n').
