# создание сокета, сервер

import socket

# Документация по сокетам
# https://docs.python.org/3/library/socket.html

# Отличный туториал от IBM
# https://www.ibm.com/developerworks/ru/library/l-python_part_10/index.html —
# Создаёт объект класса socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Связывает объект с адресом
sock.bind(("127.0.0.1", 10001))   # max port 65535
# Разрешает сокету принимать данные, "прослушивать сеть"
sock.listen(socket.SOMAXCONN)

# Разрешает сокету соединение
conn, addr = sock.accept()
while True:
    # recv(1024) отвечает за получение данных от сервера пачками по 1024 байта (1Кб)
    data = conn.recv(1024)
    # Если данных нет, то программа завершается
    if not data:
        break
    # process data
    print(data.decode("utf8"))

# Закрываем соединение
conn.close()
# Закрываем сокет
sock.close()
