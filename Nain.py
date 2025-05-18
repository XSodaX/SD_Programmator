import serial
import time


# Функция для управления GPIO через DTR
def send_data(data):
    # Открываем COM-порт (замени на свой COM порт)
    ser = serial.Serial('COM9')  # Укажи правильный COM порт (например, 'COM3')

    for bit in data:
        if bit == '1':
            # Включаем DTR (HIGH)
            ser.setDTR(1)
            ser.setDTR(0)
        elif bit == '0':
            # Выключаем DTR (LOW)
            ser.setDTR(0)

        print(f"Sent {bit}")  # Выводим информацию о переданном бите
        time.sleep(1)  # Ждем 1 секунду

    # Закрываем порт после завершения
    ser.setDTR(0)
    ser.close()


# Вводим данные
data_to_send = input("Введите данные (например, 1011): ")

# Отправляем данные через CP2102
send_data(data_to_send)

