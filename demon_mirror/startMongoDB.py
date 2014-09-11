import os
import subprocess

BASE_DIR = os.path.abspath('.')

DB_DIR = os.path.join(BASE_DIR,'data'+os.sep+'db')
LOG_DIR = os.path.join(BASE_DIR,'data'+os.sep+'log'+os.sep+'mongo.log')
# print(DB_DIR)
# print('start /b mongod --dbpath '+DB_DIR +' > '+LOG_DIR)
param =[]
param.append('start')
param.append('/b')
param.append('mongod')
param.append('--dbpath')
param.append(DB_DIR)
param.append('>')
param.append(LOG_DIR)
print(param)
subprocess.call(param,shell=True)
# subprocess.call('start /b mongod --dbpath '+DB_DIR +' > '+LOG_DIR)