#!/usr/bin/env python3

out = '''
Found 1 devices
hipSetDevice(0): (^o^)v 
=============================================================
[GPU 0] AMD Instinct MI300X
-------------------------------------------------------------
[GPU 0] gfx942:sramecc+:xnack-: AMD GCN Arch Name
[GPU 0] 2100.00: Max clock frequency of the multi-processors in MHz
[GPU 0] 304: Number of multi-processors(Compute Units: CUs)
[GPU 0] 1.30: Max global memory clock frequency in GHz
[GPU 0] 8192: Global memory bus width in bits
[GPU 0] 21299.2: Memory bandwidth in GB/s
[GPU 0] 196592: Total Global Memory (MB)
[GPU 0] 2047: Constant Memory (MB)
[GPU 0] 64: Shared Memory / Block (kB)
[GPU 0] 65536: Registers / Block
[GPU 0] 64: Warp size
[GPU 0] 2147483647: memPitch
[GPU 0] 1024: maxThreads/Block
[GPU 0] (1024, 1024, 1024): maxThreads/Block(X,Y,Z)
[GPU 0] (2147483647, 65536, 65536): max grid dimensions(XYZ)
[GPU 0] 1: Check whether HIP can map host memory
[GPU 0] 1: Device can possibly execute multiple kernels concurrently
[GPU 0] 0: Device has ECC support enabled
[GPU 0] 5: PCI Bus ID
[GPU 0] 0: PCI Device ID
[GPU 0] 0: PCI Domain ID
[GPU 0] 0: TCC(Tesla Compute Cluster) driver mode
[GPU 0] 8: Number of async engines
[GPU 0] 0: Does device and host share unified address space
[GPU 0] 33554432: L2 cache size
[GPU 0] 33554432: Device's max L2 persisting lines in bytes
[GPU 0] 2048: Maximum resident threads per multi-processor
[GPU 0] 65536: Maximum Shared Memory per multi-processor
[GPU 0] 1000.00: Frequency in MHz of the timer used by the device-side clock instructions
[GPU 0] 0: Is cluster launch supported on the device
[GPU 0] 0: Is compute preemption supported on the device
[GPU 0] 1: Is concurrent multiple kernels execution supported on the device
[GPU 0] 1: Can the GPU coherently access managed memory concurrently with the CPU
[GPU 0] 1: Does the GPU support cooperative launch
[GPU 0] 1: Does the GPU support cooperative launch on multiple devices
[GPU 0] 0: Indicates device support of RDMA APIs
[GPU 0] 1: Check whether GPU is a large PCI bar device
[GPU 0] 0: Is the device on a multi-GPU board
[GPU 0] 1: Revision of the GPU in this device
[GPU 0] 960cff6be1be8723: UUID of this device
[GPU 0] 1: 64-bit double-precision floating-point
[GPU 0] 1: 64-bit integer atomics for shared memory
[GPU 0] 1: 64-bit integer atomics for global memory
[GPU 0] 0: Dynamic parallelism
'''

def main():
    print(out)

