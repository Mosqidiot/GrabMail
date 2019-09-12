
from os import listdir
from os.path import isfile, isdir, join
import re
from shutil import copy2

def level_down (input_path):
    mypath = input_path
    out = []
    for f in mypath:
        for d in listdir(f):
            if isdir(join(f, d)):
                out.append(join(f, d))
    return out

# copy file tuple to destination 
def copy_to_dst (f_list, dst):
    for f_tuple in f_list:
        first_part = f_tuple[0];
        filenam_list = f_tuple[1];
        for f in filenam_list:
            copy2(join(first_part,f), dst)