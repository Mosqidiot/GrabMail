from os import listdir
from os.path import isfile, isdir, join
import re
from helper import level_down, copy_to_dst



r = re.compile()

mailAttchDirs = [join(mypath, f) for f in listdir(mypath) if isdir(join(mypath, f))]

while len(level_down(mailAttchDirs)) > 0:
    mailAttchDirs = level_down(mailAttchDirs);

# all the diretory contains maill attchments, format in (dir_path, [...attachments])
files = [(d,listdir(d)) for d in mailAttchDirs]
formatted = [(obj[0],list(filter(r.match, obj[1]))) for obj in files if len(list(filter(r.match, obj[1]))) > 0]
copy_to_dst(formatted,rutger_dst)