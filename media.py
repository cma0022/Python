class Media:
    arrayNotas=[]

    def notas(self):
        return self.arrayNotas

    def add(self, numero):
        if numero >= 0 and numero <= 10:
            self.arrayNotas.append(numero)
        else:
            raise ValueError

        
    def media(self):
        suma = 0
        for i in self.arrayNotas:
            suma = suma + i
        return suma/len(self.arrayNotas)