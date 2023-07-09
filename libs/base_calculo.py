from datetime import date, timedelta
from configparser import ConfigParser

lista_feriados = ["2022-12-30", "2023-01-01", "2023-02-20", "2023-02-21",
                  "2023-04-07", "2023-04-22", "2023-05-01", "2023-06-08",
                  "2023-09-07", "2023-10-12", "2023-11-02", "2023-11-15",
                  "2023-12-25", "2023-12-29"]

lista_meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista_ult_dia = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
data_hoje = date.today()

config = ConfigParser()
config.read(r'config\config.ini')


def calcular_dolar():
    ## DECLARAR VARIAVEIS QUE FORAM CAPTURADAS DOS LINKS E SALVAS NO CONFIG.INI
    di = config.getfloat('values', 'di')
    dxy = config.getfloat('values', 'dxy')
    dol_comercial = config.getfloat('values', 'dol_comercial')
    dol_fut_close = config.getfloat('values', 'dol_fut_close')
    contrato_vigente = config.get('values', 'contrato_vigente')

    ## CALCULAR DIAS DE VENCIMENTO DO DI
    venc_di = calc_dias_uteis_di(lista_meses, lista_ult_dia)

    ## VARIAVEIS CONSTANTES
    DIAS_UTEIS = 252
    DELTA = 24

    ## CALCULAR TAXA OVER E DOLAR JUSTO
    taxa_over = ((di + 1) ** (1 / DIAS_UTEIS) - 1) * venc_di
    dolar_justo = dol_comercial * (1 + (taxa_over / 100)) * 1000

    ## CALCULAR RANGE DE ABERTUDA DO DOLAR FUTURO
    abertura = dol_fut_close * (1 + (dxy / 100))
    maxima = abertura * (1 + (taxa_over / 100)) + DELTA
    minima = abertura * (1 + (taxa_over / 100)) - DELTA

    config.set('values', 'taxa_over', str(taxa_over))
    config.set('values', 'dolar_justo', str(dolar_justo))
    config.set('values', 'abertura', str(abertura))
    config.set('values', 'maxima', str(maxima))
    config.set('values', 'minima', str(minima))
    config.set('values', 'venc_di', str(venc_di))

    with open(r'config\config.ini', 'w') as config_file:
        config.write(config_file)

    # print()
    # print('DADOS ABERTURA DO DOLAR')
    # print('Contrato Vigente:', contrato_vigente)
    # print('DI:', di)
    # print('DXY:', dxy)
    # print('Dolar Comercial:', dol_comercial)
    # print('Fechamento DOLFUT:', dol_fut_close)
    # print()
    # print('Taxa Over:', taxa_over)
    # print(f'Dolar Justo: {dolar_justo:.2f}')
    # print('Dias Venc. DI:', venc_di)
    # print()
    # print(f'Abertura: {abertura:.2f}')
    # print(f'Máxima:   {maxima:.2f}')
    # print(f'Minima:   {minima:.2f}')
    # print()
    # print('[I] CALCULOS EFETUADOS COM SUCESSO!')


def calc_dias_uteis_di(lista_meses, lista_ult_dia):
    for i, mes in enumerate(lista_meses):
        if mes == data_hoje.month:
            ult_dia_mes = lista_ult_dia[i]
    data_atual = date(data_hoje.year, data_hoje.month, data_hoje.day)
    data_final = date(data_hoje.year, data_hoje.month, ult_dia_mes)
    q_dias_uteis = 0

    for d in iterdates(data_atual, data_final):
        if d.weekday() not in (5, 6) and str(d) not in lista_feriados:
            q_dias_uteis += 1

    return q_dias_uteis


def iterdates(data_atual, data_final):
    one_day = timedelta(days=1)
    atual = data_atual
    while atual < data_final:
        yield atual
        atual += one_day
