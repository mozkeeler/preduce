#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from reducer_utils import chunking_reducer

def main():
    chunking_reducer(sys.argv[1], min_chunk_size = 2)

if __name__ == "__main__":
    main()
