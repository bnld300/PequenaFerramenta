
import mysql.connector
from dotenv import load_dotenv, set_key
from pathlib import Path
from getpass import getpass
import os

ARQUIVO_ENV = Path(__file__).resolve().parent.parent / '.env'


def configurar():

    load_dotenv(ARQUIVO_ENV, override=True)

    if not all([
        os.getenv('DB_HOST'),
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_NAME')
    ]):

        print('\nCONFIGURAÇÃO DO BANCO DE DADOS')

        host = input('Host: ').strip()
        user = input('Usuário: ').strip()
        password = getpass('Senha: ')
        database = input('Banco de dados: ').strip()

        configuracoes = {
            'DB_HOST': host,
            'DB_USER': user,
            'DB_PASSWORD': password,
            'DB_NAME': database
        }

        for chave, valor in configuracoes.items():
            set_key(ARQUIVO_ENV, chave, valor, quote_mode='always')

        load_dotenv(ARQUIVO_ENV, override=True)


def conectar():

    configurar()

    try:
        banco = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )

        return banco

    except mysql.connector.Error as erro:
        raise ConnectionError(
            f'Não foi possível conectar ao MySQL: {erro}'
        ) from erro
