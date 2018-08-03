# По итогам ревью решения от сервера пришёл к выводу,
# что моё решение совсем неоптимизировано
# плюс в моём варианте данные не сортируются по timestamp,
# но в грейдере это проигнорировано, поэтому тест я прошёл

import asyncio
stored_data = {}


class ClientServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        print("Получено от клиента: ", data.decode(), "\n")
        resp = self.process_data(data.decode())
        print("Ответ серверу: ", resp)
        self.transport.write(resp.encode())

    def process_data(self, data):
        print(id(self))
        # Делим строчку, чтобы провести действия
        data_splitted = data.split(" ")
        print("Разделённые данные: ", data_splitted, "\n")

        # Запрос соответствует команде Put
        if data_splitted[0] == "put" and len(data_splitted) == 4:
            print("Обрабатываем команду put")
            key, value, timestamp = data_splitted[1:]
            print("Key: ", key, " Value: ", value, " Timestamp: ", timestamp)
            if self.is_float(value) and self.is_integer(timestamp[:-1]):
                print("Данные подходят, идём дальше")
                print(key in stored_data.keys())
                #import pdb
                # pdb.set_trace()
                if key not in stored_data:
                    print("Ключа нет, создаём")
                    stored_data[key] = []
                    stored_data[key].append([timestamp[:-1], value])
                    print("Новый ключ добавлен: ", stored_data)
                elif key in stored_data:
                    print("Stored: ", stored_data)
                    duplicate = 0
                    for elements in stored_data[key]:
                        print("Element 0: ",
                              elements[0], "Element 1: ", elements[1])
                        print("Timestamp: ", timestamp)
                        if elements[0] == timestamp[:-1]:
                            print("Duplicate! ", key, " ",
                                  timestamp, " ", value)
                            elements[1] = value
                            duplicate = 1
                            break
                    if duplicate == 0:
                        stored_data[key].append([timestamp[:-1], value])
                print("Сохранено: ", stored_data)
            return ("ok\n\n")

        # Запрос соответствует команде Get
        if data_splitted[0] == "get" and len(data_splitted) == 2:
            print("Обрабатываем команду get")
            key = data_splitted[1][:-1]
            print("Ключ: ", key)
            if key == "*":
                data_to_send = "ok\n"
                for keys in stored_data:
                    for elements in stored_data[keys]:
                        data_to_send += keys + " " + \
                            elements[1] + " " + elements[0] + "\n"
            elif key in stored_data:
                data_to_send = "ok\n"
                for elements in stored_data[key]:
                    data_to_send += key + " " + \
                        elements[1] + " " + elements[0] + "\n"
            elif key not in stored_data:
                return ("ok\n\n")
            print("To send before: ", data_to_send)
            data_to_send = data_to_send + "\n"
            print("To send:", data_to_send)
            return data_to_send
        return ("error\nwrong command\n\n")

    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except:
            return False

    @staticmethod
    def is_integer(value):
        try:
            int(value)
            return True
        except:
            return False


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    print("########## НАЧАЛО! ##########")
    run_server("127.0.0.1", 8888)
