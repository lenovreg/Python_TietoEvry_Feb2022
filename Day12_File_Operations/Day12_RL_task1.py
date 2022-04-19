import os  # system library
import string
import collections
from datetime import datetime as dt  # datetime has datetime submodule(klase)
from pathlib import Path  # this is newer for path manipulation

# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file
# check file_line_len ("veidenbaums.txt") -> should be 971 or 972
def file_line_len(fpath):
    count_lines=0
    not_empty_lines=0
    to_find="\n"
    with open(fpath, encoding="utf-8") as my_file:
        for line in my_file:
            if to_find in line:
                count_lines+=1
                if len(line.strip()) > 0:
                    not_empty_lines+=1
    return(f'Lines in file: {count_lines=}, not empty lines: {not_empty_lines=}')

# 1b -> write the function get_poem_lines (fpath), which returns a list with only those lines that contain poetry.
# So we want to avoid/filter out those lines that contain whitespace and also those lines with poem titles.
# PS preferably use encoding = "utf-8"

def get_poem_lines(fpath):
    needle='*'
    with open(fpath, encoding="utf-8") as my_file:
        filtered_lines = []
        for line in my_file:
            if not needle in line:
                if not len(line.strip())==0:
                    filtered_lines.append(line.rstrip())
        return filtered_lines
# 1c -> write the function save_lines (destpath, lines)
# This function will store all lines into destpath file

def save_lines(destpath, lines):

    if destpath.is_file():  # this is offered by Path from standard library module pathlib
        print(f"Sorry {destpath} exists, so not going to overwrite")  # should be very rare once a year ...
    else:
        with open(destpath, mode="w", encoding="utf-8") as file_out:
            print(f"Writing {len(lines)} lines into {file_path}")
            file_out.writelines("\n".join(lines))
# 1e -> write the function clean_punkts (srcpath, destpath)
# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation
# then function will save the cleaned text into destpath

def clean_punkts(srcpath, destpath):
    needle=string.punctuation
    with open(srcpath, encoding="utf-8") as my_file:
        filtered_lines = []
        for line in my_file:
            #print(type(line))
            new_line=""
            for c in line:
                if c not in needle:
                    new_line+=c
            filtered_lines.append(new_line)
    if destpath.is_file():  # this is offered by Path from standard library module pathlib
        print(f"Sorry {destpath} exists, so not going to overwrite")  # should be very rare once a year ...
    else:
        with open(destpath, mode="w", encoding="utf-8") as file_out:
            print(f"Writing {len(filtered_lines)} lines into {destpath}")
            file_out.writelines(filtered_lines)
    return(filtered_lines)

def get_word_usage(srcpath, destpath):
    c=collections.Counter()
    print(f'Initial: {c}')
    with open(srcpath, encoding="utf-8") as my_file:
        text = my_file.read().split()
        new_text=[]
        print(text)
        for word in text:
            new_text.append(word.lower())
    c = collections.Counter(new_text)
    if destpath.is_file():  # this is offered by Path from standard library module pathlib
        print(f"Sorry {destpath} exists, so not going to overwrite")  # should be very rare once a year ...
    else:
        with open(destpath, mode="w", encoding="utf-8") as file_out:
            print(f"Writing {len(c.most_common())} lines into {destpath}")
            file_out.write('vards   skaits')
            for vards, skaits in c.most_common():
                file_out.write(vards + '    ' + str(skaits))
    #         file_out.write(filtered_lines)

    # print(c.most_common())
    # for vards, skaits in c.most_common():
    #     print(vards+' ' +str(skaits))
    # print(c)

    #         print(f"Writing {len(filtered_lines)} lines into {destpath}")
    #         file_out.write(filtered_lines)
    return c
my_file = Path("veidenbaums.txt")
print(my_file)
print(file_line_len(my_file))
print(get_poem_lines(my_file))


file_path = Path("veid_poems.txt")
#1d save_lines
save_lines(file_path,get_poem_lines(my_file))
#file_path = Path(f"frost_{needle}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.txt")
dest_path=Path("cleaned_veidenbaums.txt")
#1e
print(clean_punkts(my_file,dest_path))
#1f
dest_path_counts=Path("count_words.txt")
print(get_word_usage(dest_path,dest_path_counts))

