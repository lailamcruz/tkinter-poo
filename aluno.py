import uuid

class Pessoa:
    def __init__(self, nome, idade):
        # uuid -> identificador único universal
        self.matricula = uuid.uuid1()
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, nota):
        super().__init__(nome, idade)
        self.curso = curso
        self.nota = nota
    def __repr__(self):
        return f"Matricula: {self.matricula} \n" \
               f"Nome: {self.nome} \n" \
               f"Idade: {self.idade} \n" \
               f"Curso: {self.curso} \n" \
               f"Nota: {self.nota} \n"



if __name__ == "__main__":
    aluno = Aluno('laila', 25, 'viçage', 10)
    print(aluno)