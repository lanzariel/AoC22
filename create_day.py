import sys
import os 
import requests

from web_data import cookies, headers

n = str(int(sys.argv[1]))

n = n.zfill(2)
try:
    os.mkdir(n)
    path = n + "/"
except:
    print("Already Existing Directory. Bye")
    exit()
with open(path+"1.py", "w") as f:
    f.write("import sys\n")
    f.write("\n")
    f.write("path = sys.argv[1]\n")
    f.write("with open(path, 'r') as f:\n")
    f.write("    lines = f.readlines()\n")
    f.write("\n")

url = 'https://adventofcode.com/2022/day/' + str(int(n)) + '/input'
try:

    response = requests.get(url, headers=headers, cookies=cookies)
    with open(path + 'input.txt', 'w') as f:
        f.write(response.text)
except:
    print("No file of input")
