# Vulnerable Insecure Deserialization example
import pickle
from flask import request

data = request.form['payload']
obj = pickle.loads(data)