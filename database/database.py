import pyodbc
from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read(r'config\config.ini')


def connect_database():
    try:
        dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                         "Server=localhost;"
                         r"Database=database\dados_calcDolar.db;")
        conexao = pyodbc.connect(dados_conexao)
        print('CONEXAO REALIZADA COM SUCESSO')
        return conexao
    except Exception as erro:
        print(f'Falha na conexao com o banco de dados: {erro} ')


def insert_database(conexao):
    di = config.getfloat('values', 'di')
    dxy = config.getfloat('values', 'dxy')
    dol_comercial = config.getfloat('values', 'dol_comercial')
    dol_fut_close = config.getfloat('values', 'dol_fut_close')
    contrato_vigente = config.get('values', 'contrato_vigente')
    taxa_over = config.getfloat('values', 'taxa_over')
    dolar_justo = config.getfloat('values', 'dolar_justo')
    abertura = config.getfloat('values', 'abertura')
    maxima = config.getfloat('values', 'maxima')
    minima = config.getfloat('values', 'minima')
    venc_di = config.getint('values', 'venc_di')
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    varQuery = f"""
                    INSERT INTO CALC_DOLAR (DATA, 
                    CONTRATO_VIGENTE, 
                    DI, 
                    DXY, 
                    DOL_COMERCIAL, 
                    DOLFUT_FECHAMENTO, 
                    DOLAR_JUSTO, 
                    VENC_DI, 
                    TAXA_OVER, 
                    CALC_ABERTURA, 
                    CALC_MAXIMA, 
                    CALC_MINIMA)
                    VALUES
                    (datetime('now'), 
                    '{contrato_vigente}', 
                    '{di}', 
                    '{dxy}', 
                    '{dol_comercial:.2f}', 
                    '{dol_fut_close:.2f}', 
                    '{dolar_justo:.2f}', 
                    '{venc_di}', 
                    '{taxa_over}', 
                    '{abertura:.2f}', 
                    '{maxima:.2f}', 
                    '{minima:.2f}')
                    """

    cursor = conexao.cursor()
    cursor.execute(varQuery)

    cursor.commit()

    cursor.close()
    conexao.close()
    print("DADOS INSERIDOS COM SUCESSO NO BANCO DE DADOS")