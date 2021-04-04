import random


class Hack:

    def __init__(self, n = 3):
        self.n = n
        self.alpha = '12345'


    def password(self) -> str:
        password = ''
        for i in range(self.n):
            char = random.choice(self.alpha)
            password += char
        return password
    
        
    def hacking(self, password) -> int:
        new_pass = ''
        counter = 0
        for i in range(len(self.alpha)):
            for j in range(len(self.alpha)):
                for k in range(len(self.alpha)):
                    new_pass = self.alpha[i] + self.alpha[j] + self.alpha[k]
                    counter += 1
                    if new_pass == password:
                        return counter

                    
    def hack_uni(self, password = '111') -> int:
        pat = ''
        for i in range(len(password)):
            pat += '0'
        return pat
            
            
a = Hack()
password = a.password()
print(a.hacking(password))
print(a.hack_uni(password))
b = Hack(10)
pass_2 = b.password()
print(pass_2)
print(b.hack_uni(pass_2))
