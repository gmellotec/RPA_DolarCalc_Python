from botcity.web import WebBot, Browser, By
from configparser import ConfigParser

config = ConfigParser()
config.read(r'config\config.ini')


def config_webbot(bot_w):
    bot_w.headless = False

    # Uncomment to change the default Browser to Firefox
    bot_w.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    path_driver = config.get('path', 'path_driver')
    bot_w.driver_path = path_driver
