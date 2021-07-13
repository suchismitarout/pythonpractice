class SingleTon:
    __shared_state = None

    def __init__(self):
        if SingleTon.__shared_state is None:
            SingleTon.__shared_state = self
        else:
            raise Exception("you cant create another class")

    def get_instance(self):
        if not SingleTon.__shared_state:
            return SingleTon()
        return SingleTon.__shared_state


sg = SingleTon()
print(sg)
print(sg.get_instance())
k = sg.get_instance()
print(k)