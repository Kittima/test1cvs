#! Insert the current directory path to Python Path
import sys
import os
cwd = os.getcwd()

sys.path.append(cwd)
#print(sys.path)

# Test the module: generate_list
from generate_list2 import printIt

for _ in range(100):
    printIt()