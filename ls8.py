#!/usr/bin/env python3
import sys
import sys
from cpu import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Set the file to run as a parameter")
    else:      
        cpu = CPU()
        cpu.load(sys.argv[1])
        cpu.run()