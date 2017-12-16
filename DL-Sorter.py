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
    files =  []
    src = Path(byrjun).glob('**/*') #fer recursively í gegnum allar möppur í undir current path
    for show in src:
        if not show.is_dir():
            if show.suffix in allowedSuffixes and not 'sample' in str(show).lower():
                #name_match = re.findall('[A-Z][^A-Z]*', str(show))
                name_match = re.search(r'.*[\/\\](.*)[sS](\d{1,2})', str(show))
                if name_match:
                    show_name = showNameExtractonator(show, name_match)

                    season_number = 'Season ' + name_match.group(2).zfill(2)

                    dest_path = Path(endir, show_name, season_number)
                    files.append([show, dest_path])

    copyFiles(files)




#TODO
#Regex for shows 1x02 f.e.
#Fix some folder names
#Fix bad path-names
#Sum more shit

def showNameExtractonator(show, name_match):
    show_name = re.sub(r'\'', '', name_match.group(1))
    show_name = re.sub(r'[\. _-]+', ' ', show_name).strip().title()
    if not show_name:
        directories = re.split(r'[\/\\]', str(show))[:-1]
        # print(directories[::-1])
        for d in directories[::-1]:
            folder_name = re.sub(r'[sS]\d{1,2}|[sS]eason[\.-_ ]*\d{1,2}', '', d)
            # print(folder_name)
            if folder_name:
                show_name = folder_name
                show_name = re.sub(r'\'', '', show_name)
                show_name = re.sub(r'[\. _-]+', ' ', show_name).strip().title()
                break

    return show_name

def copyFiles(files):
    for f in files:
        show = f[0]
        dest_path = f[1]
        
        if not dest_path.exists():
            dest_path.mkdir(parents=True)
        copy(show, dest_path)


pirateHelper(args.src, args.dst)
