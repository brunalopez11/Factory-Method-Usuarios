#Classe base Pessoa:
class Pessoa:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel =nivel
        
    def mostarPermissao(self):
        print(f"{self.nome} - Cargo: {self.__class__.__name__}, Permissão: Nível {self.nivel}")
        
#Subclasse:
class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome, 0)
        
class Administrativo(Pessoa):
    def __init__(self, nome):
        super().__init__(nome, 1)
        
class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome, 2)
        
class Visitante(Pessoa):
    def __init__(self, nome):
        super().__init__(nome, 3)
        
#Factory
class FabricaPessoa:
    def criarPessoa(self, nome, cargo):
        if cargo.lower() == "aluno":
            return Aluno(nome)
        elif cargo.lower() == "administrativo":
            return Administrativo(nome)
        elif cargo.lower() == "professor":
            return Professor(nome)
        elif cargo.lower() == "visitante":
            return Visitante(nome)
        else:
            raise ValueError("Cargo Inválido!!")
        
#Uso
fabrica = FabricaPessoa()

p1 = fabrica.criarPessoa("Bruna" , "aluno")
p2 = fabrica.criarPessoa("Andrea" , "administrativo")
p3 = fabrica.criarPessoa("Vinicius", "professor")
p4 = fabrica.criarPessoa("Ana" , "visitante")

p1.mostarPermissao()
p2.mostarPermissao()
p3.mostarPermissao()
p4.mostarPermissao()
