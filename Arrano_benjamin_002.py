def eliminar(id_e,lista):
    for p in lista:
        if id_e==[0]:
            lista.remove(p)
            print("equipo eliminado correctamente ")


cant=0
acum=0
prom=0
lista=[]
while True:
    print("")
    print("-.-.-.-.-.-.-.-.- M E N U   T O R N E O  B A S K E T B A L L -.-.-.-.-.-.-.-")
    print("1.- agregar equipo ")
    print("2.- listar equipo ")
    print("3.- actualizar equipo por id ")
    print("4.- generar BBDD ")
    print("5.- cargar BBDD ")
    print("6.- estadisticas ")
    print("0.- salir ")
    print("")
    op=int(input("ingrese una opcion : "))

    if op==1:
        print("")
        print("-.-.-.- A G R E G A R   E Q U I P O -.-.-.-")
        print("")
        print("equipos agregados correctamente")

        id=int(input("ingrese id(NUMEROS) : "))
        nombre=input("ingrese nombre : ")
        puntos=int(input("ingrese puntos obtenidos : "))
        categoria=[id,nombre,puntos]
        lista.append(categoria)
        print("categoria agregada correctamente")
        print("")



    elif op==2:
        print("")
        print("-.-.- L I S T A R   E Q U I P O -.-.-")
        print("")
        for p in lista:
            print(f"id:{p[0]}nombre :{p[1]}puntos :{p[2]}")
            print("")


    elif op==3:
        encontrado=false
        print("")
        print("-.-.- A C T U A L I Z A R  E Q U I P O  P O R  I D -.-.-")
        print("")


    elif op==4:
        print("")
        print("-.-.- G E N E R A R  B A S E  D E  D A T O S -.-.-")
        print("")
        with open("bbdd_categoria.csv'w',newline=")as bbdd_producto:
            escritorio_csv=csv.writerow([id],"nombre",puntos)
            escritorio_csv.writerows(lista)
            print("")
            print("archivo generado correctamente")


    elif op==5:
        print("")
        print("-.-.- C A R G A R  B A S E  D E  D A T O S -.-.-.")
        print("")
        listita.clear()
        cont=0
        with open("bbdd_categoria.csv','r',newline=")as bbdd_categoria:
            lector_csv = csv.reader(bbdd_categoria)
            for fila in lector_csv:
                if cont==0:
                    cont+=1
                    continue
                    i=int(fila[0])
                    n=(fila[1])
                    p=int(fila[2])
                    listita_chica=[i,n,p]
                    listita.append(listita_chica)
                    lista.pop(0)


    elif op==6:
        acum=0
        print("")
        print("-.-.-. E S T A D I S T I C A S -.-.-")
        print("")
        cant=len(lista)
        id cant=0:
            for p in lista:
                acum=acum+p[2]
                prom=acum/categoria
                print("puntos:",cant)
                print("puntos:",acum)
                print("puntos:",prom)

    else:
         print("no hay puntaje agregado....")

    elif op==0:
         print("")
         print("hasta luegoooooo")
         break

    else:
        print("")
        print("ingrese una opcion valida")
        print("")

                




                    



        



















