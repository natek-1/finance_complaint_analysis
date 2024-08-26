import os
import sys
from typing import List

from finance_complaint.config.aws_connection_config import AWSConnectionConfig
from finance_complaint.exception import CustomException
from finance_complaint.logger import logging

class SimpleStorageService:

    def __init__(self, s3_bucket):
        aws_connection_config = AWSConnectionConfig()
        self.client = aws_connection_config.s3_client
        self.resource = aws_connection_config.s3_resource
        region = os.environ["AWS_REGION"]

        # Create bucket if not available
        response = self.client.list_buckets()
        existing_buckets = [bucket["Name"] for bucket in response["Buckets"]]
        if s3_bucket not in existing_buckets:
            location = {'LocationConstraint', region}
            self.client.create_bucket(Bucket=s3_bucket,
                                      CreateBucketConfiguration=location)
        
        self.bucket = self.resource.Bucket(s3_bucket)
        self.bucket_name = s3_bucket
    
    
