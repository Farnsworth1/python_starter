import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from beamon.core import calc
print("Started Beamon ***********************")
print("calling calc")
print(calc(1, 2))
print("Ended Beamon *************************")