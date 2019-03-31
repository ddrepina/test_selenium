from configparser import ConfigParser


def config_read():
    config = ConfigParser()
    config.read('config/config.ini')
    try:
        index = config.get('url', 'index')
        account = config.get('url', 'account')
        acme = config.get('url', 'acme')
        sale = config.get('url', 'sale')
    except Exception as e:
        print('error:', e)

    return {'index': index, 'account': account, 'acme': acme, 'sale': sale}
