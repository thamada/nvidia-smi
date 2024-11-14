#!/usr/bin/env python3
import argparse

out = '''
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.127.05             Driver Version: 550.127.05     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:01:00.0 Off |                  Off |
| 30%   30C    P8             23W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:25:00.0 Off |                  Off |
| 30%   30C    P8             18W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:41:00.0 Off |                  Off |
| 30%   30C    P8             20W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:61:00.0 Off |                  Off |
| 30%   30C    P8             26W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:81:00.0 Off |                  Off |
| 30%   29C    P8             22W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:A1:00.0 Off |                  Off |
| 30%   29C    P8             29W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:C1:00.0 Off |                  Off |
| 30%   29C    P8             47W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:E1:00.0 Off |                  Off |
| 30%   29C    P8             21W /  300W |       2MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
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

Timestamp                                 : Thu Nov 14 10:19:08 2024
Driver Version                            : 550.127.05
CUDA Version                              : 12.4

Attached GPUs                             : 8
GPU 00000000:01:00.0
    Product Name                          : NVIDIA RTX 6000 Ada Generation
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ada Lovelace
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1714123005421
    GPU UUID                              : GPU-6130ccb8-7d66-5560-15ea-9a2a08dc87e7
    Minor Number                          : 3
    VBIOS Version                         : 95.02.59.00.09
    MultiGPU Board                        : No
    Board ID                              : 0x100
    Board Part Number                     : 900-5G133-2250-000
    GPU Part Number                       : 26B1-870-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0510.00.02
        OEM Object                        : 2.1
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x01
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x0
        Device Id                         : 0x26B110DE
        Bus Id                            : 00000000:01:00.0
        Sub System Id                     : 0x16A110DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 1
                Device Current            : 1
                Device Max                : 4
                Host Max                  : 4
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 0 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
    Performance State                     : P8
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 49140 MiB
        Reserved                          : 500 MiB
        Used                              : 2 MiB
        Free                              : 48639 MiB
    BAR1 Memory Usage
        Total                             : 256 MiB
        Used                              : 2 MiB
        Free                              : 254 MiB
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
        Current                           : Disabled
        Pending                           : Disabled
    ECC Errors
        Volatile
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
        Aggregate
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
            SRAM Threshold Exceeded       : N/A
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : N/A
            SRAM SM                       : N/A
            SRAM Microcontroller          : N/A
            SRAM PCIE                     : N/A
            SRAM Other                    : N/A
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
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 30 C
        GPU T.Limit Temp                  : 61 C
        GPU Shutdown T.Limit Temp         : -7 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : 85 C
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Power Draw                        : 23.83 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 210 MHz
        SM                                : 210 MHz
        Memory                            : 405 MHz
        Video                             : 1185 MHz
    Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Default Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 3105 MHz
        SM                                : 3105 MHz
        Memory                            : 10001 MHz
        Video                             : 2415 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 915.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:25:00.0
    Product Name                          : NVIDIA RTX 6000 Ada Generation
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ada Lovelace
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1714123005048
    GPU UUID                              : GPU-0914e825-1cec-966a-8040-31c8e276cea9
    Minor Number                          : 2
    VBIOS Version                         : 95.02.59.00.09
    MultiGPU Board                        : No
    Board ID                              : 0x2500
    Board Part Number                     : 900-5G133-2250-000
    GPU Part Number                       : 26B1-870-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0510.00.02
        OEM Object                        : 2.1
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x25
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x0
        Device Id                         : 0x26B110DE
        Bus Id                            : 00000000:25:00.0
        Sub System Id                     : 0x16A110DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 1
                Device Current            : 1
                Device Max                : 4
                Host Max                  : 4
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 50 KB/s
        Rx Throughput                     : 0 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
    Performance State                     : P8
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 49140 MiB
        Reserved                          : 500 MiB
        Used                              : 2 MiB
        Free                              : 48639 MiB
    BAR1 Memory Usage
        Total                             : 256 MiB
        Used                              : 2 MiB
        Free                              : 254 MiB
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
        Current                           : Disabled
        Pending                           : Disabled
    ECC Errors
        Volatile
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
        Aggregate
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
            SRAM Threshold Exceeded       : N/A
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : N/A
            SRAM SM                       : N/A
            SRAM Microcontroller          : N/A
            SRAM PCIE                     : N/A
            SRAM Other                    : N/A
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
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 30 C
        GPU T.Limit Temp                  : 60 C
        GPU Shutdown T.Limit Temp         : -7 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : 85 C
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Power Draw                        : 18.03 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 210 MHz
        SM                                : 210 MHz
        Memory                            : 405 MHz
        Video                             : 1185 MHz
    Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Default Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 3105 MHz
        SM                                : 3105 MHz
        Memory                            : 10001 MHz
        Video                             : 2415 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 915.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:41:00.0
    Product Name                          : NVIDIA RTX 6000 Ada Generation
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ada Lovelace
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1714123004885
    GPU UUID                              : GPU-87528235-5e93-1cdd-345e-532e881cd837
    Minor Number                          : 1
    VBIOS Version                         : 95.02.59.00.09
    MultiGPU Board                        : No
    Board ID                              : 0x4100
    Board Part Number                     : 900-5G133-2250-000
    GPU Part Number                       : 26B1-870-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0510.00.02
        OEM Object                        : 2.1
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x41
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x0
        Device Id                         : 0x26B110DE
        Bus Id                            : 00000000:41:00.0
        Sub System Id                     : 0x16A110DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 1
                Device Current            : 1
                Device Max                : 4
                Host Max                  : 4
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 50 KB/s
        Rx Throughput                     : 50 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
    Performance State                     : P8
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 49140 MiB
        Reserved                          : 500 MiB
        Used                              : 2 MiB
        Free                              : 48639 MiB
    BAR1 Memory Usage
        Total                             : 256 MiB
        Used                              : 2 MiB
        Free                              : 254 MiB
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
        Current                           : Disabled
        Pending                           : Disabled
    ECC Errors
        Volatile
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
        Aggregate
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
            SRAM Threshold Exceeded       : N/A
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : N/A
            SRAM SM                       : N/A
            SRAM Microcontroller          : N/A
            SRAM PCIE                     : N/A
            SRAM Other                    : N/A
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
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 30 C
        GPU T.Limit Temp                  : 61 C
        GPU Shutdown T.Limit Temp         : -7 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : 85 C
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Power Draw                        : 19.88 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 210 MHz
        SM                                : 210 MHz
        Memory                            : 405 MHz
        Video                             : 1185 MHz
    Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Default Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 3105 MHz
        SM                                : 3105 MHz
        Memory                            : 10001 MHz
        Video                             : 2415 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 915.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:61:00.0
    Product Name                          : NVIDIA RTX 6000 Ada Generation
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ada Lovelace
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1714123005820
    GPU UUID                              : GPU-8f83d358-bd12-41cf-f018-b87ecad2448c
    Minor Number                          : 0
    VBIOS Version                         : 95.02.59.00.09
    MultiGPU Board                        : No
    Board ID                              : 0x6100
    Board Part Number                     : 900-5G133-2250-000
    GPU Part Number                       : 26B1-870-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0510.00.02
        OEM Object                        : 2.1
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x61
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x0
        Device Id                         : 0x26B110DE
        Bus Id                            : 00000000:61:00.0
        Sub System Id                     : 0x16A110DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 1
                Device Current            : 1
                Device Max                : 4
                Host Max                  : 4
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 0 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
    Performance State                     : P8
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 49140 MiB
        Reserved                          : 500 MiB
        Used                              : 2 MiB
        Free                              : 48639 MiB
    BAR1 Memory Usage
        Total                             : 256 MiB
        Used                              : 2 MiB
        Free                              : 254 MiB
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
        Current                           : Disabled
        Pending                           : Disabled
    ECC Errors
        Volatile
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
        Aggregate
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
            SRAM Threshold Exceeded       : N/A
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : N/A
            SRAM SM                       : N/A
            SRAM Microcontroller          : N/A
            SRAM PCIE                     : N/A
            SRAM Other                    : N/A
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
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 30 C
        GPU T.Limit Temp                  : 61 C
        GPU Shutdown T.Limit Temp         : -7 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : 85 C
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Power Draw                        : 26.88 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 210 MHz
        SM                                : 210 MHz
        Memory                            : 405 MHz
        Video                             : 1185 MHz
    Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Default Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 3105 MHz
        SM                                : 3105 MHz
        Memory                            : 10001 MHz
        Video                             : 2415 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 910.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:81:00.0
    Product Name                          : NVIDIA RTX 6000 Ada Generation
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ada Lovelace
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1714123005330
    GPU UUID                              : GPU-dac548a9-d8a2-cf89-39cd-a3ae9305257b
    Minor Number                          : 7
    VBIOS Version                         : 95.02.59.00.09
    MultiGPU Board                        : No
    Board ID                              : 0x8100
    Board Part Number                     : 900-5G133-2250-000
    GPU Part Number                       : 26B1-870-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0510.00.02
        OEM Object                        : 2.1
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x81
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x0
        Device Id                         : 0x26B110DE
        Bus Id                            : 00000000:81:00.0
        Sub System Id                     : 0x16A110DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 1
                Device Current            : 1
                Device Max                : 4
                Host Max                  : 4
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 50 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
    Performance State                     : P8
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 49140 MiB
        Reserved                          : 500 MiB
        Used                              : 2 MiB
        Free                              : 48639 MiB
    BAR1 Memory Usage
        Total                             : 256 MiB
        Used                              : 2 MiB
        Free                              : 254 MiB
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
        Current                           : Disabled
        Pending                           : Disabled
    ECC Errors
        Volatile
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
        Aggregate
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
            SRAM Threshold Exceeded       : N/A
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : N/A
            SRAM SM                       : N/A
            SRAM Microcontroller          : N/A
            SRAM PCIE                     : N/A
            SRAM Other                    : N/A
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
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : 62 C
        GPU Shutdown T.Limit Temp         : -7 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : 85 C
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Power Draw                        : 22.93 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 210 MHz
        SM                                : 210 MHz
        Memory                            : 405 MHz
        Video                             : 1185 MHz
    Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Default Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 3105 MHz
        SM                                : 3105 MHz
        Memory                            : 10001 MHz
        Video                             : 2415 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 920.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:A1:00.0
    Product Name                          : NVIDIA RTX 6000 Ada Generation
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ada Lovelace
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1714123005857
    GPU UUID                              : GPU-e5f9fdf4-ddd7-0218-81e7-9823cb971e19
    Minor Number                          : 6
    VBIOS Version                         : 95.02.59.00.09
    MultiGPU Board                        : No
    Board ID                              : 0xa100
    Board Part Number                     : 900-5G133-2250-000
    GPU Part Number                       : 26B1-870-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0510.00.02
        OEM Object                        : 2.1
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xA1
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x0
        Device Id                         : 0x26B110DE
        Bus Id                            : 00000000:A1:00.0
        Sub System Id                     : 0x16A110DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 1
                Device Current            : 1
                Device Max                : 4
                Host Max                  : 4
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 50 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
    Performance State                     : P8
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 49140 MiB
        Reserved                          : 500 MiB
        Used                              : 2 MiB
        Free                              : 48639 MiB
    BAR1 Memory Usage
        Total                             : 256 MiB
        Used                              : 2 MiB
        Free                              : 254 MiB
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
        Current                           : Disabled
        Pending                           : Disabled
    ECC Errors
        Volatile
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
        Aggregate
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
            SRAM Threshold Exceeded       : N/A
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : N/A
            SRAM SM                       : N/A
            SRAM Microcontroller          : N/A
            SRAM PCIE                     : N/A
            SRAM Other                    : N/A
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
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : 62 C
        GPU Shutdown T.Limit Temp         : -7 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : 85 C
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Power Draw                        : 29.12 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 210 MHz
        SM                                : 210 MHz
        Memory                            : 405 MHz
        Video                             : 1185 MHz
    Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Default Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 3105 MHz
        SM                                : 3105 MHz
        Memory                            : 10001 MHz
        Video                             : 2415 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 915.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:C1:00.0
    Product Name                          : NVIDIA RTX 6000 Ada Generation
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ada Lovelace
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1714123005707
    GPU UUID                              : GPU-18895fa1-247d-05f8-a7d7-929ee49fb131
    Minor Number                          : 5
    VBIOS Version                         : 95.02.59.00.09
    MultiGPU Board                        : No
    Board ID                              : 0xc100
    Board Part Number                     : 900-5G133-2250-000
    GPU Part Number                       : 26B1-870-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0510.00.02
        OEM Object                        : 2.1
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xC1
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x0
        Device Id                         : 0x26B110DE
        Bus Id                            : 00000000:C1:00.0
        Sub System Id                     : 0x16A110DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 1
                Device Current            : 1
                Device Max                : 4
                Host Max                  : 4
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 50 KB/s
        Rx Throughput                     : 50 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
    Performance State                     : P8
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 49140 MiB
        Reserved                          : 500 MiB
        Used                              : 2 MiB
        Free                              : 48639 MiB
    BAR1 Memory Usage
        Total                             : 256 MiB
        Used                              : 2 MiB
        Free                              : 254 MiB
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
        Current                           : Disabled
        Pending                           : Disabled
    ECC Errors
        Volatile
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
        Aggregate
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
            SRAM Threshold Exceeded       : N/A
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : N/A
            SRAM SM                       : N/A
            SRAM Microcontroller          : N/A
            SRAM PCIE                     : N/A
            SRAM Other                    : N/A
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
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : 61 C
        GPU Shutdown T.Limit Temp         : -7 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : 85 C
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Power Draw                        : 47.41 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 210 MHz
        SM                                : 210 MHz
        Memory                            : 405 MHz
        Video                             : 1185 MHz
    Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Default Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 3105 MHz
        SM                                : 3105 MHz
        Memory                            : 10001 MHz
        Video                             : 2415 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 920.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:E1:00.0
    Product Name                          : NVIDIA RTX 6000 Ada Generation
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ada Lovelace
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1714123005564
    GPU UUID                              : GPU-16791b1a-38de-bc9c-6a07-cdb9e95e91cd
    Minor Number                          : 4
    VBIOS Version                         : 95.02.59.00.09
    MultiGPU Board                        : No
    Board ID                              : 0xe100
    Board Part Number                     : 900-5G133-2250-000
    GPU Part Number                       : 26B1-870-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0510.00.02
        OEM Object                        : 2.1
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xE1
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x0
        Device Id                         : 0x26B110DE
        Bus Id                            : 00000000:E1:00.0
        Sub System Id                     : 0x16A110DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 1
                Device Current            : 1
                Device Max                : 4
                Host Max                  : 4
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 0 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
    Performance State                     : P8
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 49140 MiB
        Reserved                          : 500 MiB
        Used                              : 2 MiB
        Free                              : 48639 MiB
    BAR1 Memory Usage
        Total                             : 256 MiB
        Used                              : 2 MiB
        Free                              : 254 MiB
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
        Current                           : Disabled
        Pending                           : Disabled
    ECC Errors
        Volatile
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
        Aggregate
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
            SRAM Threshold Exceeded       : N/A
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : N/A
            SRAM SM                       : N/A
            SRAM Microcontroller          : N/A
            SRAM PCIE                     : N/A
            SRAM Other                    : N/A
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
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : 61 C
        GPU Shutdown T.Limit Temp         : -7 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : 85 C
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Power Draw                        : 21.62 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 210 MHz
        SM                                : 210 MHz
        Memory                            : 405 MHz
        Video                             : 1185 MHz
    Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Default Applications Clocks
        Graphics                          : 2505 MHz
        Memory                            : 10001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 3105 MHz
        SM                                : 3105 MHz
        Memory                            : 10001 MHz
        Video                             : 2415 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 915.000 mV
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
    parser = argparse.ArgumentParser(description="nvidia-smi simulator")
    parser.add_argument('-a', action='store_true', help="simulate nvidia-smi -a")
    args = parser.parse_args()

    if args.a:
        print(out_a)
    else:
        print(out)

