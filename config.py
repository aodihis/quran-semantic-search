import os

class Config:
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True