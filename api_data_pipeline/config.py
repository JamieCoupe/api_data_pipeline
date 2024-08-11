import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#DB_FILE = os.path.join(BASE_DIR, 'data.db')
DATA_RETENTION_DAYS = 7
DB_FILE = 'data/data.db'

LOGGING = {
    'filename': 'data/app.log',
    'level': 'DEBUG',
    'format': '%(asctime)s:%(levelname)s:%(message)s'
}

API_URLS = {
    'NG_CarbonIntensity': 'https://api.carbonintensity.org.uk/regional/scotland'#,
    #'api2': 'https://api2.example.com/data',
    #'api3': 'https://api3.example.com/data',
}