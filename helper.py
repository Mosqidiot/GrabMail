
from os import listdir
from os.path import isfile, isdir, join
import re
from shutil import copy2

# grab directories under input path


def level_down(input_path):
    mypath = input_path
    out = []
    for f in mypath:
        for d in listdir(f):
            if isdir(join(f, d)):
                out.append(join(f, d))
    return out

# copy file tuple to destination


def copy_to_dst(f_list, dst):
    for f_tuple in f_list:
        first_part = f_tuple[0]
        filenam_list = f_tuple[1]
        for f in filenam_list:
            copy2(join(first_part, f), dst)

# input a destination obj


def explore_dst(dst_obj, mailAttchDirs):

    r = re.compile(dst_obj["reg-exp"])
    print(dst_obj["reg-exp"])
    # all the diretory contains mail attchments, format in (dir_path, [...attachments])
    files = [(d, listdir(d)) for d in mailAttchDirs]

    print(r.match("Samples_Received_ABCD Main study_20190905_162026.CSV"))
    formatted = [(obj[0], list(filter(r.match, obj[1])))
                for obj in files if len(list(filter(r.match, obj[1]))) > 0]
    copy_to_dst(formatted, dst_obj["location"])
