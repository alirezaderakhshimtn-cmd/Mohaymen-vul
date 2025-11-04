# Vulnerable Remote Code Execution example
import os
cmd = input("Enter command: ")
os.system(cmd)