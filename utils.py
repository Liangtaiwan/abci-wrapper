import http.client
import config
import json
import subprocess
from termcolor import colored

def colored_by_ratio(text, ratio, thres=[0.5, 0.999999]):
    if ratio < thres[0]:
        clr = 'green'
    elif ratio < thres[1]:
        clr = 'yellow'
    # elif ratio < thres[2]:
        # clr = 'orange'
    else:
        clr = 'red'
    return colored(text, clr)

def thres_red(text, val, thres=1):
    if val < thres:
        return colored(text, 'red')
    else:
        return colored(text, 'white')

def run_cmd(args):
    if isinstance(args, str):
        args = args.split()
    p = subprocess.run(args, stdout=subprocess.PIPE, check=True)
    return p.stdout.decode().strip()

def uniq(arr):
    # ref: https://mail.python.org/pipermail/python-dev/2017-December/151283.html
    return list(dict.fromkeys(arr))


def find_minimal_match_resource_type(gpu_type, num_gpus, cpu_cores, memory_gb):
    best_match = None
    best_charge_coefficient = float('inf')
    for resource_type in config.resource_types:
        if gpu_type is not None and gpu_type != resource_type["gpu_type"]:
            continue
        if (
            num_gpus <= resource_type["num_gpus"]
            and cpu_cores <= resource_type["cpu_cores"]
            and memory_gb <= resource_type["memory_gb"]
        ):
            charge_coefficient = resource_type["charge_coefficient"]
            if charge_coefficient < best_charge_coefficient:
                best_match = resource_type["name"]
                best_charge_coefficient = charge_coefficient
    return best_match
