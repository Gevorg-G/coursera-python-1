# создание сокета, клиент

import socket

# более длинная запись
# sock = socket.socket()
# sock.connect(("127.0.0.1", 10001))
# sock.sendall("ping".encode("utf8"))
# sock.close()

# более короткая запись

# Создаст соединение с сервером
sock = socket.create_connection(("127.0.0.1", 10001))
# Отправит данные на сервер
sock.sendall("ping".encode("utf8"))
# Закроет соединение
sock.close()
