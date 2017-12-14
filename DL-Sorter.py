import shutil
import argparse
import re
from pathlib import Path
import glob
import os
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument("src", help="Source directory")
parser.add_argument("dst", help="Destination directory")
args = parser.parse_args()

allowedSuffixes = {'.avi', '.flv','.wmv', '.mov', '.divx', '.mp4', '.mta',  '.mpg', '.m4v','.smi', '.mkv','.sfv', '.AVI'}

def pirateHelper(byrjun, endir):
    src = Path(byrjun).glob('**/*') #fer recursively í gegnum allar möppur í undir current path
    for show in src:
        if not show.is_dir():
            #Checka hvort þáttur sé örugglega movie fæll og ef það er movie fæll þá hendir hann í get info og ef þetta er þáttur þá moveFile
            if show.suffix in allowedSuffixes:

                info = getInfo(show)
                if info > -1: #Checkum hvort season nr. sé ekki -1 því ef það er -1 þá er það ekki þáttur
                    #Hér kemur move file á file-inn
                    print("Season: "+str(info)+" - "+str(show))
                    pass


def getInfo(show):
    season = -1
    name = 'notfound'
    #print(os.path.basename(show))
    name = re.search('^(.*?)s[0-9]', str(show))
    #print(name)
    b = re.search('((S|s)[0-9]+)', str(show)) #Sækjum season númerinu. Þetta virkar á sirka helminginn af þáttunum
    if b != None:
        season = b.string[b.start()+1:b.end()] #Breytir search resultinu í string (+1 til að sleppa S-inu)
    season = str(season) #Breytum í string svo hægt sé að skera 0 framan af tölunni auðveldlega
    season = season.lstrip('0')    # Þetta tekur 0-ið sem kemur fremst á töluna.
    return int(season) #Skilum tölunni sem (SKilum líka nafn hér)

def moveFile(show, nafn, season, dest):
    #TODO
    #Notum þetta til að færa fælinn í destination og eyða gamla þegar við erum búnir að finna allar upplýsingar
    #dlfile = os.listdir(r"C:\\Users\\oliprik\\Desktop\\python\\pirate\\downloads")
    dlfile = show
    for file in dlfile:
        #print(file)
        if os.path.isdir(dlfile + '/' + file):
            continue
        else:
            if os.path.exists(dest + '/' + file):
                Data = open(dlfile + file, "r").read()
                m = hashlib.sha1()
                m.update(Data)
                h = (m.hexdigest())[0:5]
                file(dest + "W").write(Data)
            print (file)
    #print (episode,season)
    return None
pirateHelper(args.src, args.dst)
