import sys
import os
import json
from datetime import datetime

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logger import logger
import config
import storage_utilities


def store_tarrif_data():
    logger.info(f"Storing tarrif data")
    tarrif_parameters = config.TARRIF_PARAMETERS

    logger.info(f"Iterating through data")
    for tarrif_option in tarrif_parameters:

        logger.info(f"Storing data for {tarrif_option}")
        with open(tarrif_option['file_path'], 'r') as file_data:
            last_line=file_data.readlines()[-1]
            if last_line:  # Check if the last line is not empty
                last_line = last_line.replace('\'', '"')
            else:
                logger.warning(f"No valid data found in {tarrif_option['file_path']}")
                continue  # Skip this entry if the line is empty

        data = json.loads(last_line)

        print(f'Tarrif Data = {last_line}')
        print(f'Tarrif Code = {tarrif_option['tarrif_code']}')
        print(f'Service = {tarrif_option['service']}')
        print(f'Cost Type = {tarrif_option['type']}')
        print(f'Cost = {data['value_inc_vat']}')

        logger.info(f'Tarrif Code = {tarrif_option['tarrif_code']}')
        logger.info(f'Service = {tarrif_option['service']}')
        logger.info(f'Cost Type = {tarrif_option['type']}')
        logger.info(f'Cost = {data['value_inc_vat']}')

        storage_utilities.store_tarrif_data(tarrif_code=tarrif_option['tarrif_code'],
                                            service=tarrif_option['service'],
                                            cost_type=tarrif_option['type'],
                                            cost=data['value_inc_vat'])

def store_generation_data():
    logger.info(f"Storing generation data")

    with open('/Users/jamiecoupe/PycharmProjects/api_data_pipeline/data/output/ripple_data.json', 'r') as file_data:
        last_line=file_data.readlines()[-1]
        if last_line:  # Check if the last line is not empty
            last_line = last_line.replace('\'', '"')
        else:
            logger.warning(f"No valid data found in Ripple Generation data")


    data = json.loads(last_line)
    dt = datetime.strptime(data["from"], "%Y-%m-%dT%H:%M:%SZ")

    # Extract only the date
    generation_date = dt.date()

    print(f'Generation Data = {data}')
    print(f'Generation date = {generation_date}')
    print(f'from = {data["from"]}')
    print(f'to = {data["to"]}')
    print(f'generated = {data["generated"]}')
    print(f'earned = {data["earned"]}')

    logger.info(f'generation_date = {generation_date}')
    logger.info(f'generation_from = {data["from"]}')
    logger.info(f'generation_to = {data["to"]}')
    logger.info(f'generated = {data["generated"]}')
    logger.info(f'earned = {data["earned"]}')

    storage_utilities.store_generation_data(generation_date=generation_date,
                                        generation_from=data["from"],
                                        generation_to=data["to"],
                                        generation=data["generated"],
                                        earned=data['earned'])


if __name__ == '__main__':
    logger.info(f"Storing data")
    store_tarrif_data()
    store_generation_data()

