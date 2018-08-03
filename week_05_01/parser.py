str = "ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\neardrum.cpu 20.3 1501864259\n\n"

data = str.split("\n")
data = data[1:-2]
print(data)

parsed = {}

for i in data:
    splitted = i.split()
    key, value, timestamp = splitted[0], splitted[1], splitted[2]
    if key in parsed:
        parsed[key] += [(value, timestamp)]
    else:
        parsed[key] = [(value, timestamp)]

print(parsed)
