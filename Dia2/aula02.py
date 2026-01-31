class pessoa:
    def __init__(self, nome, end, tel):     #init tem como função inicializar class
        self.nome = nome        #Criação de atributos
        self.end = end          #Criação de atributos
        self.telefone = tel     #Criação de atributos


    def mostrarDados(self): #função dentro de class criada com parametro dado para impressão de valores inseridos
        print(self.nome, self.end, self.telefone)

    def mostrarNome(self):
        print(self.nome)

    def editarTel(self,x):
        if type(x) == "str":
            self.telefone = x
            
#O propósito é reutilizar essas mesmas funções dentro de uma class, sem precisar criar variáveis para cada dado 

x = pessoa("exemplo", "avn342", "548539") #atribuição de uma classe em uma variável

x.mostrarDados() #imprimir uma "função" expecífica dentro de um tipo personalizado (class)



