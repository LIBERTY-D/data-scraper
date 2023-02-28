
from scapy.all import *
import sys
import logging
logging.getLogger("scapy").setLevel(logging.CRITICAL)


def get_version()->str:
    version = sys.version[0].startswith("3")
    python = ''
    if version:
        version = sys.version[0]
        python = f'Python{version}'
    else:
        version = sys.version[0]
        python = f'Python'
    return python
    
  

try:

    p = sr1(IP(dst=sys.argv[1])/TCP())
    if p:
        p.summary()
except PermissionError as err:
    print(f"[*&]You Might Need Root Priveledges,Try 'sudo {get_version()} {sys.argv[0]} {sys.argv[1]}'"+str(err))


