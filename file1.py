import random


class Hack:

    def __init__(self, n = 3):
        self.n = 3
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
            
a = Hack()
password = a.password()
print(a.hacking(password))
