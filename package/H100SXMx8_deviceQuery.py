#!/usr/bin/env python3
import argparse

out = '''
deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 8 CUDA Capable device(s)

Device 0: "NVIDIA H100 80GB HBM3"
  CUDA Driver Version / Runtime Version          12.7 / 12.4
  CUDA Capability Major/Minor version number:    9.0
  Total amount of global memory:                 81106 MBytes (85045477376 bytes)
  (132) Multiprocessors, (128) CUDA Cores/MP:    16896 CUDA Cores
  GPU Max Clock rate:                            1980 MHz (1.98 GHz)
  Memory Clock rate:                             2619 Mhz
  Memory Bus Width:                              5120-bit
  L2 Cache Size:                                 52428800 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        233472 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 24 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 1: "NVIDIA H100 80GB HBM3"
  CUDA Driver Version / Runtime Version          12.7 / 12.4
  CUDA Capability Major/Minor version number:    9.0
  Total amount of global memory:                 81106 MBytes (85045477376 bytes)
  (132) Multiprocessors, (128) CUDA Cores/MP:    16896 CUDA Cores
  GPU Max Clock rate:                            1980 MHz (1.98 GHz)
  Memory Clock rate:                             2619 Mhz
  Memory Bus Width:                              5120-bit
  L2 Cache Size:                                 52428800 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        233472 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 42 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 2: "NVIDIA H100 80GB HBM3"
  CUDA Driver Version / Runtime Version          12.7 / 12.4
  CUDA Capability Major/Minor version number:    9.0
  Total amount of global memory:                 81106 MBytes (85045477376 bytes)
  (132) Multiprocessors, (128) CUDA Cores/MP:    16896 CUDA Cores
  GPU Max Clock rate:                            1980 MHz (1.98 GHz)
  Memory Clock rate:                             2619 Mhz
  Memory Bus Width:                              5120-bit
  L2 Cache Size:                                 52428800 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        233472 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 58 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 3: "NVIDIA H100 80GB HBM3"
  CUDA Driver Version / Runtime Version          12.7 / 12.4
  CUDA Capability Major/Minor version number:    9.0
  Total amount of global memory:                 81106 MBytes (85045477376 bytes)
  (132) Multiprocessors, (128) CUDA Cores/MP:    16896 CUDA Cores
  GPU Max Clock rate:                            1980 MHz (1.98 GHz)
  Memory Clock rate:                             2619 Mhz
  Memory Bus Width:                              5120-bit
  L2 Cache Size:                                 52428800 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        233472 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 93 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 4: "NVIDIA H100 80GB HBM3"
  CUDA Driver Version / Runtime Version          12.7 / 12.4
  CUDA Capability Major/Minor version number:    9.0
  Total amount of global memory:                 81106 MBytes (85045477376 bytes)
  (132) Multiprocessors, (128) CUDA Cores/MP:    16896 CUDA Cores
  GPU Max Clock rate:                            1980 MHz (1.98 GHz)
  Memory Clock rate:                             2619 Mhz
  Memory Bus Width:                              5120-bit
  L2 Cache Size:                                 52428800 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        233472 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 154 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 5: "NVIDIA H100 80GB HBM3"
  CUDA Driver Version / Runtime Version          12.7 / 12.4
  CUDA Capability Major/Minor version number:    9.0
  Total amount of global memory:                 81106 MBytes (85045477376 bytes)
  (132) Multiprocessors, (128) CUDA Cores/MP:    16896 CUDA Cores
  GPU Max Clock rate:                            1980 MHz (1.98 GHz)
  Memory Clock rate:                             2619 Mhz
  Memory Bus Width:                              5120-bit
  L2 Cache Size:                                 52428800 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        233472 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 171 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 6: "NVIDIA H100 80GB HBM3"
  CUDA Driver Version / Runtime Version          12.7 / 12.4
  CUDA Capability Major/Minor version number:    9.0
  Total amount of global memory:                 81106 MBytes (85045477376 bytes)
  (132) Multiprocessors, (128) CUDA Cores/MP:    16896 CUDA Cores
  GPU Max Clock rate:                            1980 MHz (1.98 GHz)
  Memory Clock rate:                             2619 Mhz
  Memory Bus Width:                              5120-bit
  L2 Cache Size:                                 52428800 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        233472 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 186 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 7: "NVIDIA H100 80GB HBM3"
  CUDA Driver Version / Runtime Version          12.7 / 12.4
  CUDA Capability Major/Minor version number:    9.0
  Total amount of global memory:                 81106 MBytes (85045477376 bytes)
  (132) Multiprocessors, (128) CUDA Cores/MP:    16896 CUDA Cores
  GPU Max Clock rate:                            1980 MHz (1.98 GHz)
  Memory Clock rate:                             2619 Mhz
  Memory Bus Width:                              5120-bit
  L2 Cache Size:                                 52428800 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        233472 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 3 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 219 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >
> Peer access from NVIDIA H100 80GB HBM3 (GPU0) -> NVIDIA H100 80GB HBM3 (GPU1) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU0) -> NVIDIA H100 80GB HBM3 (GPU2) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU0) -> NVIDIA H100 80GB HBM3 (GPU3) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU0) -> NVIDIA H100 80GB HBM3 (GPU4) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU0) -> NVIDIA H100 80GB HBM3 (GPU5) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU0) -> NVIDIA H100 80GB HBM3 (GPU6) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU0) -> NVIDIA H100 80GB HBM3 (GPU7) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU1) -> NVIDIA H100 80GB HBM3 (GPU0) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU1) -> NVIDIA H100 80GB HBM3 (GPU2) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU1) -> NVIDIA H100 80GB HBM3 (GPU3) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU1) -> NVIDIA H100 80GB HBM3 (GPU4) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU1) -> NVIDIA H100 80GB HBM3 (GPU5) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU1) -> NVIDIA H100 80GB HBM3 (GPU6) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU1) -> NVIDIA H100 80GB HBM3 (GPU7) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU2) -> NVIDIA H100 80GB HBM3 (GPU0) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU2) -> NVIDIA H100 80GB HBM3 (GPU1) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU2) -> NVIDIA H100 80GB HBM3 (GPU3) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU2) -> NVIDIA H100 80GB HBM3 (GPU4) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU2) -> NVIDIA H100 80GB HBM3 (GPU5) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU2) -> NVIDIA H100 80GB HBM3 (GPU6) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU2) -> NVIDIA H100 80GB HBM3 (GPU7) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU3) -> NVIDIA H100 80GB HBM3 (GPU0) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU3) -> NVIDIA H100 80GB HBM3 (GPU1) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU3) -> NVIDIA H100 80GB HBM3 (GPU2) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU3) -> NVIDIA H100 80GB HBM3 (GPU4) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU3) -> NVIDIA H100 80GB HBM3 (GPU5) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU3) -> NVIDIA H100 80GB HBM3 (GPU6) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU3) -> NVIDIA H100 80GB HBM3 (GPU7) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU4) -> NVIDIA H100 80GB HBM3 (GPU0) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU4) -> NVIDIA H100 80GB HBM3 (GPU1) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU4) -> NVIDIA H100 80GB HBM3 (GPU2) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU4) -> NVIDIA H100 80GB HBM3 (GPU3) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU4) -> NVIDIA H100 80GB HBM3 (GPU5) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU4) -> NVIDIA H100 80GB HBM3 (GPU6) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU4) -> NVIDIA H100 80GB HBM3 (GPU7) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU5) -> NVIDIA H100 80GB HBM3 (GPU0) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU5) -> NVIDIA H100 80GB HBM3 (GPU1) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU5) -> NVIDIA H100 80GB HBM3 (GPU2) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU5) -> NVIDIA H100 80GB HBM3 (GPU3) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU5) -> NVIDIA H100 80GB HBM3 (GPU4) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU5) -> NVIDIA H100 80GB HBM3 (GPU6) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU5) -> NVIDIA H100 80GB HBM3 (GPU7) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU6) -> NVIDIA H100 80GB HBM3 (GPU0) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU6) -> NVIDIA H100 80GB HBM3 (GPU1) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU6) -> NVIDIA H100 80GB HBM3 (GPU2) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU6) -> NVIDIA H100 80GB HBM3 (GPU3) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU6) -> NVIDIA H100 80GB HBM3 (GPU4) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU6) -> NVIDIA H100 80GB HBM3 (GPU5) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU6) -> NVIDIA H100 80GB HBM3 (GPU7) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU7) -> NVIDIA H100 80GB HBM3 (GPU0) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU7) -> NVIDIA H100 80GB HBM3 (GPU1) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU7) -> NVIDIA H100 80GB HBM3 (GPU2) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU7) -> NVIDIA H100 80GB HBM3 (GPU3) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU7) -> NVIDIA H100 80GB HBM3 (GPU4) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU7) -> NVIDIA H100 80GB HBM3 (GPU5) : Yes
> Peer access from NVIDIA H100 80GB HBM3 (GPU7) -> NVIDIA H100 80GB HBM3 (GPU6) : Yes

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 12.7, CUDA Runtime Version = 12.4, NumDevs = 8
Result = PASS
'''

def main():
    print(out)
