ls_programas = []

import os 
sw = True
def fnt_agregar(p):
    global ls_programas
    if p == '':
        enter = input('Debe ingrear un programa >ENTER<')
    else:
        ls_programas.append(p)
        enter = input(f'El programa {p} ha sido registrado con éxito >ENTER<')
def fnt_seleccion(op):
    if op == '1':
        program = input('Ingrese el nombre del programa ')
        fnt_agregar(program)
    elif op == '2':
        if len(ls_programas) >0:
            fnt_mostrar()
        else:
            enter = input('\nNo se encontraron registros >ENTER<')
    elif op == '3':
        fnt_eliminar()
    elif op =='4':
        print(ls_programas)
        pos = input('\nIngrese la posicion del programa a eliminar')
        fnt_eliminarP(pos)

def fnt_mostrar():
    print(ls_programas)
    enter = input('\n>ENTER<')

def fnt_eliminar():
    ls_programas.pop()
    enter = input('\nPrograma eliminado con éxito >ENTER<')

def fnt_eliminarP(pos):
    tamaño = len(ls_programas)
    if len(ls_programas) >0:
        if tamaño > int(pos):
            ls_programas.pop(int(pos))
        enter = input('\nPrograma eliminado con éxito >ENTER<')
    else:
        enter = input('\nPosición no valida >ENTER<')
while sw == True:
    os.system('cls')


    var_opcion = input('>>>MENU<<< \n1. AGREGRAR\n2. MOSTRAR\n3. ELIMINAR PROGRAMA X ORDEN\n4. ELIMINACIÓN POR POSICIÓN\n-> ')
    fnt_seleccion(var_opcion)