import sys, os, pathlib, importlib
from datetime import datetime, timedelta, timezone

monitors_path = os.path.join(
    pathlib.Path(__file__).parent.parent, 
    "potestat-monitors"
)

sys.path.append(monitors_path)

def format_data(raw_data, monitor):
    data = {}
    
    data["timestamp"] = str(datetime.now(timezone.utc))
    data["monitor"] = monitor
    data["data"] = raw_data

    return data



def run_monitors():

    monitors = os.listdir(monitors_path)

    for monitor in monitors:
        
        if not monitor.startswith("potestat-monitor"):
            continue

        monitor_lib = importlib.import_module(monitor[:-3])

        data = monitor_lib.get_data()

        formatted_data = format_data(data, monitor[:-3])

        print(formatted_data)



if __name__ == '__main__':
    run_monitors()