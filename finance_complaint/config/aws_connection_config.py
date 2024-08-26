import os
from dotenv import load_dotenv
import boto3

load_dotenv()

class AWSConnectionConfig:

    def __init__(self):
        __access_key_id = os.environ['AWS_ACCESS_KEY']
        __secret_access_key_id = os.environ['AWS_SECRET_ACCESS_KEY']
        __region_name = os.environ["AWS_REGION"]
        if __access_key_id is None:
            raise Exception(f"Environment variable: AWS ACCESS KEY ID is not not set.")
        if __secret_access_key_id is None:
            raise Exception(f"Environment variable: AWS SECRET ACCESS KEY ID is not set.")
        if __region_name is None:
            raise Exception(f"Environment variable: AWS REGION is not set.")

        self.s3_resource = boto3.resource('s3',
                                        aws_access_key_id=__access_key_id,
                                        aws_secret_access_key=__secret_access_key_id,
                                        region_name=__region_name
                                        )
        self.s3_client = boto3.client("s3",
                                       aws_access_key_id=__access_key_id,
                                        aws_secret_access_key=__secret_access_key_id,
                                        region_name=__region_name
                                        )

