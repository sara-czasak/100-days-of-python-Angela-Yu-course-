import requests
import dotenv
import os
from pprint import pprint
from data_manager import *


dotenv.load_dotenv()


data_manager = DataManager()
pprint(data_manager.get_data())