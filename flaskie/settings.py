import os

# Flask settings
FLASK_SERVER_NAME = '127.0.0.1:8000'
FLASK_DEBUG = True  # Do not use debug mode in production
SECRET_KEY = os.getenv('SECRET_KEY', 'i love hot ladies')
TESTING = True
DEVELOPMENT = True

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = True
RESTPLUS_ERROR_404_HELP = False
RESTPLUS_MASK_HEADER = 'Authorization'

# SQLAlchemy settings

# Jwt settings
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
JWT_SECRET_KEY = 'jwt-secret-string'