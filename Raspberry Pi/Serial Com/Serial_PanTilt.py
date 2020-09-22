import serial 

ser = serial.Serial('/dev/ttyUSB0', 9600)

while True: 
    data = ser.readline().strip().decode('utf-8').split(';')
    print(data,'\n')

#testing testing