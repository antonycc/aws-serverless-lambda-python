import os
import logging
import boto3
import uuid

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def lambda_handler(event, context):    
    destination_bucket = os.environ['DestinationBucket']
    if 'Records' in event:
        for record in event['Records']:
            source_bucket = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key'] 
            local_filepath = '/tmp/{}{}'.format(uuid.uuid4(), key)
            s3_client.download_file(source_bucket, object_key, local_filepath)
            s3_client.upload_file(local_filepath, destination_bucket, object_key)
            logger.info("Created s3://{}/{}".format(destination_bucket, object_key))