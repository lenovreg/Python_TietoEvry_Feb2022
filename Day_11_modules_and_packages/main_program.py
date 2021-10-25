import sys  # this is a module from Python standard library
import os  # operating system
# generally you want to import Python standard stuff first before moving onto our modules
# import my_mod

# import my_mod as mm # so typically we can create a short two-three letter alias for our module
# from my_mod import add  # for those times when you are sure there are no name collisions
# from my_mod import PI
# from my_mod import add as my_add # custom name for those cases when you want a single import but have a name collision
# from my_mod import * # THIS IS BAD PRACTICE !! leads to name collission and might not actually import everything

# import my_pkg.my_utils
# import my_pkg.subp.sub_utils
# import my_pkg.subp.sub_utils as su  # so import from subpackage a particular module with a different name
# from my_pkg.subp.sub_utils import sub_add
from my_pkg.subp.sub_utils import sub_add as add  # so import a specific function/calls/variable and alias it


# from sub_map import prod_tools as u1_g2


def main():
    print("running main_program.py residing at", __file__)
    print("of course __name__ is main...", __name__)
    # print(my_mod.add(5, 10))
    # print(my_mod.mlist)
    # print(my_mod.txt)
    # new_garage = my_mod.Garage("LNB")
    # print(new_garage.gname)
    print("Python version", sys.version_info)
    print("Python will look for modules in order of:", "\n".join(sys.path))
    print("Current working directory is", os.getcwd())
    print("OS is ", os.name)
    # so how does Python search for modules
    # print(mm.add(1100,333))
    # print(mm.PI)
    # print(add(100,200))
    # print(PI)
    # print(my_add(10,50))
    # print(my_pkg.my_utils.util_add(50, 10))
    # my_pkg.subp.sub_utils.subadd(30, 22)  #kind of long if you have to write it often
    # su.sub_add(30,20,2000)
    # sub_add(25, 20)
    add(10, 2, 5)
    # we put calls to other functions here
    # initialize/config function(s)
    # do stuff function(s)
    # cleanup function(s)


# if main_program was import main_program then the next part would no run
# so called main guard
if __name__ == "__main__":
    main()
