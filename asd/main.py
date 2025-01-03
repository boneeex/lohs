import sys
import os
import asyncio
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from query import create_tables


if __name__ == '__main__':
    asyncio.run(create_tables())