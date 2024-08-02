from input import text, keyword

def main():

    words_from_text = []

    #Se inicia una variable word, donde despues se le concatenan las letras de la variable text
    word = ''
    for letter in text:
        #Se inicia una variable skip en False, la cual se vuelve True, cuando la letra que se esta leyendo es un espacio, punto, coma, punto y coma o dos puntos
        #Esto para saber cuando se completa una palabra y se debe agregar a la lista de palabras
        skip = False
        if letter == ' ' or letter == '.' or letter == ',' or letter == ';' or letter == ':':
            skip = True
        #Sí la letra no es un espacio, punto, coma, punto y coma o dos puntos, se le concatena a la variable word
        if skip == False:
            word += letter
        #Si la letra si lo es, se agrega la palabra a la lista de palabras y se reinicia la variable word para seguir con la siguiente palabra
        if skip == True:
            words_from_text.append(word)
            word = ''

    #Se inicia un contador en 0 para añadirle las veces que se encuentra la palabra keyword en la lista de palabras
    count = 0
    for word in words_from_text:
        #Se eliminan los espacios que se hayan guardado en la lista de palabras
        if word == '':
            words_from_text.remove(word)
        if word == keyword:
            count += 1

    print(f'La palabra "{keyword}" se repite {count} veces en el texto.')

if __name__ == '__main__':
    main()

