

class Heroi:

    
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

   
    def atacar(self):

        if self.tipo == "mago":
            ataque = "magia"

        elif self.tipo == "guerreiro":
            ataque = "espada"

        elif self.tipo == "monge":
            ataque = "artes marciais"

        elif self.tipo == "ninja":
            ataque = "shuriken"

        print(f"{self.tipo} atacou usando {ataque}")



def criar_heroi():

    nome = input().strip()
    idade = int(input())
    tipo = input().strip().lower()

  
    while tipo not in ["mago", "guerreiro", "monge", "ninja"]:
        tipo = input().strip().lower()

    return Heroi(nome, idade, tipo)



heroi = criar_heroi()
heroi.atacar()
