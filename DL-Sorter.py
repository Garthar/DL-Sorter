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
    files = []
    src = Path(byrjun).glob('**/*') #fer recursively í gegnum allar möppur í undir current path
    for show in src: #Athugar með hvern þátt fyrir sig.
        if not show.is_dir(): #Athugar hvort fællinn sé mappa
            if show.suffix in allowedSuffixes and not 'sample' in str(show).lower():

                #Fer í gegnum listan og athugar týpu af þætti
                name_match1 = re.search(r'.*[\/\\](.*)[sS](\d{1,2})', str(show))
                name_match2 = re.search(r'.*[\/\\](.*)[\. ]([0]*\d)\d{2}[\. ]', str(show))
                name_match3 = re.search(r'.*[\/\\](.*)[^\d](\d{1,2})[\.xX]\d{1,2}[^\d]', str(show))
                name_match4 = re.search(r'.*[\/\\](?P<show_name>)(\d)\d{2}', str(show)) #(?P<show_name>) optional
                name_match5 = re.search(r'.*[\/\\](.*)[sS]eason (?P<season>\d{1,2})', str(show)) #(?P<season>) optional

                #Sendir resultið úr regexinu inn í regExMatches. Skippar ef það kom ekkert út. Ef ekkert fannst þá er fællinn líklegast ekki þáttur.
                if name_match1:
                    regExMatches(show, name_match1, endir, files)
                elif name_match2:
                    regExMatches(show, name_match2, endir, files)
                elif name_match3:
                    regExMatches(show, name_match3, endir, files)
                elif name_match4:
                    regExMatches(show, name_match4, endir, files)
                elif name_match5:
                    regExMatches(show, name_match5, endir, files)
    #Að lokum copy-ar hann alla file-a sem voru rétt greindir.
    copyFiles(files)



def showNameExtractonator(show, name_match):
    #Sækir nafnið á þættinum.
    show_name = re.sub(r'\'', '', name_match.group(1))
    show_name = re.sub(r'[\. _-]+', ' ', show_name)
    show_name = show_name.strip().title()

    #Ef nafnið fannst ekki þá þurfum við að beyta annari aðferð til að finna það.
    if not show_name:
        directories = re.split(r'[\/\\]', str(show))[:-1]
        for d in directories[::-1]:
            folder_name = re.sub(r'[sS]\d{1,2}|[sS]eason[\.-_ ]*\d{1,2}', '', d)
            if folder_name:
                show_name = folder_name
                show_name = re.sub(r'\'', '', show_name)
                show_name = re.sub(r'[\. _-]+', ' ', show_name).strip().title()
                break
    return show_name

def copyFiles(files):
    #Bætir möpunum inn og hverjum file fyrir sig á eftir
    for f in files:
        show = f[0]
        dest_path = f[1]

        if not dest_path.exists():
            dest_path.mkdir(parents=True)
        copy(show, dest_path)

def regExMatches(show, name_match, endir, files):
        #Kallar á showNameExtractonator sem sækir nafnið á þættinum
        show_name = showNameExtractonator(show, name_match)

        #Sækir season númerið og bætir inn í streng sem er nafnið á undirmöppunni.
        season_number = 'Season ' + name_match.group(2).zfill(2)

        #Býr til slóðina sem þátturinn á að fara
        dest_path = Path(endir, show_name, season_number)

        #Bætir inn í listan af þáttum sem bæta á við.
        files.append([show, dest_path])

pirateHelper(args.src, args.dst)
