import getpass
import http.client
from urllib.parse import urlencode
import os
import json


#TODO: Need to customize the following
resources = [
    'rt_F',
    'rt_G.large',
    'rt_G.small',
    'rt_C.large',
    'rt_C.small',
    'rt_AF',
    'rt_AG.small',
    'rt_M.large',
    'rt_M.small',
]

# Define the resource types in the specified format
resource_types = [
    {
        "name": "rt_F",
        "description": "node-exclusive",
        "gpu_type": "V100",
        "cpu_cores": 40,
        "num_gpus": 4,
        "memory_gb": 360,
        "storage_gb": 1440,
        "charge_coefficient": 1.00,
    },
    {
        "name": "rt_G.large",
        "description": "node-sharing with GPU",
        "gpu_type": "V100",
        "cpu_cores": 20,
        "num_gpus": 4,
        "memory_gb": 240,
        "storage_gb": 720,
        "charge_coefficient": 0.90,
    },
    {
        "name": "rt_G.small",
        "description": "node-sharing with GPU",
        "gpu_type": "V100",
        "cpu_cores": 5,
        "num_gpus": 1,
        "memory_gb": 60,
        "storage_gb": 180,
        "charge_coefficient": 0.30,
    },
    {
        "name": "rt_C.large",
        "description": "node-sharing CPU only",
        "gpu_type": None,
        "cpu_cores": 20,
        "num_gpus": 0,
        "memory_gb": 120,
        "storage_gb": 720,
        "charge_coefficient": 0.60,
    },
    {
        "name": "rt_C.small",
        "description": "node-sharing CPU only",
        "gpu_type": None,
        "cpu_cores": 5,
        "num_gpus": 0,
        "memory_gb": 30,
        "storage_gb": 180,
        "charge_coefficient": 0.20,
    },
    {
        "name": "rt_AF",
        "description": "node-exclusive",
        "gpu_type": "A100",
        "cpu_cores": 72,
        "num_gpus": 8,
        "memory_gb": 480,
        "storage_gb": 34401,
        "charge_coefficient": 3.00,
    },
    {
        "name": "rt_AG.small",
        "description": "node-sharing with GPU",
        "gpu_type": "A100",
        "cpu_cores": 9,
        "num_gpus": 1,
        "memory_gb": 60,
        "storage_gb": 390,
        "charge_coefficient": 0.50,
    },
    {
        "name": "rt_M.large",
        "description": "node-sharing",
        "gpu_type": None,
        "cpu_cores": 8,
        "num_gpus": 0,
        "memory_gb": 800,
        "storage_gb": 480,
        "charge_coefficient": 0.40,
    },
    {
        "name": "rt_M.small",
        "description": "node-sharing",
        "gpu_type": None,
        "cpu_cores": 4,
        "num_gpus": 0,
        "memory_gb": 400,
        "storage_gb": 240,
        "charge_coefficient": 0.20,
    },
]

