#!/usr/bin/env python3
import argparse

out = '''
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.14              Driver Version: 550.54.14      CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H100 NVL                On  |   00000000:AD:00.0 Off |                    0 |
| N/A   32C    P0             61W /  310W |       0MiB /  95830MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H100 NVL                On  |   00000000:AE:00.0 Off |                    0 |
| N/A   31C    P0             62W /  310W |       0MiB /  95830MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
'''

out_a = '''
==============NVSMI LOG==============

Timestamp                                 : Thu Nov 14 15:35:07 2024
Driver Version                            : 550.54.14
CUDA Version                              : 12.4

Attached GPUs                             : 2
GPU 00000000:AD:00.0
    Product Name                          : NVIDIA H100 NVL
    Product Brand                         : NVIDIA
    Product Architecture                  : Hopper
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : Disabled
        Pending                           : Disabled
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1650724004565
    GPU UUID                              : GPU-806f8ea2-6428-1096-a076-bb687fb45fb0
    Minor Number                          : 4
    VBIOS Version                         : 96.00.74.00.11
    MultiGPU Board                        : No
    Board ID                              : 0xad00
    Board Part Number                     : 900-21010-0020-000
    GPU Part Number                       : 2321-886-A1
    FRU Part Number                       : N/A
    Module ID                             : 4
    Inforom Version
        Image Version                     : 1010.0210.00.02
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/11/13 22:03:47.226
        Latest Duration                   : 135912 us
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : Disabled
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : 550.54.14
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xAD
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x232110DE
        Bus Id                            : 00000000:AD:00.0
        Sub System Id                     : 0x183910DE
        GPU Link Info
            PCIe Generation
                Max                       : 5
                Current                   : 5
                Device Current            : 5
                Device Max                : 5
                Host Max                  : 5
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 727 KB/s
        Rx Throughput                     : 525 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
    Fan Speed                             : N/A
    Performance State                     : P0
    Clocks Event Reasons
        Idle                              : Active
        Applications Clocks Setting       : Not Active
        SW Power Cap                      : Not Active
        HW Slowdown                       : Not Active
            HW Thermal Slowdown           : Not Active
            HW Power Brake Slowdown       : Not Active
        Sync Boost                        : Not Active
        SW Thermal Slowdown               : Not Active
        Display Clock Setting             : Not Active
    Sparse Operation Mode                 : Disabled
    FB Memory Usage
        Total                             : 95830 MiB
        Reserved                          : 594 MiB
        Used                              : 0 MiB
        Free                              : 95235 MiB
    BAR1 Memory Usage
        Total                             : 131072 MiB
        Used                              : 1 MiB
        Free                              : 131071 MiB
    Conf Compute Protected Memory Usage
        Total                             : 0 MiB
        Used                              : 0 MiB
        Free                              : 0 MiB
    Compute Mode                          : Default
    Utilization
        Gpu                               : 0 %
        Memory                            : 0 %
        Encoder                           : 0 %
        Decoder                           : 0 %
        JPEG                              : 0 %
        OFA                               : 0 %
    Encoder Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    FBC Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    ECC Mode
        Current                           : Enabled
        Pending                           : Enabled
    ECC Errors
        Volatile
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 0
            DRAM Uncorrectable            : 0
        Aggregate
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 0
            DRAM Uncorrectable            : 0
            SRAM Threshold Exceeded       : No
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : 0
            SRAM SM                       : 0
            SRAM Microcontroller          : 0
            SRAM PCIE                     : 0
            SRAM Other                    : 0
    Retired Pages
        Single Bit ECC                    : N/A
        Double Bit ECC                    : N/A
        Pending Page Blacklist            : N/A
    Remapped Rows
        Correctable Error                 : 0
        Uncorrectable Error               : 0
        Pending                           : No
        Remapping Failure Occurred        : No
        Bank Remap Availability Histogram
            Max                           : 3072 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 32 C
        GPU T.Limit Temp                  : 55 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 40 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 61.62 W
        Current Power Limit               : 310.00 W
        Requested Power Limit             : 310.00 W
        Default Power Limit               : 310.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 400.00 W
    GPU Memory Power Readings 
        Power Draw                        : N/A
    Module Power Readings
        Power Draw                        : N/A
        Current Power Limit               : N/A
        Requested Power Limit             : N/A
        Default Power Limit               : N/A
        Min Power Limit                   : N/A
        Max Power Limit                   : N/A
    Clocks
        Graphics                          : 345 MHz
        SM                                : 345 MHz
        Memory                            : 2619 MHz
        Video                             : 765 MHz
    Applications Clocks
        Graphics                          : 1785 MHz
        Memory                            : 2619 MHz
    Default Applications Clocks
        Graphics                          : 1785 MHz
        Memory                            : 2619 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1785 MHz
        SM                                : 1785 MHz
        Memory                            : 2619 MHz
        Video                             : 1410 MHz
    Max Customer Boost Clocks
        Graphics                          : 1785 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 705.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:AE:00.0
    Product Name                          : NVIDIA H100 NVL
    Product Brand                         : NVIDIA
    Product Architecture                  : Hopper
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : Disabled
        Pending                           : Disabled
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1650924002357
    GPU UUID                              : GPU-db6d02a2-1413-eccf-8a17-d99eac29d365
    Minor Number                          : 5
    VBIOS Version                         : 96.00.74.00.11
    MultiGPU Board                        : No
    Board ID                              : 0xae00
    Board Part Number                     : 900-21010-0020-000
    GPU Part Number                       : 2321-886-A1
    FRU Part Number                       : N/A
    Module ID                             : 4
    Inforom Version
        Image Version                     : 1010.0210.00.02
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/11/14 05:51:19.230
        Latest Duration                   : 91759 us
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : Disabled
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : 550.54.14
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xAE
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x232110DE
        Bus Id                            : 00000000:AE:00.0
        Sub System Id                     : 0x183910DE
        GPU Link Info
            PCIe Generation
                Max                       : 5
                Current                   : 5
                Device Current            : 5
                Device Max                : 5
                Host Max                  : 5
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 640 KB/s
        Rx Throughput                     : 601 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
    Fan Speed                             : N/A
    Performance State                     : P0
    Clocks Event Reasons
        Idle                              : Active
        Applications Clocks Setting       : Not Active
        SW Power Cap                      : Not Active
        HW Slowdown                       : Not Active
            HW Thermal Slowdown           : Not Active
            HW Power Brake Slowdown       : Not Active
        Sync Boost                        : Not Active
        SW Thermal Slowdown               : Not Active
        Display Clock Setting             : Not Active
    Sparse Operation Mode                 : Disabled
    FB Memory Usage
        Total                             : 95830 MiB
        Reserved                          : 594 MiB
        Used                              : 0 MiB
        Free                              : 95235 MiB
    BAR1 Memory Usage
        Total                             : 131072 MiB
        Used                              : 1 MiB
        Free                              : 131071 MiB
    Conf Compute Protected Memory Usage
        Total                             : 0 MiB
        Used                              : 0 MiB
        Free                              : 0 MiB
    Compute Mode                          : Default
    Utilization
        Gpu                               : 0 %
        Memory                            : 0 %
        Encoder                           : 0 %
        Decoder                           : 0 %
        JPEG                              : 0 %
        OFA                               : 0 %
    Encoder Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    FBC Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    ECC Mode
        Current                           : Enabled
        Pending                           : Enabled
    ECC Errors
        Volatile
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 0
            DRAM Uncorrectable            : 0
        Aggregate
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 0
            DRAM Uncorrectable            : 0
            SRAM Threshold Exceeded       : No
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : 0
            SRAM SM                       : 0
            SRAM Microcontroller          : 0
            SRAM PCIE                     : 0
            SRAM Other                    : 0
    Retired Pages
        Single Bit ECC                    : N/A
        Double Bit ECC                    : N/A
        Pending Page Blacklist            : N/A
    Remapped Rows
        Correctable Error                 : 0
        Uncorrectable Error               : 0
        Pending                           : No
        Remapping Failure Occurred        : No
        Bank Remap Availability Histogram
            Max                           : 3072 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 31 C
        GPU T.Limit Temp                  : 55 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 40 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 62.11 W
        Current Power Limit               : 310.00 W
        Requested Power Limit             : 310.00 W
        Default Power Limit               : 310.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 400.00 W
    GPU Memory Power Readings 
        Power Draw                        : N/A
    Module Power Readings
        Power Draw                        : N/A
        Current Power Limit               : N/A
        Requested Power Limit             : N/A
        Default Power Limit               : N/A
        Min Power Limit                   : N/A
        Max Power Limit                   : N/A
    Clocks
        Graphics                          : 345 MHz
        SM                                : 345 MHz
        Memory                            : 2619 MHz
        Video                             : 765 MHz
    Applications Clocks
        Graphics                          : 1785 MHz
        Memory                            : 2619 MHz
    Default Applications Clocks
        Graphics                          : 1785 MHz
        Memory                            : 2619 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1785 MHz
        SM                                : 1785 MHz
        Memory                            : 2619 MHz
        Video                             : 1410 MHz
    Max Customer Boost Clocks
        Graphics                          : 1785 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 690.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None
'''

def main():
    # ArgumentParserのインスタンスを作成
    parser = argparse.ArgumentParser(description="nvidia-smi simulator")

    # -a 引数（例: フラグとして使用するオプション）
    parser.add_argument('-a', action='store_true', help="simulate nvidia-smi -a")

    # 引数をパース
    args = parser.parse_args()

    # 引数に基づいた処理
    if args.a:
        print(out_a)
    else:
        print(out)

