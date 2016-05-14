class BaseConfig(object):
    'Base config class'
    SECRET_KEY = 'A random secret key'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = 'my value'

class ProductionConfig(BaseConfig):
    'production spesific config'
    DEBUG = False
    #SECRET_KEY = open('/path/to/secret/key/file').read()

class StagingConfig(BaseConfig):
    'Staging specific config'
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    'Development environment spesific config'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Another random secret key'