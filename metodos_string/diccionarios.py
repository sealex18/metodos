""" dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())
 """
 
estudiante={
    'id':123,
    'nombre': 'andrea',
    'asignatura': ["BD","web2"]
}
estudiante['celular']='323456789'
#estudiante['nombre']='andres'
#print(estudiante)

for key in estudiante.items():
    print (key[0],":",key[1])
    