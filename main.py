class Actor():
    def __init__(self, name, amplua, rost):
        self.rost = rost
        self.name = name
        self.amplua = amplua
        self.count = 0
    def info(self):
        return 'Actor ' + self.name + self.amplua
    def joke(self):
        if self.count == 0:
                self.count = 1
                return 'неудачная'
        else:
            self.count = 0
            return 'удачная'
def buffenoory(self, size):
        if size > self.rost:
            return "влез"
        else:
            return "не влез"
    def change_amplua(self, value, register):
        amplua = self.amplua
            if register == 'up':
                amplua = amplua.upper()
            return amplua.upper()
        elif register == 'low':
            amplua = amplua.lower()
            return amplua.lower()
A = Actor('Pulcinella ', 'stupid servant ', 160)
print(A.info())
print(A.joke())
print(A.joke())
print(A.joke())
print(A.buffenoory(161))
A.change_amplua('smart servant', 'up')
print(A.info())