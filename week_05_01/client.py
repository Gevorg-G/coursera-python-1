# https://www.coursera.org/learn/diving-in-python/programming/aG3x3/kliient-dlia-otpravki-mietrik
# https://d3c33hcgiwev3.cloudfront.net/_0c1c1bede648463ed60e3bd2e67db919_W5.pdf?Expires=1532563200&Signature=WwfFJHOpUta8eVr95LyoaVrVY56X09a3V2dihC5usqXxcrU7ptWcgVmoO9OnxWgSTTDyqKLBxdrnPfIKQAi3eqwJoMpp8Q-jU4hxhbS7Q2eu4nJlNNuqAW1r7Rn1Cu4be9l5-4mCGztGj0-203JoaXwCEOXVYxAUHnfYWdGo4pI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

import asyncio
# import time


class Client:
    """Клиент для записи и чтения данных"""

    def __init__(self, addr, port, timeout):
        self.addr = addr
        self.port = port
        self.timeout = timeout

    async def put(self, key, value, timestamp):
        """Метод для записи данных"""

        reader, writer = await asyncio.open_connection(self.addr, self.port)

        print(f"key: {key}, value: {value}, timestamp: {timestamp}")
        try:
            writer.write(key.encode())
            writer.write(value.encode())
            writer.write(timestamp.encode())
        except:
            raise ClientError("не могу отправить данные")
        finally:
            writer.close()

    def get(self):
        """Метод для чтения данных"""
        pass


class ClientError(Exception):
    """Ошибка"""
    pass
    # def __init__(self, text=""):
    #     self.text = text


client = Client("127.0.0.1", 10001, 2)

loop = asyncio.get_event_loop()
loop.run_until_complete(client.put("key", "value", "timestamp"))
loop.close()
