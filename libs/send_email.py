from botcity.plugins.email import BotEmailPlugin
from configparser import ConfigParser
from datetime import datetime

config = ConfigParser()
config.read(r'config\config.ini')

login_email = config.get('credentials', 'login_email')
password = config.get('credentials', 'password')


def send_email():
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

    email = BotEmailPlugin()

    # Configure IMAP com o servidor Gmail
    email.configure_imap("imap.gmail.com", 993)

    # Configure SMTP com o servidor Gmail
    email.configure_smtp("imap.gmail.com", 587)

    # Faça login com uma conta de email válida
    email.login(login_email, password)

    para = ['gmellotec@gmail.com', 'guilhermesamello@gmail.com']

    data_atual = datetime.now().strftime('%d/%m/%Y')

    assunto = f"Dados para operação Dolar Futuro dia {data_atual}"

    corpo_email = f"""
                <b>Bom dia, Trader! Segue os dados para operação do DOLAR no dia de hoje: {data_atual}</b>
                <br>
                <br>
                <table style="border-spacing: 0px; border: 1px solid;">
                <caption style="font-family: Calibri, sans-serif; font-size: 12px">Dados para Cálculo de Abertura do Dólar</caption>
                <tr>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        Contrato Vigente</th>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        </tdstyle>
                        {contrato_vigente}
                    </td>
                </tr>
                <tr>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        DI</th>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        </tdstyle>
                        {di}
                    </td>
                </tr>
                <tr>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        DXY</th>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        </tdstyle>
                        {dxy}
                    </td>
                </tr>
                <tr>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        Dol Comercial</th>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        </tdstyle>
                        {dol_comercial}
                    </td>
                </tr>
                <tr>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        Fech. DOLFUT</th>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        </tdstyle>
                        {dol_fut_close}
                    </td>
                </tr>
                <tr>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        Taxa Over</th>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        </tdstyle>
                        {taxa_over}
                    </td>
                </tr>
                <tr>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        Dolar Justo</th>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        </tdstyle>
                        {dolar_justo:.2f}
                    </td>
                </tr>
                <tr>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        D Vencimento DI</th>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        </tdstyle>
                        {venc_di}
                    </td>
                </tr>
                </table>
                <br>
                <br>
                <table style="border-spacing: 0px; border: 1px solid;">
                <caption style="font-family: Calibri, sans-serif; font-size: 12px">Dados Operacional Abertura DÓLAR</caption>
                <tr>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        Abertura</th>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        Máxima</th>
                    <th
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(112, 128, 144); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        Mínima</th>
                </tr>
                <tr>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        {abertura:.2f}</td>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        {maxima:.2f}</td>
                    <td
                        style="border: 1px solid white; width: 120px; height: 40px; background-color: rgb(158,185,202); text-align: center; font-family: Calibri, sans-serif, sans-serif; font-size: 12px;">
                        {minima:.2f}</td>
                </tr>
                </table>
                """

    # Enviando a mensagem de e -mail
    email.send_message(assunto, corpo_email, para, use_html=True)

    print(f'E-MAIL ENVIADO COM SUCESSO PARA: {para} !!!')

    # Feche a conexão com os servidores IMAP e SMTP
    email.disconnect()
