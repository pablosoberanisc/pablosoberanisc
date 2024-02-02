class Colacircular:
    cola=[]

    def tam(self, tamaño_de_cola):
        if len(self.cola)==tamaño_de_cola:
            print("cola esta llena")

        else:
            dato= input("Ingrese el dato: ")
            self.cola.append(dato)

    def vacia(self):
        if len(self.cola) == 0:
            print("cola esta vacia")

        else:
            pdta= self.cola.pop(0)
            print("El dato es", pdta)
            
    def mostrar(self):
        if len(self.cola) == 0:
            print("cola esta vacia. ")
        else:
            print("Datos de la cola son ")
            for i in self.cola:
                print(i)

if __name__=='__main__':
    obj = Colacircular()

    tamaño_de_cola = int (input("Ingresa el tamaño de la cola: "))

    while True:
        opcion = input("1. Ingresa dato:\n2. Devolver dato:\n3. Mostrar la cola:\n4. Salir:")
        if opcion=="1":
            obj.tam(tamaño_de_cola)
        
        elif opcion =="2":
            obj.vacia()

        elif opcion =="3":
            obj.mostrar()

        elif opcion =="4":
            exit()
        
        else:
            print("Ingresa una valida")