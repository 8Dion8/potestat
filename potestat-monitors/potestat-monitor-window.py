import platform
import os
import subprocess

HOSTOS = platform.system()

def get_data():
    if HOSTOS != "Linux":
        raise Exception("yeah windows is not supported yet lol")
        #TODO windows support
    else:
        process = subprocess.Popen(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE)
        window_title = process.stdout.readline().decode('utf-8').strip()
        process.terminate()


    return window_title


if __name__ == '__main__':
    print(get_data())