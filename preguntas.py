"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv


def pregunta_01():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
            
        prueba_suma = []
        for row in reader:
            prueba_suma.append(row[1])
        
    suma = 0
    for elemento in prueba_suma:
        suma = int(elemento) + suma
        
    return suma


def pregunta_02():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        recuentos = {"A":0,"B":0,"C":0,"D":0,"E":0}
        for row in reader:
            if row[0] in recuentos:
                recuentos[row[0]] += 1
        tuplas = [(key,value) for key,value in recuentos.items()]
        return tuplas  
#print(pregunta_02())       


def pregunta_03():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        recuentos = {"A":0,"B":0,"C":0,"D":0,"E":0}
        for row in reader:
            if row[0] in recuentos:
                recuentos[row[0]] += int(row[1])
        tuplas = [(key,value) for key,value in recuentos.items()]
        return tuplas
#print(pregunta_03())
    


def pregunta_04():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        meses = {"01":0,
                     "02":0,
                     "03":0,
                     "04":0,
                     "05":0,
                     "06":0,
                     "07":0,
                     "08":0,
                     "09":0,
                     "10":0,
                     "11":0,
                     "12":0,}
        for row in reader:
            mes = row[2].split("-")[1] # 1999-02-28 (1998, 02, 28)
            if mes in meses:
                meses[mes] += 1
        tuplas = [(key,value) for key,value in meses.items()]
        return tuplas
#print(pregunta_04())


def pregunta_05():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        maximos_minimos = {"A":[0,0],"B":[0,0],"C":[0,0],"D":[0,0],"E":[0,0]}
        recuentos = {"A":[],"B":[],"C":[],"D":[],"E":[]}
        for row in reader:
            if row[0] in recuentos:
                recuentos[row[0]].append(int(row[1]))
        for n in maximos_minimos:
            maximos_minimos[n][0], maximos_minimos[n][1] = max(recuentos[n]), min(recuentos[n])
            tuplafinal = [(key, value[0], value[1]) for key, value in maximos_minimos.items()]
            
        return tuplafinal


def pregunta_06():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        secuencias_agrupadas = []
        for row in reader:
            secuencias_agrupadas.append(row[4])
        secuencias_no_agrupadas = []
        for element in secuencias_agrupadas:
            element = element.split(",")
            secuencias_no_agrupadas.extend(element)
        
        maximos_minimos = {
            "aaa":[0,0],
            "bbb":[0,0],
            "ccc":[0,0],
            "ddd":[0,0],
            "eee":[0,0],
            "fff":[0,0],
            "ggg":[0,0],
            "hhh":[0,0],
            "iii":[0,0],
            "jjj":[0,0]
            }
        recuentos = {"aaa":[],"bbb":[],"ccc":[],"ddd":[],"eee":[],"fff":[],"ggg":[],"hhh":[],"iii":[],"jjj":[]}
        desagrupacion = []
        for valor in secuencias_no_agrupadas:
            valor = valor.split(":")
            desagrupacion.append(valor)
        desagrupacion = sorted(desagrupacion, key=lambda x:(x[0],x[1]))
        for elemento in desagrupacion:
            if elemento[0] in recuentos:
                recuentos[elemento[0]].append(int(elemento[1]))
        for n in maximos_minimos:
            maximos_minimos[n][0], maximos_minimos[n][1] = min(recuentos[n]), max(recuentos[n])
            tuplafinal = [(key, value[0], value[1]) for key, value in maximos_minimos.items()]
        return tuplafinal   



def pregunta_07():
   with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        
        tuplas = [(0, []), (1, []), (2, []),
                         (3, []), (4, []), (5, []),
                         (6, []), (7, []), (8, []),
                         (9, [])]
        
        for line in reader:
            letter = line[0]
            n = int(line[1])
            for tuple in tuplas:
                if tuple[0] == n:
                    tuple[1].append(letter)    
                        
        return tuplas


def pregunta_08():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
    
        tuplas = [(0, []), (1, []), (2, []),
                         (3, []), (4, []), (5, []),
                         (6, []), (7, []), (8, []),
                         (9, [])]
        
        for line in reader:
            letter = line[0]
            n = int(line[1])
            for tupla in tuplas:
                if tupla[0] == n and letter not in tupla[1]:
                    tupla[1].append(letter)
                tupla[1].sort()
                
        return tuplas


def pregunta_09():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        conteos = {"aaa":0,"bbb":0,"ccc":0,"ddd":0,"eee":0,"fff":0,"ggg":0,"hhh":0,"iii":0,"jjj":0}
        
        for row in reader:
            columna5 = row[4].split(',')
            for elemento in columna5:
                clave, _ = elemento.split(':')
                if clave in conteos:
                    conteos[clave] += 1
                else:
                    conteos[clave] = 1
    return conteos


def pregunta_10():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")   
        list = []          
        for line in reader:
            letter = line[0]
            column4 = len(line[3].split(","))
            column5 = len(line[4].split(","))
            all_together = (letter, column4, column5)
            list.append(all_together)
        return list


def pregunta_11():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        
        dictionary = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,    
        }
    
        for line in reader:
            column2 = int(line[1])
            letters = line[3].split(",")
            for letter in letters:
                if letter in dictionary:
                    dictionary[letter] += column2
        return dictionary


def pregunta_12():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        
        dictionary = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
                
        }
        
        for line in reader:
            if line[0] in dictionary:
                column5 = line[4].split(",") 
                for element in column5:
                    n = element.split(":") 
                    n = int(n[1])
                    dictionary[line[0]] += n
        return dictionary
