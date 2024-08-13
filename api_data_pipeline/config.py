import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#DB_FILE = os.path.join(BASE_DIR, 'data.db')
DATA_RETENTION_DAYS = 7
DB_FILE = 'data/data.db'

LOGGING = {
    'filename': 'data/app.log',
    #'filename': '../../data/app.log',
    'level': 'DEBUG',
    'format': '%(asctime)s:%(levelname)s:%(message)s'
}

API_URLS = {
    'NG_CarbonIntensity': 'https://api.carbonintensity.org.uk/regional/scotland'#,
    #'api2': 'https://api2.example.com/data',
    #'api3': 'https://api3.example.com/data',
}

TARRIF_PARAMETERS = [
        {
            'service' : 'Electric',
            'type' : 'StandingCharge',
            'tarrif_code' : 'E-1R-OE-FIX-12M-24-08-07-N',
            'file_path' : '/Users/jamiecoupe/PycharmProjects/api_data_pipeline/data/output/electric_standing_charges.json'
        },
        {
            'service': 'Electric',
            'type': 'UnitRate',
            'tarrif_code': 'E-1R-OE-FIX-12M-24-08-07-N',
            'file_path': '/Users/jamiecoupe/PycharmProjects/api_data_pipeline/data/output/electric_unit_rate.json'
        },
        {
            'service': 'Gas',
            'type': 'StandingCharge',
            'tarrif_code' : 'G-1R-OE-FIX-12M-24-08-07-N',
            'file_path': '/Users/jamiecoupe/PycharmProjects/api_data_pipeline/data/output/gas_standing_charges.json'
        },
        {
            'service': 'Gas',
            'type': 'UnitRate',
            'tarrif_code': 'G-1R-OE-FIX-12M-24-08-07-N',
            'file_path': '/Users/jamiecoupe/PycharmProjects/api_data_pipeline/data/output/gas_unit_rate.json'
        }
    ]