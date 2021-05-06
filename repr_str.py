class IPadress():
    def __init__(self,ip,proc):
        self.ip=ip
        self.proc=proc
    def __str__(self):
        return f'IPAdress: {self.ip} {self.proc}'
    def __repr__(self):
        return f'IPAdress: {self.ip} {self.proc}'
ip1=IPadress('10.1.1','Intel Core 5')
ip2=IPadress('10.2.2','Intel Core 3')
ipadress=[ip1,ip2]
# print(ipadress)
x=repr(ipadress)
print(x)