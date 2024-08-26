import os, sys

from finance_complaint.exception import CustomException
from finance_complaint.logger import logging
from collections import namedtuple
from finance_complaint.utils import read_yaml_file, write_yaml_file


DataIngestionMetadataInfo = namedtuple("DataIngestionMetadataInfo", ["from_date", "to_date", "data_file_path"])


