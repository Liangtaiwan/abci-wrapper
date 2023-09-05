# ABCI-SGE-wrapper

ABCI-SGE-wrapper is a convenient wrapper for SGE (Sun Grid Engine), specifically designed for use on the ABCI Cluster. 

For information on using ABCI, please refer to the [official documentation (English)](https://docs.abci.ai/en/) or the [Japanese documentation](https://docs.abci.ai/ja/).

**Note**: While we acknowledge that SGE may have limitations, it is the current choice for ABCI. We hope that ABCI will consider transitioning to SLURM in the future.

## Installation

To get started with ABCI-SGE-wrapper, follow these simple steps:

1. Clone the repository to your preferred location:
   ```sh
   git clone git@github.com:Liangtaiwan/abci-wrapper.git
   mv abci-wrapper $HOME/.wrapper
   ```

2. Add the following lines to your shell configuration file (e.g., `.bashrc` or `.zshrc`):

   ```sh
   export PATH=$PATH:$HOME/.wrapper
   export ABCI_GROUP=<YOUR GROUP ID>
   ```

Replace `<YOUR GROUP ID>` with your actual ABCI group ID.

## Usage

### On-demand Service (Interactive Mode)

The primary mode of ABCI-SGE-wrapper is on-demand service, which acts as a wrapper for the `qrsh` command to submit jobs to the queue. For instance, you can execute a Python script like this:

```sh
qrun python my_script.py
```

You can also use the `-r` option followed by a resource name to specify resource requirements. For example, to allocate a small GPU node, use:

```sh
qrun -r rt_G.small python my_script.py
```

Alternatively, you can specify the GPU type, the number of GPUs, the number of CPUs, and memory size. ABCI-SGE-wrapper will automatically find the resource with the lowest charge coefficient for you. For example:

- To request a node with at least two GPUs, use:

  ```sh
  qrun -g 2 python my_script.py
  ```

  This will use `rt_G.large` as the computation cost.

- To request a node with at least 16 CPUs and 500GB of memory, use:

  ```sh
  qrun -c 32 -m 500 python my_script.py
  ```

  This will use `rt_C.large` as the computation cost.

- To specify a GPU type (e.g., A100), use:

  ```sh
  qrun -G A100 -g 1 python my_script.py
  ```

**Warning**: ABCI does not support custom partial resource requests. We recommend using 1, 4, or 8 GPUs to avoid resource waste.

### Spot Job (Batch/Detach Mode)

You can run a spot job using `qrun` by adding the `-d` argument, eliminating the need to write a separate script. `qrun` will automatically generate a script for you. For example:

```sh
qrun -d python my_script.py
```

The standard output and standard error will be saved in `/scratch/{username}/logs`.

You can retain the generated script by using the `-k` argument:

```sh
qrun -k -d python my_script.py
```

This will create a script named `python_my_script.py_{random_id}.sh` in the current directory.

### Reserved Job

For advanced users, you can use the `-ar` argument with reserved nodes. For details on reserving nodes, please refer to the ABCI user guide.

**Warning**: Reserved jobs are intended for advanced users and can lead to resource waste if not used carefully.

### Multinode Job

For advanced users who require multinode jobs, use the `-n` argument. For example, to run a Python script on 2 nodes, each with one GPU, use:

```sh
qrun -n 2 -g 1 python my_script.py
```

**Warning**: Multinode jobs require expertise in MPI or other parallel tools.

### Singularity Container
To use a Singularity container, use the `-s` argument. For example:

```sh
qrun -s test.sif python my_script.py
```

### Other Options
For more options, please refer to the help message:

```sh
qrun --help
```