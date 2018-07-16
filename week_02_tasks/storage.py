import json
import os
import tempfile
import argparse


def Main():

    # Ключи и значения
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", action="store",
                        dest="key",
                        help="Ключ",
                        type=str)
    parser.add_argument("--val", action="append",
                        dest="values",
                        default=[],
                        help="Значения",
                        nargs="*",
                        type=str)
    args = parser.parse_args()

    # JSON-файл, в котором будем данные
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    # Проверяем передан ли команде ключ и значения. Если да — пишем их в файл
    if args.key and args.values:

        data_key = args.key
        data_values = ' '.join(args.values[0])

        # Проверяем есть ли файл, загружаем его
        if os.path.exists(storage_path) and os.path.getsize(storage_path) > 0:
            with open(storage_path, "r") as f:
                data = json.load(f)
        else:
            data = {}

        # Собираем данные
        if data_key in data:
            data[data_key] = data[data_key] + ', ' + data_values
        else:
            data[data_key] = data_values

        with open(storage_path, "w") as f:
            json.dump(data, f)

    else:
        data_key = args.key
        if os.path.exists(storage_path) and os.path.getsize(storage_path) > 0:
            with open(storage_path, "r") as f:
                data = json.load(f)
                if data_key in data:
                    print(data[data_key])
                else:
                    print(None)
        else:
            print(None)


if __name__ == '__main__':
    Main()
