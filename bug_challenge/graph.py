class DataHolder:
    def __init__(self):
        self.data = [0]*10

    def add_data(self, index, value):
        self.data[index] = value

    def remove_data(self, index):
        self.data.pop(index)

holder = DataHolder()
holder.add_data(5, 20)
holder.remove_data(5)
output = holder.data[5]

print(output)


