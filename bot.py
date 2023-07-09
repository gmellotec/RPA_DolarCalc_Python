from config.web_bot import *
from pages.capturar_dados import *
from datetime import date
from libs.base_calculo import lista_feriados, calcular_dolar
from libs.send_email import send_email
from database.database import connect_database, insert_database

config = ConfigParser()
config.read(r'config\config.ini')


def main():
    print('INICIO DO PROCESSO DO CALC_DOLAR 2.0.0')

    ## INICIANDO INSTANCIA DO BOT WEB
    bot_w = WebBot()

    ## IMPORTANDO AS CONFIGURACOES DO WEB BOT
    config_webbot(bot_w)

    #### INICIO DO PROCESSO! ####

    ## VERIFICAR SE FERIADO OU FIM DE SEMANA
    data_hoje = date.today()

    # if data_hoje.weekday() in (5, 6) or str(data_hoje) in lista_feriados:
    if str(data_hoje) in lista_feriados:
        print("FIM DE SEMANA E/OU FERIADO - CÓDIGO NÃO EXECUTADO!")
    else:
        print("INICIO DO PROCESSO DE CAPTURA DE DADOS")
        ## CAPTURAR DADOS PARA CALCULO
        capturar_dados(bot_w)

        ## REALIZAR CALCULOS PARA OPERACAO DIARIA DO DOLAR
        print('CALCULAR DADOS PARA OPERACAO DIARIA')
        values = calcular_dolar()

        ## CONECTAR COM BANCO DE DADOS E FAZER INSERT DOS DADOS COLETADOS E CALCULADOS
        print('CONECTANDO AO BANCO DE DADOS')
        conn = connect_database()

        print('INSERINDO DADOS NO BANCO DE DADOS')
        insert_database(conn)

        print('ENVIAR DADOS POR EMAIL')
        send_email()




def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
