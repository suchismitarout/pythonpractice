class SingleTon:
    __sharedinstance = None

    def __init__(self):
        if SingleTon.__sharedinstance is None:
            SingleTon.__sharedinstance = self
        else:
            raise Exception("you can't create class")

    def get_instance(self):
        if not SingleTon.__sharedinstance:
            return SingleTon()
        else:
            return SingleTon.__sharedinstance
