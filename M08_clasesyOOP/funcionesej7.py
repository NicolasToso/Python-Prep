class funcion():
    def __init__(self):
        pass

    def es_primo(n):
        flag = [1 for i in range(1,n) if n%i==0]
        if len(flag) > 1:
            return False
        else:
            return True
        
    def temp_converter(val, origin_unit, convert_unit):
        def c_to_k(c):
            return((c+273.15))
        def k_to_c(k):
            return(k-273.15)
        def c_to_f(c):
            return(((c*9)/5)+32)
        def f_to_c(f):
            return(((f-32)*5)/9)
        def k_to_f(k):
            return(c_to_f(k_to_c(k)))
        def f_to_k(f):
            return(c_to_k(f_to_c(f)))
        int(val)
        if origin_unit.lower() == "c":
            if convert_unit.lower() == "k":
                return f"{c_to_k(val)} K"
            elif convert_unit.lower() == "f":
                return f"{c_to_f(val)} F"
            else:
                return ("Invalid destination unit")
        elif origin_unit.lower() == "k":
            if convert_unit.lower() == "c":
                return f"{k_to_c(val)} C"
            elif convert_unit.lower() == "f":
                return f"{k_to_f(val)} F"
            else:
                return ("Invalid destination unit")
        elif origin_unit.lower() == "f":
            if convert_unit.lower() == "c":
                return f"{f_to_c(val)} C"
            elif convert_unit.lower() == "k":
                return f"{f_to_k(val)} K"
            else:
                return ("Invalid destination unit")
        else:
            return ("Invalid origin unit")
        
    def contador_repetidos(lista_numeros):
        counter=[]
        if lista_numeros==[]:
            return None,None
        else:
            for numero in lista_numeros:
                counter.append(lista_numeros.count(numero))
            repetido=lista_numeros[counter.index(max(counter))]
            return repetido, max(counter)   