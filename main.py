import re
import json
from os import listdir
from os.path import isfile, isdir, join
from helper import level_down, copy_to_dst, explore_dst

with open('config.json') as json_file:
    config = json.load(json_file)

mypath = config["Mail-attach-location"];

mailAttchDirs = [join(mypath, f) for f in listdir(mypath) if isdir(join(mypath, f))]

while len(level_down(mailAttchDirs)) > 0:
    mailAttchDirs = level_down(mailAttchDirs)

for dst in config["destination"]:
    explore_dst(dst,mailAttchDirs)