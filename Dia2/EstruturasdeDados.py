pessoas = [
    ["nome", "endereco", "telefone", "total compras"], #indice
    ["Lucas", "av 123", "4423","R$1200,00"], #atributos
    ["Maria", "av 743", "9420", "R$139,90"],
    ["Frederico", "av 322", "9382","R$75,00"],

] #dentro de matriz []

#manipulação de dados estruturados

pessoas[1][2] = 123 #Edição de valores
pessoas[1][1] = pessoas[1][1].capitalize()  #.captalize() returna maiuscula na primeira casa do indice mencionado

#for item in pessoas[1:]:    #[1:3] slice com parametro inicial : final
#    item[1] = item[1].capitalize()  #
#print(pessoas)  

total = 0
for item in pessoas[1:]:
    total += float(item[3].replace(",",".").replace("R$",""))   #conversão e método replace     .replace("","")
print(total)
    
#replace
#slice 
#captalize



    