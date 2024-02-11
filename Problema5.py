#%%
class Alumno:
    notas =[]
    def __init__(self, nombre, num_reg, age, notas=[]):
        self.nombre = nombre 
        self.num_reg = num_reg
        self.age = age
        self.notas = notas

    def display(self):
        return '{} ({})'.format(self.nombre, self.num_reg)
        
    
    
    def setage(self):
        return '{} ({})'.format(self.nombre, self.age)
    
#%%
    def agregarnota(self, p):
        p =[]
        cant = str(input("¿Cuantas notas quiere agregar?"))
        for cant in range(0,cant):
            while cant < cant:
                
                self.notas.append(p)

#%%     

    def setnotas(self):
         return '{} ({})'.format(self.nombre, self.notas)

#%%
classmate = Alumno(input("Ingresa nombre del alumno: "), input("Ingresa numero de registro del alumno: "), input("Ingresa edad edad del alumno:"))
classmate.display()
#%%
classmate.setage()



    
#%%

    

    

  



