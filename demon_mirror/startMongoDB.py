import os
import subprocess

BASE_DIR = os.path.abspath('.')

DB_DIR = os.path.join(BASE_DIR,'db')

subprocess.call('mongod --dbpath '+DB_DIR)