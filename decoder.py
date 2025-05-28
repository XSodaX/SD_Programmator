import sys
import time
from fileinput import close

import serial

with open('./Settings.txt','r') as file:
    Settings = file.read().splitlines()

PORT = str(Settings[0])
throughput = int(Settings[1])
Memory = int(Settings[2])

decode = ''
char = ''
charMass = []
Error = 'Application Shutdown...'

text = input('Word: ')


for i in range(len(text)):
    char=(format(ord(text[i]), 'b'))
    charMass.append(char.zfill(8))
print(charMass)
for j in range(charMass.__len__()):
    decode += chr(int(charMass[j],2))
print(decode)
MemoryUse = charMass.__len__() * 8

if Memory < MemoryUse:
    print("insufficient memory!")
    print('The data outweight for:', MemoryUse / Memory * 100 - 100, '% of the memory')
    input('Press ENTER to close programm')
    sys.exit(Error)
else:
    print('The data takes up ', MemoryUse / Memory * 100, '% of the memory')
    print('All time:', round(MemoryUse / throughput, 2), 'sec')

def send_data(data):
    try:
        # Попробуем открыть неверный порт
        ser = serial.Serial(PORT, 9600)  # Укажи свой порт
        print("Порт открыт успешно!")
    except serial.SerialException:
        input("INVALID PORT")
        sys.exit(Error)
    ser.setDTR(False)
    for c in range(data.__len__()):
        for p in range(8):
            ser.write(int(data[c][p]))
            ser.setDTR(True)
            ser.setDTR(False)
            print(int(data[c][p]), end='')
            time.sleep(throughput)
        print('')


    ser.close()
    print("The data has been uploaded successfully!")
send_data(charMass)
input('Press ENTER to close programm')