from servicos.services import MostrarDadosSQL
from datetime import datetime

dados = MostrarDadosSQL()

while True:
    opcao = input(
        '\n([1] MOSTRAR DADOS) '
        '([2] INSERIR UM NOVO ALUNO) '
        '([3] EDITAR OU EXCLUIR UM ALUNO PELO ID) '
        '([4] ENCERRAR): '
    )

    # ─── OPÇÃO 1 ───────────────────────────────────────────
    if opcao == '1':
        dados.Mostrar_Tabela()

    # ─── OPÇÃO 2 ───────────────────────────────────────────
    elif opcao == '2':
        erro = False

        # NOME
        nome = input('Digite o nome do aluno: ').strip()
        if len(nome) < 1:
            print('Nome não pode ser vazio!')
            erro = True
        elif len(nome) > 12:
            print(f'Nome contém {len(nome)} caracteres, o limite é 12!')
            erro = True
        else:
            print('Nome aceito!')

        # PROFISSÃO
        profissao = input('Digite a profissão do aluno: ').strip()
        if len(profissao) < 1:
            print('Profissão não pode ser vazia!')
            erro = True
        elif len(profissao) > 15:
            print(f'Profissão contém {len(profissao)} caracteres, o limite é 15!')
            erro = True
        else:
            print('Profissão aceita!')

        # NASCIMENTO
        nascimento = input('Digite a data de nascimento (AAAA-MM-DD): ').strip()
        try:
            data = datetime.strptime(nascimento, '%Y-%m-%d')
            if data.year < 1930:
                print('Ano precisa ser 1930 ou posterior.')
                erro = True
            else:
                print(f"Data aceita: {data.strftime('%d/%m/%Y')}")
        except ValueError:
            print('Formato inválido! Use AAAA-MM-DD. Exemplo: 2000-12-30')
            erro = True

        # SEXO
        sexo = input('Digite o sexo do aluno (M/F): ').strip().upper()
        if sexo not in ('M', 'F'):
            print(f'Só é aceito M ou F, você digitou: {sexo}')
            erro = True
        else:
            print(f'Sexo aceito: {sexo}')

        # PESO
        peso = input('Digite o peso do aluno (kg, apenas números): ').strip()
        if len(peso) < 1:
            print('Você não digitou nada!')
            erro = True
        elif len(peso) > 3:
            print(f'Peso pode conter apenas até 3 caracteres!')
            erro = True
        else:
            try:
                int(peso)
                print(f'Peso aceito: {peso}kg')
            except ValueError:
                print(f'O peso não pode conter letras: {peso}')
                erro = True

        # ALTURA
        altura = input('Digite a altura do aluno (cm, apenas números): ').strip()
        if len(altura) < 1:
            print('Você não digitou nada!')
            erro = True
        elif len(altura) > 3:
            print(f'Altura pode conter apenas até 3 caracteres!')
            erro = True
        else:
            try:
                int(altura)
                print(f'Altura aceita: {altura}cm')
            except ValueError:
                print(f'A altura não pode conter letras: {altura}')
                erro = True

        # NACIONALIDADE
        nacionalidade = input('Digite a nacionalidade do aluno: ').strip()
        if len(nacionalidade) < 1:
            print('Nacionalidade não pode ser vazia!')
            erro = True
        elif len(nacionalidade) > 12:
            print(f'Nacionalidade contém {len(nacionalidade)} caracteres, o limite é 12!')
            erro = True
        else:
            print('Nacionalidade aceita!')

        # INSERÇÃO — só executa se tudo estiver certo
        if not erro:
            dados.Inserir_Novo_Aluno(nome, profissao, nascimento, sexo, peso, altura, nacionalidade)
            print('\nAluno inserido com sucesso!')
        else:
            print('\nInserção cancelada! Corrija os erros e tente novamente.')

    # ─── OPÇÃO 3 ───────────────────────────────────────────
    elif opcao == '3':
        a = input('Deseja editar ou excluir? ').strip().lower()
        if a not in ('editar', 'excluir'):
            print('Opção inválida! Digite "editar" ou "excluir"')
            continue

        try:
            b = int(input('Digite o id do aluno: '))
        except ValueError:
            print('O ID precisa ser um número inteiro!')
            continue

        ids_existentes = dados.buscar_todos_ids()
        if b not in ids_existentes:
            print(f'ID {b} não encontrado no banco de dados!')
            continue

        if a == 'editar':
            nome = input('Novo nome: ').strip()
            profissao = input('Nova profissão: ').strip()
            dados.Editar_Excluir(a, b, nome=nome, profissao=profissao)
        else:
            dados.Editar_Excluir(a, b)

        print('Operação realizada com sucesso!')

    # ─── OPÇÃO 4 ───────────────────────────────────────────
    elif opcao == '4':
        print('Encerrando...')
        break

    else:
        print('Opção inválida! Digite 1, 2, 3 ou 4.')