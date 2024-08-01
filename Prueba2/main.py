from input import data, criteria1

def main():

    #Copia de la lista "data", para despues eliminar los registros que ya se hayan filtrado por las criterias y añadirlos al final de la lista ordenada
    data_copy = data.copy()
    #Lista de data que cumple con los criterios
    data_by_criteria = []
    
    #Ordenar la lista de datos por criterio
    #Por cada registro en data
    for i in data:

        validation = True

        #Por cada criterio en criteria1
        for field, operation, value in criteria1:

            #Según la operación que esté en el criterio, se evalúa que NO se cumpla dicho criterio, comparando los valores del registro con el valor del criterio según el campo que se escoge
            #Si el criterio NO se cumple se cambia la variable de validación a False para que no se añada a la lista de data_by_criteria
            #Esto se hace por cada criterio, si NO cumple con alguno, no se añade a la lista
            if operation == '=' and i[field] != value:
                validation = False
            if operation == '>' and i[field] <= value:
                validation = False
            if operation == '<' and i[field] >= value:
                validation = False
            if operation == '>=' and i[field] < value:
                validation = False
            if operation == '<=' and i[field] > value:
                validation = False
            if operation == '!=' and i[field] == value:
                validation = False
            

        #Si la variable validation sigue True, quiere decir que el registro cumple con todos los criterios, por lo que se añade a la lista de data_by_criteria y se elimina de la lista data_copy
        #Esto se hace para que al final de la lista ordenada se añadan los registros que cumplieron con los criterios
        if validation:
            data_by_criteria.append(i)
            data_copy.remove(i)

    print(data_by_criteria)

if __name__ == '__main__':
    main()

