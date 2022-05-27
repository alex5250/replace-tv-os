import configparser


def read_config():
    config = configparser.ConfigParser()
    print(config.sections())
    config.read('config.ini')
    url=config['IMAGE_DOWNLOAD']['url']
    checksum=config['IMAGE_DOWNLOAD']['checksum']
    tmp_dir=config['IMAGE_DOWNLOAD']['tmp_dir']
    command=config['INSTALL_CONFIG']['command']
    return url,checksum,tmp_dir,command