import os  # system library
import string
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
    return(count_lines, not_empty_lines)
my_file = Path("veidenbaums.txt")
print(my_file)
print(file_line_len(my_file))
