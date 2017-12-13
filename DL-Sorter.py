import shutil
import argparse
import re
from pathlib import Path
import glob

parser = argparse.ArgumentParser()
parser.add_argument("src", help="Source directory")
parser.add_argument("dst", help="Destination directory")
args = parser.parse_args()



def pirateHelper(byrjun, endir):
    src = Path(byrjun).glob('**/*') #fer recursively í gegnum allar möppur í undir current path
    nyttSett = set()

    for show in src:
        if not show.is_dir():
            #print(show.suffix)
            nyttSett.add(show.suffix)   #addar unique endingum inn í settið nyttSett
    print(nyttSett)


pirateHelper(args.src, args.dst)