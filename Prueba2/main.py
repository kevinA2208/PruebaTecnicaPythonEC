from input import data, criteria1

def main():

    #Copia de la lista "data", para despues eliminar los registros que ya se hayan filtrado por las criterias y añadirlos al final de la lista ordenada
    data_copy = data.copy()
    #Lista de data que cumple con los criterios
    data_by_criteria = []
    #Lista de data (anteriormente ordenada por criterios), ordenada por prioridad de mayor a menor
    data_ordered_by_priority = []
    
    #Envio la lista vacia data_by_criteria para que se le añadan los registros que cumplan con los criterios
    #Y la lista data_copy para que se le eliminen los registros que ya se hayan filtrado por los criterios, para que solo cuente con los registros NO filtrados por criterio y añadirlos al final.
    order_data_by_criteria(data_by_criteria, data_copy)


    #Envio la lista de registros filtrados por criterio y la lista vacia data_ordered_by_priority 
    #para que se añadan los registros previamente ordenados por criterio y por prioridad de mayor a menor
    order_data_by_priority(data_by_criteria, data_ordered_by_priority)

    #Se añaden los registros que no cumplieron con los criterios al final de la lista ordenada       
    data_ordered_by_priority.extend(data_copy)

    #Se imprime la lista ordenada, donde los primeros registros son los que fueron filtrados por los criterios ingresados, y ademas, ordenados por el campo
    #"priority", de mayor a menor, el resto de registros son los que no fueron filtrados por criterio, se añaden al final de la lista.
    #En caso de que ningun registro cumpla con los criterios ingresados, se muestran todos los registros sin ordenar.
    print(data_ordered_by_priority)

#Ordenar la lista de datos por criterio
def order_data_by_criteria(data_by_criteria, data_copy):

    
    #Por cada registro en data
    for i in data:

        validation = True

        #Por cada criterio en criteria1
        for field, operation, value in criteria1:

            #Según la operación que esté en el criterio, se evalúa que NO se cumpla dicho criterio, comparando los valores del registro con el valor del criterio según el campo que se escoge
            #Si el criterio NO se cumple se cambia la variable de validación a False para que no se añada a la lista de data_by_criteria
            #Esto se hace por cada criterio, si NO cumple con alguno, no se añade a la lista, esto lo hice para que se puedan añadir mas de un criterio, ya que previamente habia probado solo con uno.
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
        #Esto se hace para que al final de la lista ordenada se añadan los registros que NO cumplieron con los criterios
        if validation:
            data_by_criteria.append(i)
            data_copy.remove(i)

#Ordenar cada registro previamente ordenado por criterio, por prioridad de mayor a menor
def order_data_by_priority(data_by_criteria, data_ordered_by_priority):

    #Por cada registro que se haya filtrado por los criterios
    for i in data_by_criteria:

        #Se inicializa una variable en False para despues validar si el registro tiene una prioridad mayor a los registros ya ordenados o menor
        high_priority = False

        #Se iteran por cada indice de la lista ordenada
        #(Si la lista está vacia, no entra al for y high_priority se mantiene en False por lo que se agrega "i" como primer objeto de la lista ordenada)
        for j in range(len(data_ordered_by_priority)):
            
            #Si la prioridad del registro actual es mayor a la prioridad del registro en la posición j de la lista ordenada
            if i['priority'] > data_ordered_by_priority[j]['priority']:
                
                #Se inserta el registro en la posición j de la lista ordenada, quedando por delante de los registros con menor prioridad incluyendo el de la posicion "j"
                #Se puede usar el .insert() en vez de hacer un slice de la lista y agregar el registro en la posición j
                data_ordered_by_priority[j:j] = [i]

                #Se cambia la variable high_priority a True para no agregar el registro al final de la lista ordenada
                high_priority = True
                #Se termina el ciclo
                break
        
        #Si high_priority es False (Osea, si la prioridad del registro actual es menor a la prioridad de todos los registros ya ordenados o si la lista ordenada está vacía)
        #Se agrega el registro al final de la lista ordenada
        if high_priority == False:
            data_ordered_by_priority.append(i)


if __name__ == '__main__':
    main()

