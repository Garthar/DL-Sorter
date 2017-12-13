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



def pirateHelper(byrjun, endir):
    src = Path(byrjun).glob('**/*') #fer recursively í gegnum allar möppur í undir current path
    nyttSett = set()

    for show in src:
        if not show.is_dir():
            print(show)
            #nyttSett.add(show.suffix)   #addar unique endingum inn í settið nyttSett

            #TODO Checka hvort þáttur sé örugglega movie fæll og ef það er movie fæll þá hendir hann í get info og movie
            if True:
                info = getInfo(show)
                #moveFile(show) færum fælinn
    #print(nyttSett)

def getInfo(show):
    return None
    #TODO
    #Get show name, episode nr og season.
    #Ef fællinn er ekki lýsandi á episode nr og season nr þá þurfum við að checka parent folder alveg upp að rótinni á download möppunni.
    #returna nafni, episode nr. og season nr.
    #Ef þetta er ekki þáttur heldur bíómynd eða annað þá skilum við bara episode eða season nr -1 og checkum á því í pirateHelper og sleppum því að færa hann.
def moveFile(nafn, episode, season, dest):
    #TODO
    #Notum þetta til að færa fælinn í destination og eyða gamla þegar við erum búnir að finna allar upplýsingar
    return None
pirateHelper(args.src, args.dst)
