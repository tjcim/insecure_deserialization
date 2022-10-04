import sys
import pickle
from base64 import b64encode, b64decode

inp = ""
if (len(sys.argv) > 1):
    inp = sys.argv[1]
elif(sys.stdin):
    inp = sys.stdin.readlines()[0].strip()

des = pickle.loads(b64decode(inp))
print(des)
