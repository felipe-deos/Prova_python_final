import pymysql.cursors
from aluno import Aluno
class AlunoBanco:
    def __init__(self, host: str, username: str, db: str, password: str):
        self.conexao = self.criarConexao(host, username, db, password)

        self.cursor = self.conexao.cursor()
    def criarConexao(self, host: str, username: str, db: str, password: str):
        try:
            conn = pymysql.connect(host=host, user=username,
                                   db=db, password=password,
                                   cursorclass=pymysql.cursors.DictCursor)
            return conn
        except Exception as erro:
            print(f"Erro ao conectar ao banco! Erro: {erro}")

    def insert(self, aluno: Aluno):
        try:
            sql = ('INSERT INTO alunos (matricula, nome, idade, curso, nota) '
                   'VALUES (%s, %s, %s, %s, %s)')
            self.cursor.execute(sql, (aluno.matricula, aluno.nome,
                                      aluno.idade, aluno.curso, aluno.nota))
            self.conexao.commit()
            print('Aluno cadastrado com sucesso!')
        except Exception as error:
            print(f'Erro ao inserir! Erro: {error}')

    def update(self, aluno: Aluno):
        try:
            sql = ("UPDATE alunos SET nome = %s, idade = %s, curso = %s, nota = %s "
                   "WHERE matricula = %s")
            self.cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso,
                                      aluno.nota, aluno.matricula))
            self.conexao.commit()
            print('Dados alterados!')
        except Exception as error:
            print(f'Erro ao editar! Erro: {error}')

    def delete(self, matricula: int):
        try:
            sql = "DELETE FROM alunos WHERE matricula = %s"
            self.cursor.execute(sql, matricula)
            self.conexao.commit()
            print('Dados removidos com sucesso!')
        except Exception as error:
            print(f'Erro ao deletar! erro: {error}')

    def select(self):
        try:
            sql = "SELECT*FROM alunos"
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall()
            return alunos
        except Exception as error:
            print(f'Erro ao listar! Erro: {error}')

if __name__ == "__main__":
    a = AlunoBanco('localhost', 'root', 'escola', '')

    aluno1 = Aluno('Jonas', 19,' java', 8.5)
    aluno2 = Aluno('Diego', 21, 'Python', 7.9)
    aluno3=Aluno('Maria',21,'Python',9.9)
    a.insert(aluno1)
    a.insert(aluno2)
    a.insert(aluno3)
    print(a.select())
    aluno1.nome = 'Jonas Lopes'
    a.update(aluno1)
    print(a.select())
    a.delete(aluno1.matricula)
    print(a.select())





