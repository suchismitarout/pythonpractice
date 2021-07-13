class SingleTon:
    __shared_state = None

    def __init__(self):
        if SingleTon.__shared_state is None:
            SingleTon.__shared_state = self
        else:
            raise Exception("object is already created")

    def get_instance(self):
        if not SingleTon.__shared_state:
            return SingleTon()
        return SingleTon.__shared_state
s = SingleTon()
print(s.get_instance())
print(s.get_instance())

