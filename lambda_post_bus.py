import logging
import boto3
import os

dynamodb = boto3.client('dynamodb')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    stop_code = event['stop_code']
    bus_line = event['bus_line']
    datetime = event['datetime']

    logger.info(f'{stop_code} {bus_line} {datetime}')

    data = dynamodb.put_item(TableName=os.environ['TABLE_NAME'],
                             Item={
                                'stop_code': {'S': stop_code},
                                'bus_line': {'S': bus_line},
                                'datetime': {'S': datetime}
                             })

    return {
        'statusCode': 200,
        'body': data
    }
