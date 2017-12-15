from shutil import copy
from pathlib import Path
import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument("src", help="Source directory")
parser.add_argument("dst", help="Destination directory")
args = parser.parse_args()

allowedSuffixes = {'.avi', '.flv', '.wmv', '.mov', '.divx', '.mp4', '.mta',  '.mpg', '.m4v', '.smi', '.mkv', '.AVI'}

def pirateHelper(byrjun, endir):
    src = Path(byrjun).glob('**/*') #fer recursively í gegnum allar möppur í undir current path
    for show in src:
        if not show.is_dir():
            #Checka hvort þáttur sé örugglega movie fæll og ef það er movie fæll þá hendir hann í get info og ef þetta er þáttur þá moveFile
            if show.suffix in allowedSuffixes:

                test = re.search(r'.*[\/\\](.*)[sS](\d{1,2})', str(show))
                if test:
                    show_name = re.sub(r'\'', '',test.group(1))
                    show_name = re.sub(r'[\. _-]+', ' ',show_name).strip().title()
                    if not show_name:
                        temp = str(show).split('\\')[:-1]
                        #print(temp[::-1])
                        for t in temp[::-1]:
                            xname = re.sub(r'[sS]\d{1,2}|[sS]eason[\.-_ ]*\d{1,2}', '', t)
                            if xname:
                                show_name = xname
                                show_name = re.sub(r'\'', '', show_name)
                                show_name = re.sub(r'[\. _-]+', ' ', show_name).strip().title()
                                break

                    season_number = 'Season ' + test.group(2).zfill(2)

                    dest_path = Path(endir, show_name, season_number)
                    if not dest_path.exists():
                        dest_path.mkdir(parents=True)
                    copy(show, dest_path)

#TODO
#Regex for shows 1x02 f.e.
#Fix some folder names
#Fix bad path-names
#Sum more shit

def getInfo(show):
    return 0

def moveFile(show, season, dest):
    return 0

pirateHelper(args.src, args.dst)
