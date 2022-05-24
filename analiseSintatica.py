import re

def analiseLexica():
    f = open("calculadoraBasica.c", "r") #Abre o arquivo para leitura
    lines = f.readlines()

    tokens = {}
    qtdLines = 1
    pilhaDelimitadoresC = [] #pilha delimitadores chaves
    pilhaDelimitadoresP = [] #pilha delimitadores parenteses

    for line in lines:
        line = re.sub(r"{", " { ", line)
        line = re.sub(r";", " ;", line)
        line = re.sub(r",", " , ", line)
        line = re.sub(r"[ ]{0,}\(", " ( ", line)
        line = re.sub(r"[ ]{0,}\)", " ) ", line)
        line = re.sub(r"\|\|", " || ", line)
        line = re.sub(r"&&", " && ", line)
        line = re.sub(r"=", " = ", line)
        line = re.sub(r"[^.h]>", " > ", line)
        line = re.sub(r"<[^A-Za-z]", " < ", line)
        line = re.sub(r"!", " ! ", line)
        line = re.sub(r"=[ ]{0,}=", " == ", line)
        line = re.sub(r">[ ]{0,}=", " >= ", line)
        line = re.sub(r"<[ ]{0,}=", " <= ", line)
        line = re.sub(r"![ ]{0,}=", " != ", line)
        line = re.sub(r"[ ]{2,}", " ", line)
        #print(line)
        if line.strip() != '':
            line = line.strip()

            if re.search(r"^#include <.*[.]h>$", line):
                line = line.split()
                tokens[line[0]] = "Palavra reservada"
                biblioteca = re.sub(r"(<|>)","", line[1])
                tokens[biblioteca] = "Biblioteca"
            elif re.search(r"^int main\(\)( {|)$", line):
                line = line.split()
                tokens[line[0]] = "Palavra reservada"
                tokens[line[1]] = "Palavra reservada"
                if len(line) == 3:
                    tokens[line[2]] = "Delimitador de início"
            elif line == "{":
                tokens[line] = "Delimitador de início"
                pilhaDelimitadoresC.append(qtdLines)
            elif line == "}":
                tokens[line] = "Delimitador de fim"
                if len(pilhaDelimitadoresC) > 0:
                    pilhaDelimitadoresC.pop()
                else:
                    print("Delimitador de fim '}' a mais na linha " + str(qtdLines))
                    return
            else:
                aux = line
                line = line.split()
                for i in line:
                    if i == "int" or i == "return" or i == "if":
                        tokens[i] = "Palavra reservada"
                    elif i == "{" or i == "(":
                        tokens[i] = "Delimitador de início"
                        if i == "{":
                            pilhaDelimitadoresC.append(qtdLines)
                        elif i == "(":
                            pilhaDelimitadoresP.append(qtdLines)
                    elif i == "}" or i == ")":
                        tokens[i] = "Delimitador de fim"
                        if i == '}' and len(pilhaDelimitadoresC) > 0:
                            pilhaDelimitadoresC.pop()
                        elif i == ")" and len(pilhaDelimitadoresP) > 0:
                            pilhaDelimitadoresP.pop()
                        else:
                            print("Delimitador de fim " + i + " a mais na linha " + str(qtdLines))
                            return
                    elif i == "=":
                        tokens[i] = "Comando de atribuição"
                    elif i == "+":
                        tokens[i] = "Operador de adição"
                    elif i == "*":
                        tokens[i] = "Operador de multiplicação"
                    elif i == "-":
                        tokens[i] = "Operador de subtração"
                    elif i == "/":
                        tokens[i] = "Operador de divisão"
                    elif i == ";":
                        tokens[i] = "Finalizador de linha"
                    elif re.search(r"^[a-zA-Z]{1,}[0-9]*$", i):
                        tokens[i] = "Nome de variável"
                    elif re.search(r"^[0-9]{1,}$", i):
                        tokens[i] = "Constante numérica"
                    elif i == ",":
                        tokens[i] = "Separador"
                    elif i in ["==", "!="]:
                        tokens[i] = "Operador de igualdade"
                    elif i in [">", "<",">=", "<="]:
                        tokens[i] = "Operador relacional"
                    elif i in ["!", "&&", "||"]:
                        tokens[i] = "Operador lógico"
                    else:
                        if i == "#include":
                            i = aux
                        print("O token '" + i + "' na linha " + str(qtdLines) + " é inválido")
                        return
        qtdLines += 1
    if(len(pilhaDelimitadoresC) > 0):
        print("Delimitador de início '{' a mais na linha " + str(pilhaDelimitadoresC[len(pilhaDelimitadoresC)-1]))
        return
    if(len(pilhaDelimitadoresP) > 0):
        print("Delimitador de início '(' a mais na linha " + str(pilhaDelimitadoresP[len(pilhaDelimitadoresP)-1]))
        return
    for key in tokens:
        print(key + " - " + tokens[key])
    
def main():
    analiseLexica()

main()