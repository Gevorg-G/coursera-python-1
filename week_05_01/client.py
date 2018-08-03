# https://www.coursera.org/learn/diving-in-python/programming/aG3x3/kliient-dlia-otpravki-mietrik


import socket
import time


class ClientError(Exception):
    """Ошибка"""
    print("Ошибка")


class Client:
    """Клиент для записи и чтения данных"""

    def __init__(self, addr, port, timeout=None):
        self.addr = addr
        self.port = port
        self.timeout = timeout

    def put(self, key, value, timestamp=None):
        """Метод для записи данных"""
        with socket.create_connection((self.addr, self.port), self.timeout) as sock:
            # Преобразовываем значения в строки
            if timestamp is None:
                timestamp = int(time.time())
            timestamp = str(timestamp) + "\n"
            value = str(value)

            # Формируем строку и отправляем её
            send_data = ' '.join(["put", key, value, timestamp])
            try:
                sock.sendall(send_data.encode("utf8"))
            except:
                raise ClientError

            # Получаем ответ от сервера
            recieved_data = b""
            while not recieved_data.endswith(b"\n\n"):
                try:
                    recieved_data += sock.recv(1024)
                except socket.timeout:
                    raise ClientError

            if recieved_data.decode("utf8") == "ok\n\n":
                print("Everything is ok")
            if recieved_data.decode("utf8") == "error\nwrong command\n\n":
                print("Something broken")

    def get(self, key):
        """Метод для чтения данных"""
        with socket.create_connection((self.addr, self.port), self.timeout) as sock:
            key += "\n"
            send_data = ' '.join(["get", key])
            sock.sendall(send_data.encode("utf8"))

            recieved_data = b""

            while not recieved_data.endswith(b"\n\n"):
                try:
                    recieved_data += sock.recv(1024)
                    print(recieved_data.decode("utf8"))
                except:
                    raise ClientError

            if recieved_data.decode("utf8") == "ok\n\n":
                return {}
            elif recieved_data.decode("utf8") == "error\nwrong command\n\n":
                raise ClientError
            else:
                return self.parser(recieved_data)

    def parser(self, recieved_data):
        data = {}

        unparsed_data = recieved_data.decode("utf8").split("\n")
        unparsed_data = unparsed_data[1:-2]

        for i in unparsed_data:
            parsed_data = i.split(" ")
            key, value, timestamp = parsed_data[0], float(
                parsed_data[1]), int(parsed_data[2])

            if key in data:
                data[key] += [(timestamp, value)]
            else:
                data[key] = [(timestamp, value)]

        return data
