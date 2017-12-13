import shutil
import argparse
import re
from pathlib import Path
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument("src", help="Source directory")
parser.add_argument("dst", help="Destination directory")
args = parser.parse_args()

allowedSuffixes = {'.avi', '.flv','.wmv', '.mov', '.divx', '.mp4', '.mta',  '.mpg', '.m4v','.smi', '.mkv','.sfv', '.AVI'}

def pirateHelper(byrjun, endir):
    src = Path(byrjun).glob('**/*') #fer recursively í gegnum allar möppur í undir current path


    for show in src:
        if not show.is_dir():
            #print(show)

            #Checka hvort þáttur sé örugglega movie fæll og ef það er movie fæll þá hendir hann í get info og ef þetta er þáttur þá moveFile
            if show.suffix in allowedSuffixes:

                info = getInfo(show)
                print(info)
                if True == True: #Checkum hvort season nr. sé ekki -1 því ef það er -1 þá er það ekki þáttur
                    #moveFile(show, info) færum fælinn
                    b = 1 #Bara svo forritið keyri án þess að hafa klára if statementið


def getInfo(show):
    season = -1
    name = 'notfound'
    #print(os.path.basename(show))

    b = re.search('((S|s)[0-9]+)', str(show)) #Sækjum season númerinu. Þetta virkar á sirka helminginn af þáttunum
    if b != None:
        season = b.string[b.start()+1:b.end()] #Breytir search resultinu í string (+1 til að sleppa S-inu)
    season = str(season) #Breytum í string svo hægt sé að skera 0 framan af tölunni auðveldlega
    season = season.lstrip('0')    # Þetta tekur 0-ið sem kemur fremst á töluna.
    return int(season) #Skilum tölunni sem integer.
    #TODO
    #Get show name, episode nr og season.
    #Ef fællinn er ekki lýsandi á episode nr og season nr þá þurfum við að checka parent folder alveg upp að rótinni á download möppunni.
    #returna nafni, episode nr. og season nr.
    #Ef þetta er ekki þáttur heldur bíómynd eða annað þá skilum við bara episode eða season nr -1 og checkum á því í pirateHelper og sleppum því að færa hann.
def moveFile(show, nafn, episode, season, dest):
    #TODO
    #Notum þetta til að færa fælinn í destination og eyða gamla þegar við erum búnir að finna allar upplýsingar
    return None
pirateHelper(args.src, args.dst)
