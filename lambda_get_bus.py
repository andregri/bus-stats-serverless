import logging
from botocore.exceptions import ClientError
import boto3
from boto3.dynamodb.conditions import Key, Attr
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    stop_code = event['stop_code']
    start_datetime = event['start_datetime']
    stop_datetime = event['stop_datetime']

    logger.info(f'{stop_code} {start_datetime} {stop_datetime}')

    try:
        response = table.query(KeyConditionExpression=Key('stop_code').eq(stop_code))
    except ClientError as err:
        logger.error(
            "Couldn't query for stop code %s. Here's why: %s: %s", stop_code,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    else:
        return {
            'statusCode': 200,
            'body': response['Items']
        }
