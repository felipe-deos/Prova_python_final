class Aluno:
    matricula = 0
    def __init__(self, nome: str, idade: int, curso: str, nota: float):
        Aluno.matricula += 1
        self.matricula = Aluno.matricula
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def __repr__(self):
        return (f"({self.matricula}, {self.nome}, {self.idade},"
                f"{self.curso}, {self.nota})")
if __name__ == "__main__":
    print(Aluno('Jonas', 19, "Python", 8.5))