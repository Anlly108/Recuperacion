import json

print ("USUARIO\n")

print("--------------------")
print("* MENU DE OPCIONES*")
print("--------------------")

print("1. REGISTRO DE USUARIO")
print("2. INGRESO DE USUARIO Y CONTRASEÑA")


numero = int(input("Introduce la opción deseada:"))

if numero == 1:
    data=[]
    
    correo = input("Ingresa correo: ")                           
    contraseña1 = input("Ingresa la contraseña: ")  
    contraseña2 = input("Repite la contraseña: ")      
    nombre = input("Ingresa nombre: ")  
    apellido = input("Ingresa apellido: ")  
    cedula = input("Ingresa cedula: ")  
        
    if contraseña1 == contraseña2 :
        print("Se registro correctamente")
    else: 
        print("La contraseña son diferente, por favor intente de nuevo")
            
            
    data['usuario']= []
    data = ['usuario'].append({                                             
        "correo": correo,                                         
        "contraseña": contraseña1,
        "nombre": nombre,
        "apellido": apellido,
        "cedula": cedula})
                               
    with open('usuario.json', 'w') as file:   
        json.dump(data,file, indent=2)      

if numero == 2:
    data=[]
    
    correo = input("Ingresa correo: ")                           
    contraseña1 = input("Ingresa la contraseña: ")  
    
    data = ['usuario'].append({                                             
        "correo": correocom,                                         
        "contraseña": contraseñacom})
        
    if correo == correocom :
        if contraseña1 == contraseñacom :
            print ("Se inicio sesion correctamente")
            with open ("usuario.json", "r") as file:
                data = json.load(file)
                print(data)
        else:
            print("Error")
            
elif numero >2:
    print("Error al seleccionar una opcion")
