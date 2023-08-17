import ctypes
from random import randint

kDOMAIN = range(-5, 257)


def deref(addr, typ):
    return ctypes.cast(addr, ctypes.POINTER(typ))


def change_value(old, new):
    try:
        deref(id(old), ctypes.c_int)[6] = new
    except:
        ...  # :)


def main():
    for num in kDOMAIN:
        # 80% chance we dont change it
        if randint(0, 4):
            continue

        new_value = randint(
            kDOMAIN.start, kDOMAIN.stop - 1
        )  # randint is right-inclusive so subtract 1
        print(new_value)
        change_value(old=num, new=new_value)


main()  # run when imported
