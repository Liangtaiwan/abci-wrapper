import config


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
