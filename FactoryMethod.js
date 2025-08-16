// Classe de pessoa
class Pessoa {
    constructor(nome, nivel){
        this.nome = nome;
        this.nivel = nivel;
    }
    mostrarPermissao(){
        console.log(`${this.nome} Cargo - ${this.constructor.name}, Permissão: Nível ${this.nivel}`);
    }
}

// Subclasse
class Aluno extends Pessoa{
    constructor(nome){
        super(nome, 0);
    }
}

class Administrativo extends Pessoa{
    constructor(nome){
        super(nome, 1);
    }
}

class Professor extends Pessoa{
    constructor(nome){
        super(nome, 2);
    }
}

class Visitante extends Pessoa{
    constructor(nome){
        super(nome, 3)
    }
}
// Factory
class fabricaPessoa{
    criarPessoa(nome, Cargo){
        switch(Cargo.toLowerCase()){
            case "aluno": return new Aluno(nome);
            case "administrativo": return new Administrativo(nome);
            case "professor": return new Professor(nome);
            case "visitante": return new Visitante(nome);
            default: throw new Error("Cargo Invalido!!")
        }
    }
}
// Uso
const fabrica = new fabricaPessoa();

const p1 = fabrica.criarPessoa("Bruna", "Aluno");
const p2 = fabrica.criarPessoa("Andrea", "Administrativo");
const p3 = fabrica.criarPessoa("Vinicius", "Professor");
const p4 = fabrica.criarPessoa("Ana", "Visitante");


p1.mostrarPermissao();
p2.mostrarPermissao();
p3.mostrarPermissao();
p4.mostrarPermissao();