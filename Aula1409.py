#S T R I N G S Aula dia 14/09

frase = "Hello world!"
print(frase)
print(len(frase)) #contar o tamanho
print(frase[0]) #mostrar a posição que quero mostrar
print(frase[0:5]) #mostrar só a primeira palavra
#STRING é imutável, não da pra trocar apenas uma coisa como em listas, é igual em tuplas
frase = list(frase) #transformar em lista para poder modificar algo
print(frase)
frase[0] = "h"
print(frase)
frase = "".join(frase) #desfazendo a lista e voltando a ser frase '_'
print(frase)

palavra1 = "Boa"
palavra2 = "noite"
palavra3 = "!"

print(palavra1 +" " + palavra2  + palavra3*3) #Juntar as palavras e o " " é para dar o espaço na frase e o vezes 3 é vezes 3

palavra_lista = palavra1 +" " + palavra2  + palavra3*3
palavra_lista = list(palavra_lista)

palavra_string = "".join(palavra_lista) #me perdi aqui, Bea mentindo enquanto escrevo oq sinto

print(palavra_string.startswith("Boa"))
print(palavra_string.endswith("Boa"))
print("Hello" in palavra_string)
print("Boa"in palavra_string)
print("boa" in palavra_string)

print(palavra_string.count("o")) #conta as letras da palavra
print(palavra_string.find("u")) # -1 = não tem
print(palavra_string.find("o"))#conta mas só fala se tem ou não tem sem risadinha

print(palavra_string)
print(palavra_string.split(" ")) #ele le a minha variável e procura todos os espaços (pq eu coloquei ali) e aí ele vai cortar os espaços e arrancar as palvras e formar lista com elas (itens)

print(palavra_string.replace("noite", "tarde")) #substitur noite por tarde
palavra_nova = (palavra_string.replace("noite", "tarde"))
print(palavra_nova)

titulo = "CHECKPOINT 2" #para apresentar bonitão a CP
print(titulo.center(50))
print(titulo.center(50,"-"))

print(titulo.rjust(50,".")) #outro jeito de colocar titulo - alinha para direita
print(titulo.ljust(50,"*")) #alinha para esquerda