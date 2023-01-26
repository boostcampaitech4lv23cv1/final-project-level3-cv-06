from a_pack.a_module import AA

class BB:
    def __init__(self):
        self.__aa = AA()
        print('classBB')
    
    def print(self):
        print('classBB.print()')