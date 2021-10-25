import my_mod
# import my_mod as new_mod
# from my_mod import add
# import my_pkg.my_utils
# import my_pkg.subp.sub_utils
# import my_pkg.subp.sub_utils as su
# from my_pkg.subp.sub_utils import subadd
# from my_mod import * # THIS IS BAD PRACTICE !! leads to name collission and might not actually import everything


# from sub_map import prod_tools as u1_g2


def main():
    print("running main_program.py ", __file__)
    my_mod.add(5, 10)
    # new_mod.add(1100,333)
    # add(100,200)
    # my_pkg.my_utils.add(50, 10)
    # my_pkg.subp.sub_utils.subadd(30, 22)
    # su.subadd(30,20,2000)
    # subadd(25, 20)
    # we put calls to other functions here
    # initialize/config function(s)
    # do stuff function(s)
    # cleanup function(s)


if __name__ == "__main__":
    main()
