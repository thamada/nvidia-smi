#!/usr/bin/env python3
import argparse

out = '''
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 565.57.01              Driver Version: 565.57.01      CUDA Version: 12.7     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H100 80GB HBM3          On  |   00000000:18:00.0 Off |                    0 |
| N/A   30C    P0            100W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H100 80GB HBM3          On  |   00000000:2A:00.0 Off |                    0 |
| N/A   30C    P0             82W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H100 80GB HBM3          On  |   00000000:3A:00.0 Off |                    0 |
| N/A   31C    P0             85W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H100 80GB HBM3          On  |   00000000:5D:00.0 Off |                    0 |
| N/A   30C    P0             85W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H100 80GB HBM3          On  |   00000000:9A:00.0 Off |                    0 |
| N/A   28C    P0             84W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H100 80GB HBM3          On  |   00000000:AB:00.0 Off |                    0 |
| N/A   30C    P0             85W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H100 80GB HBM3          On  |   00000000:BA:00.0 Off |                    0 |
| N/A   29C    P0             86W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H100 80GB HBM3          On  |   00000000:DB:00.0 Off |                    0 |
| N/A   29C    P0             75W /  700W |       1MiB /  81559MiB |      0%      Default |
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

Timestamp                                 : Thu Nov 14 07:00:14 2024
Driver Version                            : 565.57.01
CUDA Version                              : 12.7

Attached GPUs                             : 8
GPU 00000000:18:00.0
    Product Name                          : NVIDIA H100 80GB HBM3
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
    Serial Number                         : 1654423001593
    GPU UUID                              : GPU-b42dd28e-ffdd-8720-1df0-98bd8cdc05b1
    Minor Number                          : 0
    VBIOS Version                         : 96.00.74.00.01
    MultiGPU Board                        : No
    Board ID                              : 0x1800
    Board Part Number                     : 692-2G520-0200-000
    GPU Part Number                       : 2330-885-A1
    FRU Part Number                       : N/A
    Platform Info
        RACK Serial Number                : N/A
        Chassis Physical Slot Number      : N/A
        Compute Slot Index                : N/A
        Node Index                        : N/A
        Peer Type                         : N/A
        Module Id                         : 2
    Inforom Version
        Image Version                     : G520.0200.00.05
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/11/14 06:25:18.433
        Latest Duration                   : 92243 us
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
    GPU Recovery Action                   : None
    GSP Firmware Version                  : 565.57.01
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x18
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x233010DE
        Bus Id                            : 00000000:18:00.0
        Sub System Id                     : 0x16C110DE
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
        Replays Since Reset               : 7
        Replay Number Rollovers           : 0
        Tx Throughput                     : 567 KB/s
        Rx Throughput                     : 559 KB/s
        Atomic Caps Outbound              : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
        Atomic Caps Inbound               : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
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
        Total                             : 81559 MiB
        Reserved                          : 454 MiB
        Used                              : 1 MiB
        Free                              : 81106 MiB
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
            Max                           : 2560 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 30 C
        GPU T.Limit Temp                  : 57 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 36 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 100.89 W
        Current Power Limit               : 700.00 W
        Requested Power Limit             : 700.00 W
        Default Power Limit               : 700.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 700.00 W
    GPU Memory Power Readings 
        Power Draw                        : 69.61 W
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
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Default Applications Clocks
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1980 MHz
        SM                                : 1980 MHz
        Memory                            : 2619 MHz
        Video                             : 1545 MHz
    Max Customer Boost Clocks
        Graphics                          : 1980 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 685.000 mV
    Fabric
        State                             : Completed
        Status                            : Success
        CliqueId                          : 0
        ClusterUUID                       : 00000000-0000-0000-0000-000000000000
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled

GPU 00000000:2A:00.0
    Product Name                          : NVIDIA H100 80GB HBM3
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
    Serial Number                         : 1654223054577
    GPU UUID                              : GPU-7c3cadbd-17e5-0913-f69b-c618122ea0cd
    Minor Number                          : 1
    VBIOS Version                         : 96.00.74.00.01
    MultiGPU Board                        : No
    Board ID                              : 0x2a00
    Board Part Number                     : 692-2G520-0200-000
    GPU Part Number                       : 2330-885-A1
    FRU Part Number                       : N/A
    Platform Info
        RACK Serial Number                : N/A
        Chassis Physical Slot Number      : N/A
        Compute Slot Index                : N/A
        Node Index                        : N/A
        Peer Type                         : N/A
        Module Id                         : 4
    Inforom Version
        Image Version                     : G520.0200.00.05
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/11/14 06:25:21.764
        Latest Duration                   : 118586 us
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
    GPU Recovery Action                   : None
    GSP Firmware Version                  : 565.57.01
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x2A
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x233010DE
        Bus Id                            : 00000000:2A:00.0
        Sub System Id                     : 0x16C110DE
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
        Tx Throughput                     : 555 KB/s
        Rx Throughput                     : 3874 KB/s
        Atomic Caps Outbound              : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
        Atomic Caps Inbound               : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
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
        Total                             : 81559 MiB
        Reserved                          : 454 MiB
        Used                              : 1 MiB
        Free                              : 81106 MiB
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
            Max                           : 2560 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 30 C
        GPU T.Limit Temp                  : 57 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 36 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 82.81 W
        Current Power Limit               : 700.00 W
        Requested Power Limit             : 700.00 W
        Default Power Limit               : 700.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 700.00 W
    GPU Memory Power Readings 
        Power Draw                        : 50.06 W
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
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Default Applications Clocks
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1980 MHz
        SM                                : 1980 MHz
        Memory                            : 2619 MHz
        Video                             : 1545 MHz
    Max Customer Boost Clocks
        Graphics                          : 1980 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 685.000 mV
    Fabric
        State                             : Completed
        Status                            : Success
        CliqueId                          : 0
        ClusterUUID                       : 00000000-0000-0000-0000-000000000000
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled

GPU 00000000:3A:00.0
    Product Name                          : NVIDIA H100 80GB HBM3
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
    Serial Number                         : 1654423003947
    GPU UUID                              : GPU-2d50cdf6-dd67-9f2e-855e-0d4d6d395a2f
    Minor Number                          : 2
    VBIOS Version                         : 96.00.74.00.01
    MultiGPU Board                        : No
    Board ID                              : 0x3a00
    Board Part Number                     : 692-2G520-0200-000
    GPU Part Number                       : 2330-885-A1
    FRU Part Number                       : N/A
    Platform Info
        RACK Serial Number                : N/A
        Chassis Physical Slot Number      : N/A
        Compute Slot Index                : N/A
        Node Index                        : N/A
        Peer Type                         : N/A
        Module Id                         : 1
    Inforom Version
        Image Version                     : G520.0200.00.05
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/11/14 06:25:19.489
        Latest Duration                   : 95627 us
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
    GPU Recovery Action                   : None
    GSP Firmware Version                  : 565.57.01
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x3A
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x233010DE
        Bus Id                            : 00000000:3A:00.0
        Sub System Id                     : 0x16C110DE
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
        Tx Throughput                     : 574 KB/s
        Rx Throughput                     : 535 KB/s
        Atomic Caps Outbound              : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
        Atomic Caps Inbound               : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
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
        Total                             : 81559 MiB
        Reserved                          : 454 MiB
        Used                              : 1 MiB
        Free                              : 81106 MiB
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
            Max                           : 2560 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 31 C
        GPU T.Limit Temp                  : 56 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 38 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 85.98 W
        Current Power Limit               : 700.00 W
        Requested Power Limit             : 700.00 W
        Default Power Limit               : 700.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 700.00 W
    GPU Memory Power Readings 
        Power Draw                        : 57.65 W
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
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Default Applications Clocks
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1980 MHz
        SM                                : 1980 MHz
        Memory                            : 2619 MHz
        Video                             : 1545 MHz
    Max Customer Boost Clocks
        Graphics                          : 1980 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 670.000 mV
    Fabric
        State                             : Completed
        Status                            : Success
        CliqueId                          : 0
        ClusterUUID                       : 00000000-0000-0000-0000-000000000000
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled

GPU 00000000:5D:00.0
    Product Name                          : NVIDIA H100 80GB HBM3
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
    Serial Number                         : 1654223056472
    GPU UUID                              : GPU-d1838e76-90e6-4408-711d-aeeaa2e1fd14
    Minor Number                          : 3
    VBIOS Version                         : 96.00.74.00.01
    MultiGPU Board                        : No
    Board ID                              : 0x5d00
    Board Part Number                     : 692-2G520-0200-000
    GPU Part Number                       : 2330-885-A1
    FRU Part Number                       : N/A
    Platform Info
        RACK Serial Number                : N/A
        Chassis Physical Slot Number      : N/A
        Compute Slot Index                : N/A
        Node Index                        : N/A
        Peer Type                         : N/A
        Module Id                         : 3
    Inforom Version
        Image Version                     : G520.0200.00.05
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/11/14 06:25:20.372
        Latest Duration                   : 88614 us
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
    GPU Recovery Action                   : None
    GSP Firmware Version                  : 565.57.01
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x5D
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x233010DE
        Bus Id                            : 00000000:5D:00.0
        Sub System Id                     : 0x16C110DE
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
        Tx Throughput                     : 565 KB/s
        Rx Throughput                     : 463 KB/s
        Atomic Caps Outbound              : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
        Atomic Caps Inbound               : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
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
        Total                             : 81559 MiB
        Reserved                          : 454 MiB
        Used                              : 1 MiB
        Free                              : 81106 MiB
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
            Max                           : 2560 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : 58 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 37 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 85.48 W
        Current Power Limit               : 700.00 W
        Requested Power Limit             : 700.00 W
        Default Power Limit               : 700.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 700.00 W
    GPU Memory Power Readings 
        Power Draw                        : 54.51 W
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
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Default Applications Clocks
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1980 MHz
        SM                                : 1980 MHz
        Memory                            : 2619 MHz
        Video                             : 1545 MHz
    Max Customer Boost Clocks
        Graphics                          : 1980 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 670.000 mV
    Fabric
        State                             : Completed
        Status                            : Success
        CliqueId                          : 0
        ClusterUUID                       : 00000000-0000-0000-0000-000000000000
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled

GPU 00000000:9A:00.0
    Product Name                          : NVIDIA H100 80GB HBM3
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
    Serial Number                         : 1654423003267
    GPU UUID                              : GPU-72be6e5d-3c1b-0d37-98ac-d3ef159f2589
    Minor Number                          : 4
    VBIOS Version                         : 96.00.74.00.01
    MultiGPU Board                        : No
    Board ID                              : 0x9a00
    Board Part Number                     : 692-2G520-0200-000
    GPU Part Number                       : 2330-885-A1
    FRU Part Number                       : N/A
    Platform Info
        RACK Serial Number                : N/A
        Chassis Physical Slot Number      : N/A
        Compute Slot Index                : N/A
        Node Index                        : N/A
        Peer Type                         : N/A
        Module Id                         : 6
    Inforom Version
        Image Version                     : G520.0200.00.05
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/11/14 06:25:16.754
        Latest Duration                   : 144264 us
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
    GPU Recovery Action                   : None
    GSP Firmware Version                  : 565.57.01
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x9A
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x233010DE
        Bus Id                            : 00000000:9A:00.0
        Sub System Id                     : 0x16C110DE
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
        Tx Throughput                     : 617 KB/s
        Rx Throughput                     : 567 KB/s
        Atomic Caps Outbound              : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
        Atomic Caps Inbound               : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
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
        Total                             : 81559 MiB
        Reserved                          : 454 MiB
        Used                              : 1 MiB
        Free                              : 81106 MiB
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
            Max                           : 2560 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 28 C
        GPU T.Limit Temp                  : 59 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 36 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 84.94 W
        Current Power Limit               : 700.00 W
        Requested Power Limit             : 700.00 W
        Default Power Limit               : 700.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 700.00 W
    GPU Memory Power Readings 
        Power Draw                        : 52.03 W
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
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Default Applications Clocks
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1980 MHz
        SM                                : 1980 MHz
        Memory                            : 2619 MHz
        Video                             : 1545 MHz
    Max Customer Boost Clocks
        Graphics                          : 1980 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 670.000 mV
    Fabric
        State                             : Completed
        Status                            : Success
        CliqueId                          : 0
        ClusterUUID                       : 00000000-0000-0000-0000-000000000000
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled

GPU 00000000:AB:00.0
    Product Name                          : NVIDIA H100 80GB HBM3
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
    Serial Number                         : 1654323021387
    GPU UUID                              : GPU-52378fbc-3124-3895-13b6-1dd179563e0f
    Minor Number                          : 5
    VBIOS Version                         : 96.00.74.00.01
    MultiGPU Board                        : No
    Board ID                              : 0xab00
    Board Part Number                     : 692-2G520-0200-000
    GPU Part Number                       : 2330-885-A1
    FRU Part Number                       : N/A
    Platform Info
        RACK Serial Number                : N/A
        Chassis Physical Slot Number      : N/A
        Compute Slot Index                : N/A
        Node Index                        : N/A
        Peer Type                         : N/A
        Module Id                         : 8
    Inforom Version
        Image Version                     : G520.0200.00.05
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/11/14 06:25:19.464
        Latest Duration                   : 88375 us
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
    GPU Recovery Action                   : None
    GSP Firmware Version                  : 565.57.01
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xAB
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x233010DE
        Bus Id                            : 00000000:AB:00.0
        Sub System Id                     : 0x16C110DE
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
        Replays Since Reset               : 4
        Replay Number Rollovers           : 0
        Tx Throughput                     : 3534 KB/s
        Rx Throughput                     : 551 KB/s
        Atomic Caps Outbound              : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
        Atomic Caps Inbound               : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
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
        Total                             : 81559 MiB
        Reserved                          : 454 MiB
        Used                              : 1 MiB
        Free                              : 81106 MiB
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
            Max                           : 2560 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 30 C
        GPU T.Limit Temp                  : 57 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 38 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 85.27 W
        Current Power Limit               : 700.00 W
        Requested Power Limit             : 700.00 W
        Default Power Limit               : 700.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 700.00 W
    GPU Memory Power Readings 
        Power Draw                        : 55.82 W
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
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Default Applications Clocks
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1980 MHz
        SM                                : 1980 MHz
        Memory                            : 2619 MHz
        Video                             : 1545 MHz
    Max Customer Boost Clocks
        Graphics                          : 1980 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 670.000 mV
    Fabric
        State                             : Completed
        Status                            : Success
        CliqueId                          : 0
        ClusterUUID                       : 00000000-0000-0000-0000-000000000000
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled

GPU 00000000:BA:00.0
    Product Name                          : NVIDIA H100 80GB HBM3
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
    Serial Number                         : 1654423003872
    GPU UUID                              : GPU-83a5aebb-b71c-c570-aa83-185e1233fe97
    Minor Number                          : 6
    VBIOS Version                         : 96.00.74.00.01
    MultiGPU Board                        : No
    Board ID                              : 0xba00
    Board Part Number                     : 692-2G520-0200-000
    GPU Part Number                       : 2330-885-A1
    FRU Part Number                       : N/A
    Platform Info
        RACK Serial Number                : N/A
        Chassis Physical Slot Number      : N/A
        Compute Slot Index                : N/A
        Node Index                        : N/A
        Peer Type                         : N/A
        Module Id                         : 5
    Inforom Version
        Image Version                     : G520.0200.00.05
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/11/14 06:25:16.547
        Latest Duration                   : 140470 us
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
    GPU Recovery Action                   : None
    GSP Firmware Version                  : 565.57.01
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xBA
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x233010DE
        Bus Id                            : 00000000:BA:00.0
        Sub System Id                     : 0x16C110DE
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
        Replays Since Reset               : 15
        Replay Number Rollovers           : 0
        Tx Throughput                     : 638 KB/s
        Rx Throughput                     : 553 KB/s
        Atomic Caps Outbound              : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
        Atomic Caps Inbound               : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
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
        Total                             : 81559 MiB
        Reserved                          : 454 MiB
        Used                              : 1 MiB
        Free                              : 81106 MiB
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
            Max                           : 2560 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : 54 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 37 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 86.05 W
        Current Power Limit               : 700.00 W
        Requested Power Limit             : 700.00 W
        Default Power Limit               : 700.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 700.00 W
    GPU Memory Power Readings 
        Power Draw                        : 53.23 W
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
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Default Applications Clocks
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1980 MHz
        SM                                : 1980 MHz
        Memory                            : 2619 MHz
        Video                             : 1545 MHz
    Max Customer Boost Clocks
        Graphics                          : 1980 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 670.000 mV
    Fabric
        State                             : Completed
        Status                            : Success
        CliqueId                          : 0
        ClusterUUID                       : 00000000-0000-0000-0000-000000000000
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled

GPU 00000000:DB:00.0
    Product Name                          : NVIDIA H100 80GB HBM3
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
    Serial Number                         : 1654223055370
    GPU UUID                              : GPU-33135771-a848-ece1-b61e-489e221d663c
    Minor Number                          : 7
    VBIOS Version                         : 96.00.74.00.01
    MultiGPU Board                        : No
    Board ID                              : 0xdb00
    Board Part Number                     : 692-2G520-0200-000
    GPU Part Number                       : 2330-885-A1
    FRU Part Number                       : N/A
    Platform Info
        RACK Serial Number                : N/A
        Chassis Physical Slot Number      : N/A
        Compute Slot Index                : N/A
        Node Index                        : N/A
        Peer Type                         : N/A
        Module Id                         : 7
    Inforom Version
        Image Version                     : G520.0200.00.05
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/11/14 06:25:21.448
        Latest Duration                   : 119660 us
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
    GPU Recovery Action                   : None
    GSP Firmware Version                  : 565.57.01
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xDB
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x233010DE
        Bus Id                            : 00000000:DB:00.0
        Sub System Id                     : 0x16C110DE
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
        Tx Throughput                     : 658 KB/s
        Rx Throughput                     : 604 KB/s
        Atomic Caps Outbound              : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
        Atomic Caps Inbound               : FETCHADD_32 FETCHADD_64 SWAP_32 SWAP_64 CAS_32 CAS_64 
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
        Total                             : 81559 MiB
        Reserved                          : 454 MiB
        Used                              : 1 MiB
        Free                              : 81106 MiB
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
            Max                           : 2560 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : 58 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 36 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 75.09 W
        Current Power Limit               : 700.00 W
        Requested Power Limit             : 700.00 W
        Default Power Limit               : 700.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 700.00 W
    GPU Memory Power Readings 
        Power Draw                        : 44.07 W
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
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Default Applications Clocks
        Graphics                          : 1980 MHz
        Memory                            : 2619 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1980 MHz
        SM                                : 1980 MHz
        Memory                            : 2619 MHz
        Video                             : 1545 MHz
    Max Customer Boost Clocks
        Graphics                          : 1980 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 685.000 mV
    Fabric
        State                             : Completed
        Status                            : Success
        CliqueId                          : 0
        ClusterUUID                       : 00000000-0000-0000-0000-000000000000
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled
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

