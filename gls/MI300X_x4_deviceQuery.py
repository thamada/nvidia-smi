#!/usr/bin/env python3

out = '''
Found 4 devices
hipSetDevice(0): (^o^)v 
hipSetDevice(1): (^o^)v 
hipSetDevice(2): (^o^)v 
hipSetDevice(3): (^o^)v 
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
[GPU 0] 38: PCI Bus ID
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
[GPU 0] 8d1457e2c20f59d2: UUID of this device
[GPU 0] 1: 64-bit double-precision floating-point
[GPU 0] 1: 64-bit integer atomics for shared memory
[GPU 0] 1: 64-bit integer atomics for global memory
[GPU 0] 0: Dynamic parallelism
=============================================================
[GPU 1] AMD Instinct MI300X
-------------------------------------------------------------
[GPU 1] gfx942:sramecc+:xnack-: AMD GCN Arch Name
[GPU 1] 2100.00: Max clock frequency of the multi-processors in MHz
[GPU 1] 304: Number of multi-processors(Compute Units: CUs)
[GPU 1] 1.30: Max global memory clock frequency in GHz
[GPU 1] 8192: Global memory bus width in bits
[GPU 1] 21299.2: Memory bandwidth in GB/s
[GPU 1] 196592: Total Global Memory (MB)
[GPU 1] 2047: Constant Memory (MB)
[GPU 1] 64: Shared Memory / Block (kB)
[GPU 1] 65536: Registers / Block
[GPU 1] 64: Warp size
[GPU 1] 2147483647: memPitch
[GPU 1] 1024: maxThreads/Block
[GPU 1] (1024, 1024, 1024): maxThreads/Block(X,Y,Z)
[GPU 1] (2147483647, 65536, 65536): max grid dimensions(XYZ)
[GPU 1] 1: Check whether HIP can map host memory
[GPU 1] 1: Device can possibly execute multiple kernels concurrently
[GPU 1] 0: Device has ECC support enabled
[GPU 1] 70: PCI Bus ID
[GPU 1] 0: PCI Device ID
[GPU 1] 0: PCI Domain ID
[GPU 1] 0: TCC(Tesla Compute Cluster) driver mode
[GPU 1] 8: Number of async engines
[GPU 1] 0: Does device and host share unified address space
[GPU 1] 33554432: L2 cache size
[GPU 1] 33554432: Device's max L2 persisting lines in bytes
[GPU 1] 2048: Maximum resident threads per multi-processor
[GPU 1] 65536: Maximum Shared Memory per multi-processor
[GPU 1] 1000.00: Frequency in MHz of the timer used by the device-side clock instructions
[GPU 1] 0: Is cluster launch supported on the device
[GPU 1] 0: Is compute preemption supported on the device
[GPU 1] 1: Is concurrent multiple kernels execution supported on the device
[GPU 1] 1: Can the GPU coherently access managed memory concurrently with the CPU
[GPU 1] 1: Does the GPU support cooperative launch
[GPU 1] 1: Does the GPU support cooperative launch on multiple devices
[GPU 1] 0: Indicates device support of RDMA APIs
[GPU 1] 1: Check whether GPU is a large PCI bar device
[GPU 1] 0: Is the device on a multi-GPU board
[GPU 1] 1: Revision of the GPU in this device
[GPU 1] b4fa34630e85d42a: UUID of this device
[GPU 1] 1: 64-bit double-precision floating-point
[GPU 1] 1: 64-bit integer atomics for shared memory
[GPU 1] 1: 64-bit integer atomics for global memory
[GPU 1] 0: Dynamic parallelism
=============================================================
[GPU 2] AMD Instinct MI300X
-------------------------------------------------------------
[GPU 2] gfx942:sramecc+:xnack-: AMD GCN Arch Name
[GPU 2] 2100.00: Max clock frequency of the multi-processors in MHz
[GPU 2] 304: Number of multi-processors(Compute Units: CUs)
[GPU 2] 1.30: Max global memory clock frequency in GHz
[GPU 2] 8192: Global memory bus width in bits
[GPU 2] 21299.2: Memory bandwidth in GB/s
[GPU 2] 196592: Total Global Memory (MB)
[GPU 2] 2047: Constant Memory (MB)
[GPU 2] 64: Shared Memory / Block (kB)
[GPU 2] 65536: Registers / Block
[GPU 2] 64: Warp size
[GPU 2] 2147483647: memPitch
[GPU 2] 1024: maxThreads/Block
[GPU 2] (1024, 1024, 1024): maxThreads/Block(X,Y,Z)
[GPU 2] (2147483647, 65536, 65536): max grid dimensions(XYZ)
[GPU 2] 1: Check whether HIP can map host memory
[GPU 2] 1: Device can possibly execute multiple kernels concurrently
[GPU 2] 0: Device has ECC support enabled
[GPU 2] 101: PCI Bus ID
[GPU 2] 0: PCI Device ID
[GPU 2] 0: PCI Domain ID
[GPU 2] 0: TCC(Tesla Compute Cluster) driver mode
[GPU 2] 8: Number of async engines
[GPU 2] 0: Does device and host share unified address space
[GPU 2] 33554432: L2 cache size
[GPU 2] 33554432: Device's max L2 persisting lines in bytes
[GPU 2] 2048: Maximum resident threads per multi-processor
[GPU 2] 65536: Maximum Shared Memory per multi-processor
[GPU 2] 1000.00: Frequency in MHz of the timer used by the device-side clock instructions
[GPU 2] 0: Is cluster launch supported on the device
[GPU 2] 0: Is compute preemption supported on the device
[GPU 2] 1: Is concurrent multiple kernels execution supported on the device
[GPU 2] 1: Can the GPU coherently access managed memory concurrently with the CPU
[GPU 2] 1: Does the GPU support cooperative launch
[GPU 2] 1: Does the GPU support cooperative launch on multiple devices
[GPU 2] 0: Indicates device support of RDMA APIs
[GPU 2] 1: Check whether GPU is a large PCI bar device
[GPU 2] 0: Is the device on a multi-GPU board
[GPU 2] 1: Revision of the GPU in this device
[GPU 2] e8986800e182538a: UUID of this device
[GPU 2] 1: 64-bit double-precision floating-point
[GPU 2] 1: 64-bit integer atomics for shared memory
[GPU 2] 1: 64-bit integer atomics for global memory
[GPU 2] 0: Dynamic parallelism
=============================================================
[GPU 3] AMD Instinct MI300X
-------------------------------------------------------------
[GPU 3] gfx942:sramecc+:xnack-: AMD GCN Arch Name
[GPU 3] 2100.00: Max clock frequency of the multi-processors in MHz
[GPU 3] 304: Number of multi-processors(Compute Units: CUs)
[GPU 3] 1.30: Max global memory clock frequency in GHz
[GPU 3] 8192: Global memory bus width in bits
[GPU 3] 21299.2: Memory bandwidth in GB/s
[GPU 3] 196592: Total Global Memory (MB)
[GPU 3] 2047: Constant Memory (MB)
[GPU 3] 64: Shared Memory / Block (kB)
[GPU 3] 65536: Registers / Block
[GPU 3] 64: Warp size
[GPU 3] 2147483647: memPitch
[GPU 3] 1024: maxThreads/Block
[GPU 3] (1024, 1024, 1024): maxThreads/Block(X,Y,Z)
[GPU 3] (2147483647, 65536, 65536): max grid dimensions(XYZ)
[GPU 3] 1: Check whether HIP can map host memory
[GPU 3] 1: Device can possibly execute multiple kernels concurrently
[GPU 3] 0: Device has ECC support enabled
[GPU 3] 133: PCI Bus ID
[GPU 3] 0: PCI Device ID
[GPU 3] 0: PCI Domain ID
[GPU 3] 0: TCC(Tesla Compute Cluster) driver mode
[GPU 3] 8: Number of async engines
[GPU 3] 0: Does device and host share unified address space
[GPU 3] 33554432: L2 cache size
[GPU 3] 33554432: Device's max L2 persisting lines in bytes
[GPU 3] 2048: Maximum resident threads per multi-processor
[GPU 3] 65536: Maximum Shared Memory per multi-processor
[GPU 3] 1000.00: Frequency in MHz of the timer used by the device-side clock instructions
[GPU 3] 0: Is cluster launch supported on the device
[GPU 3] 0: Is compute preemption supported on the device
[GPU 3] 1: Is concurrent multiple kernels execution supported on the device
[GPU 3] 1: Can the GPU coherently access managed memory concurrently with the CPU
[GPU 3] 1: Does the GPU support cooperative launch
[GPU 3] 1: Does the GPU support cooperative launch on multiple devices
[GPU 3] 0: Indicates device support of RDMA APIs
[GPU 3] 1: Check whether GPU is a large PCI bar device
[GPU 3] 0: Is the device on a multi-GPU board
[GPU 3] 1: Revision of the GPU in this device
[GPU 3] eff71edc82169115: UUID of this device
[GPU 3] 1: 64-bit double-precision floating-point
[GPU 3] 1: 64-bit integer atomics for shared memory
[GPU 3] 1: 64-bit integer atomics for global memory
[GPU 3] 0: Dynamic parallelism
'''

def main():
    print(out)

