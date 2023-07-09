from botcity.web import WebBot, Browser, By
from configparser import ConfigParser

config = ConfigParser()
config.read(r'config\config.ini')


def capturar_dados(bot_w):
    ## CAPTURAR VALOR DO DI
    print('CAPTURANDO VALOR DO DI')
    capturar_di(bot_w)

    ## CAPTURAR VALOR CONTRATO VIGENTE
    print('CAPTURANDO O CONTRATO VIGENTE')
    contrato_vigente = capturar_contrato_vigente(bot_w)

    ## CAPTURAR VALOR DO DXY
    print('CAPTURANDO O VALOR DO DXY')
    capturar_dxy(bot_w)

    ## CAPTURAR PRECO DO DOLAR COMERCIAL
    print('CAPTURANDO VALOR DOLAR COMERCIAL')
    capturar_dolarcomercial(bot_w)

    ## CAPTURAR DOLFUT PRECO FECHAMENTO
    print('CAPTURANDO VALOR DO FECHAMENTO DOLAR FUTURO')
    capturar_dolfut(bot_w, contrato_vigente)

    print('FIM DA CAPTURA DE DADOS')


def capturar_di(bot_w):
    ## SETAR LINK VIA CONFIG
    link_di = config.get('links', 'link_di')

    bot_w.browse(link_di)
    di = bot_w.find_element('//*[@id="id_lista-futuros"]/tbody/tr[1]/td[3]', By.XPATH).text
    di = di.replace(",", ".")
    # di = float(di)
    print(f'DI: {di}')

    config.set('values', 'di', di)

    with open(r'config\config.ini', 'w') as config_file:
        config.write(config_file)


def capturar_contrato_vigente(bot_w):
    ## SETAR LINK VIA CONFIG
    link_contrato = config.get('links', 'link_contrato')

    bot_w.browse(link_contrato)
    contrato_vigente = bot_w.find_element('//*[@id="id_lista-futuros"]/tbody/tr[1]/td[1]/a', By.XPATH).text
    # print(f'Contrato Vigente: {contrato_vigente}')
    contrato_vigente = contrato_vigente[4:]
    print(contrato_vigente)

    config.set('values', 'contrato_vigente', contrato_vigente)

    with open(r'config\config.ini', 'w') as config_file:
        config.write(config_file)

    return contrato_vigente


def capturar_dxy(bot_w):
    ## SETAR LINK VIA CONFIG
    link_dxy = config.get('links', 'link_dxy')

    bot_w.browse(link_dxy)
    dxy = bot_w.find_element('//*[@id="quotes_summary_current_data"]/div[1]/div[1]/div[1]/div[2]/span[2]', By.XPATH).text
    dxy = dxy.replace(',', '.')
    # dxy = float(dxy)
    print(f'DXY: {dxy}')

    config.set('values', 'dxy', dxy)

    with open(r'config\config.ini', 'w') as config_file:
        config.write(config_file)


def capturar_dolarcomercial(bot_w):
    ## SETAR LINK VIA CONFIG
    link_dolcomercial = config.get('links', 'link_dolcomercial')

    bot_w.browse(link_dolcomercial)
    try:
        dol_comercial = bot_w.find_element('//*[@id="__next"]/div[2]/div/div/div[2]/main/div/div[1]/div[2]/div[1]/span',
                                           By.XPATH).text
    except Exception as erro:
        dol_comercial = bot_w.find_element('//*[@id="__next"]/div[2]/div/div/div[2]/main/div/div[5]/div/div[1]/div/div[2]/div/cq-context/div[2]/div[1]/div/div/span',
                                           By.XPATH).text

    dol_comercial = dol_comercial.replace(",", ".")
    # dol_comercial = float(dol_comercial)
    print(f'Dolar Comercial: {dol_comercial}')

    config.set('values', 'dol_comercial', dol_comercial)

    with open(r'config\config.ini', 'w') as config_file:
        config.write(config_file)


def capturar_dolfut(bot_w, contrato_vigente):
    ## SETAR LINK VIA CONFIG
    link_dolfut = config.get('links', 'link_dolfut')

    bot_w.browse(link_dolfut.replace(':CONTRATO_VIGENTE:', contrato_vigente))
    dol_fut_close = bot_w.find_element('//*[@id="quoteElementPiece8"]', By.XPATH).text
    dol_fut_close = dol_fut_close.replace(".", "").replace(",", ".")
    # dol_fut_close = float(dol_fut_close)
    print(f'Fechamento Dolar Futuro: {dol_fut_close}')

    config.set('values', 'dol_fut_close', dol_fut_close)

    with open(r'config\config.ini', 'w') as config_file:
        config.write(config_file)
