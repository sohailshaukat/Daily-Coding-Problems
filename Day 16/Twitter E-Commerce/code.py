class Logs:

    def __init__(self):
        self.list = []

    def record(self, order_id):
        self.list.append(order_id)
        
    def get_last(self, index):
        return self.list[-1*index]

logs = Logs()
logs.record("Order_Id1")
logs.record("Order_Id2")
logs.record("Order_Id3")
logs.record("Order_Id4")
logs.record("Order_Id5")

print(logs.list)

print(logs.get_last(2))