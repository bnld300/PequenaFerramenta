from database.conexoes import conectar

class MostrarDadosSQL:

    def Mostrar_Tabela(self):
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute('SELECT * FROM pessoas')

        resultado = cursor.fetchall()
        for pessoa in resultado:
            print(pessoa)

        cursor.close()
        banco.close()

    def Inserir_Novo_Aluno(self, nome, profissao, nascimento, sexo, peso, altura, nacionalidade):
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute(
            '''INSERT INTO pessoas
            (nome, profissao, nascimento, sexo, peso, altura, nacionalidade)
            VALUES (%s,%s,%s,%s,%s,%s,%s)''',
            (nome, profissao, nascimento, sexo, peso, altura, nacionalidade)
        )

        banco.commit()
        cursor.close()
        banco.close()

    def Editar_Excluir(self, opcao, id, nome=None, profissao=None):
        banco = conectar()
        cursor = banco.cursor()

        if opcao == 'editar':
            cursor.execute(
                'UPDATE pessoas SET nome = %s, profissao = %s WHERE id = %s',
                (nome, profissao, id)
            )

        elif opcao == 'excluir':
            cursor.execute(
                'DELETE FROM pessoas WHERE id = %s',
                (id,)
            )

        else:
            cursor.close()
            banco.close()
            raise ValueError('Operação inválida!')

        banco.commit()
        cursor.close()
        banco.close()

    def buscar_todos_ids(self):
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute('SELECT id FROM pessoas')

        resultados = cursor.fetchall()

        cursor.close()
        banco.close()

        return [row[0] for row in resultados]