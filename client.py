import sys
import pickle
from base64 import b64encode, b64decode


USER = {
    "name": "Joe User",
    "role": "user"
}

user = b64encode(pickle.dumps(USER)).decode()
print(user)
