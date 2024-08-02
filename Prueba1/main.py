from input import text

def main():

    #Se pide al usuario que ingrese la palabra clave
    keyword = str(input('Ingrese la palabra clave: '))

    words_from_text = []
    #Se normaliza la palabra keyword para que no haya diferencia entre mayusculas y minusculas ni tildes
    keyword_normalized = normalize_words(keyword)

    #Envio la lista vacia de palabras, a la función para que se le añadan las palabras del texto
    letters_into_words_from_text(words_from_text)
    #print(words_from_text)

    #Envio la lista de palabras y la palabra keyword normalizada, a la función para que cuente cuantas veces se repite la palabra keyword en la lista de palabras
    count = count_word_in_text(words_from_text, keyword_normalized)

    print(f'{count} ocurrencias encontradas. Keyword: {keyword}')

def normalize_words(word):
    word_normalized = ''
    for letter in word:
        if letter == 'á':
            letter = 'a'
        if letter == 'é':
            letter = 'e'
        if letter == 'í':
            letter = 'i'
        if letter == 'ó':
            letter = 'o'
        if letter == 'ú':
            letter = 'u'
        if letter == 'Á':
            letter = 'A'
        if letter == 'É':
            letter = 'E'
        if letter == 'Í':
            letter = 'I'
        if letter == 'Ó':
            letter = 'O'
        if letter == 'Ú':
            letter = 'U'
        #Se puede poner en minusculas las letras mayusculas, pero se necesita una gran cantidad de codigo, por eso opté por usar lower()
        """ if letter == 'A':
            letter = 'a'
        if letter == 'B':
            letter = 'b'
        if letter == 'C':
            letter = 'c' """
        
        word_normalized += letter

    word_normalized = word_normalized.lower()
    return word_normalized

def letters_into_words_from_text(words_from_text):
    #Se inicia una variable word, donde despues se le concatenan las letras de la variable text
    word = ''

    #Guardo cada letra a la variable word, pero solo la añade a la lista si despues de la letra hay un delimitador
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
            #Se normalizan las palabras para que no haya diferencia entre mayusculas y minusculas ni tildes
            word = normalize_words(word)
            if word:
                words_from_text.append(word)
            word = ''

    #Se agrega la ultima palabra a la lista de palabras despues de salir del ciclo for, la ultima palabra no se agrega a la lista en el bucle y queda guardada en la variable word ya que en caso de que despues de la
    #ultima palabra, no haya ningun delimitador, no entraría en el condicional que reinicia la variable "word"
    if word:
        word = normalize_words(word)
        words_from_text.append(word)

def count_word_in_text(words_from_text, keyword_normalized):
    #Se inicia un contador en 0 para añadirle las veces que se encuentra la palabra keyword en la lista de palabras
    count = 0
    for word in words_from_text:
        if word == keyword_normalized:
            count += 1
    return count

if __name__ == '__main__':
    main()

