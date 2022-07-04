import platform
from math import floor

HOSTOS = platform.system()

def get_data():
    if HOSTOS != "Linux":
        raise Exception("yeah windows is not supported yet lol")
        #TODO windows support
    else:
        #TODO obviously very hacky lol
        file_path = "/sys/class/backlight/amdgpu_bl1/brightness"
        backlight_level = floor(int(open(file_path, "r").readline()) / 255 * 100)


    return backlight_level


if __name__ == '__main__':
    print(get_data())