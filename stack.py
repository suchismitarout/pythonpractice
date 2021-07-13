class Stack():
    def __init__(self):
        self.st = []

    def is_empty(self):
        return self.st == []

    def get_size(self):
        return len(self.st)

    def push(self, data_):
        self.st.append(data_)

    def pop(self):
        if len(self.st) == 0:
            return
        return self.st.pop()



