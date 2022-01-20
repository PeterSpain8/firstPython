print ("Bienvenido a Napole Pizza")
print ("Porfavor, elige sus ingridientes Pizza")
#Variables veg
#b=Pimiento
#c=Tofu
#Variables no vegetariano
#d= Peperoni
#i= Jamon
#f=Salmon
#g= Mozarella
#h= Tomate
print("Ingridientes Veganos: Pimiento y Tofu ")
print("Ingridientes Carniboros: Peperoni,Jamon, Salmon ")

b = int(input('Pimiento? (1- SI, 0 - NO) : '))
c = int(input('Tofu? (1- SI, 0 - NO) : '))
d = int(input('Peperoni? (1- SI, 0 - NO) : '))
i = int(input('Jamon? (1- SI, 0 - NO) : '))
f = int(input('Salmon? (1- SI, 0 - NO) : '))
g = "Mozarella"
h = "Tomate"
if (d==0 and i==0 and f==0): 
    print ("Usted elegido pizza vegetariana")
else:
    print("Usted eligido pizza carnibora")
    print ("Ingridientes elegidos:")
    print (g,h)
if b==1 :
    print("Pimiento")
if c==1:
    print("Tofu")
if d==1:
    print("Peperoni")
if i==1:
    print ("Jamon")
if  f==1:
    print("Salmon")
if (b>1 or c>1 or d>1 or i>1 or f>1 ):
    print("Datos erroneos")
