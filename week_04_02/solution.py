class Value:
    def __init__(self):
        self.amount = None

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, amount):
        self.amount = amount * (1 - obj.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
