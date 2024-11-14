#!/usr/bin/env python3
import argparse

out = '''
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 555.42.02              Driver Version: 555.42.02      CUDA Version: 12.5     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A100-SXM4-80GB          On  |   00000000:68:00.0 Off |                    0 |
| N/A   25C    P0             59W /  500W |       1MiB /  81920MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA A100-SXM4-80GB          On  |   00000000:9E:00.0 Off |                    0 |
| N/A   22C    P0             60W /  500W |       1MiB /  81920MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA A100-SXM4-80GB          On  |   00000000:C2:00.0 Off |                    0 |
| N/A   23C    P0             58W /  500W |       1MiB /  81920MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA A100-SXM4-80GB          On  |   00000000:D4:00.0 Off |                    0 |
| N/A   23C    P0             58W /  500W |       1MiB /  81920MiB |      0%      Default |
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

Timestamp                                 : Thu Nov 14 10:45:47 2024
Driver Version                            : 555.42.02
CUDA Version                              : 12.5

Attached GPUs                             : 4
GPU 00000000:68:00.0
    Product Name                          : NVIDIA A100-SXM4-80GB
    Product Brand                         : NVIDIA
    Product Architecture                  : Ampere
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
    Serial Number                         : 1320222043305
    GPU UUID                              : GPU-31515c3d-1414-7c2c-004a-f86a898946ac
    Minor Number                          : 3
    VBIOS Version                         : 92.00.9E.00.02
    MultiGPU Board                        : No
    Board ID                              : 0x6800
    Board Part Number                     : 692-2G506-0212-005
    GPU Part Number                       : 20B2-896-A1
    FRU Part Number                       : N/A
    Module ID                             : 3
    Inforom Version
        Image Version                     : G506.0212.00.01
        OEM Object                        : 2.0
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/07/10 08:30:24.927
        Latest Duration                   : 93357 us
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
    GSP Firmware Version                  : 555.42.02
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x68
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x20B210DE
        Bus Id                            : 00000000:68:00.0
        Sub System Id                     : 0x147F10DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 4
                Device Current            : 4
                Device Max                : 4
                Host Max                  : 5
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 81920 MiB
        Reserved                          : 763 MiB
        Used                              : 1 MiB
        Free                              : 81158 MiB
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
            Max                           : 640 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 25 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 92 C
        GPU Slowdown Temp                 : 89 C
        GPU Max Operating Temp            : 85 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 43 C
        Memory Max Operating Temp         : 95 C
    GPU Power Readings
        Power Draw                        : 59.77 W
        Current Power Limit               : 500.00 W
        Requested Power Limit             : 500.00 W
        Default Power Limit               : 500.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 500.00 W
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
        Memory                            : 1593 MHz
        Video                             : 585 MHz
    Applications Clocks
        Graphics                          : 1140 MHz
        Memory                            : 1593 MHz
    Default Applications Clocks
        Graphics                          : 1140 MHz
        Memory                            : 1593 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1410 MHz
        SM                                : 1410 MHz
        Memory                            : 1593 MHz
        Video                             : 1290 MHz
    Max Customer Boost Clocks
        Graphics                          : 1410 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 706.250 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled

GPU 00000000:9E:00.0
    Product Name                          : NVIDIA A100-SXM4-80GB
    Product Brand                         : NVIDIA
    Product Architecture                  : Ampere
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
    Serial Number                         : 1321022027867
    GPU UUID                              : GPU-72d87681-01db-370e-567d-41afcf20fad0
    Minor Number                          : 4
    VBIOS Version                         : 92.00.9E.00.02
    MultiGPU Board                        : No
    Board ID                              : 0x9e00
    Board Part Number                     : 692-2G506-0212-005
    GPU Part Number                       : 20B2-896-A1
    FRU Part Number                       : N/A
    Module ID                             : 7
    Inforom Version
        Image Version                     : G506.0212.00.01
        OEM Object                        : 2.0
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
    GSP Firmware Version                  : 555.42.02
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x9E
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x20B210DE
        Bus Id                            : 00000000:9E:00.0
        Sub System Id                     : 0x147F10DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 4
                Device Current            : 4
                Device Max                : 4
                Host Max                  : 5
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 81920 MiB
        Reserved                          : 763 MiB
        Used                              : 1 MiB
        Free                              : 81158 MiB
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
            DRAM Correctable              : 353
            DRAM Uncorrectable            : 0
        Aggregate
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 353
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
        Correctable Error                 : 1
        Uncorrectable Error               : 0
        Pending                           : Yes
        Remapping Failure Occurred        : No
        Bank Remap Availability Histogram
            Max                           : 639 bank(s)
            High                          : 1 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 22 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 92 C
        GPU Slowdown Temp                 : 89 C
        GPU Max Operating Temp            : 85 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 41 C
        Memory Max Operating Temp         : 95 C
    GPU Power Readings
        Power Draw                        : 60.31 W
        Current Power Limit               : 500.00 W
        Requested Power Limit             : 500.00 W
        Default Power Limit               : 500.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 500.00 W
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
        Memory                            : 1593 MHz
        Video                             : 585 MHz
    Applications Clocks
        Graphics                          : 1140 MHz
        Memory                            : 1593 MHz
    Default Applications Clocks
        Graphics                          : 1140 MHz
        Memory                            : 1593 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1410 MHz
        SM                                : 1410 MHz
        Memory                            : 1593 MHz
        Video                             : 1290 MHz
    Max Customer Boost Clocks
        Graphics                          : 1410 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 700.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled

GPU 00000000:C2:00.0
    Product Name                          : NVIDIA A100-SXM4-80GB
    Product Brand                         : NVIDIA
    Product Architecture                  : Ampere
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
    Serial Number                         : 1321022087204
    GPU UUID                              : GPU-62989189-9e1e-ac75-4676-114f14998542
    Minor Number                          : 5
    VBIOS Version                         : 92.00.9E.00.02
    MultiGPU Board                        : No
    Board ID                              : 0xc200
    Board Part Number                     : 692-2G506-0212-005
    GPU Part Number                       : 20B2-896-A1
    FRU Part Number                       : N/A
    Module ID                             : 5
    Inforom Version
        Image Version                     : G506.0212.00.01
        OEM Object                        : 2.0
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
    GSP Firmware Version                  : 555.42.02
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xC2
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x20B210DE
        Bus Id                            : 00000000:C2:00.0
        Sub System Id                     : 0x147F10DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 4
                Device Current            : 4
                Device Max                : 4
                Host Max                  : 5
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 81920 MiB
        Reserved                          : 763 MiB
        Used                              : 1 MiB
        Free                              : 81158 MiB
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
        Correctable Error                 : 1
        Uncorrectable Error               : 0
        Pending                           : No
        Remapping Failure Occurred        : No
        Bank Remap Availability Histogram
            Max                           : 639 bank(s)
            High                          : 1 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 23 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 92 C
        GPU Slowdown Temp                 : 89 C
        GPU Max Operating Temp            : 85 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 40 C
        Memory Max Operating Temp         : 95 C
    GPU Power Readings
        Power Draw                        : 58.78 W
        Current Power Limit               : 500.00 W
        Requested Power Limit             : 500.00 W
        Default Power Limit               : 500.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 500.00 W
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
        Memory                            : 1593 MHz
        Video                             : 585 MHz
    Applications Clocks
        Graphics                          : 1140 MHz
        Memory                            : 1593 MHz
    Default Applications Clocks
        Graphics                          : 1140 MHz
        Memory                            : 1593 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1410 MHz
        SM                                : 1410 MHz
        Memory                            : 1593 MHz
        Video                             : 1290 MHz
    Max Customer Boost Clocks
        Graphics                          : 1410 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 718.750 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled

GPU 00000000:D4:00.0
    Product Name                          : NVIDIA A100-SXM4-80GB
    Product Brand                         : NVIDIA
    Product Architecture                  : Ampere
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
    Serial Number                         : 1321122065002
    GPU UUID                              : GPU-011b2cfe-2b8e-1cb0-19e1-1b764e854dfc
    Minor Number                          : 6
    VBIOS Version                         : 92.00.9E.00.02
    MultiGPU Board                        : No
    Board ID                              : 0xd400
    Board Part Number                     : 692-2G506-0212-005
    GPU Part Number                       : 20B2-896-A1
    FRU Part Number                       : N/A
    Module ID                             : 6
    Inforom Version
        Image Version                     : G506.0212.00.01
        OEM Object                        : 2.0
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : 2024/09/09 14:59:05.032
        Latest Duration                   : 91470 us
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
    GSP Firmware Version                  : 555.42.02
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xD4
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x20B210DE
        Bus Id                            : 00000000:D4:00.0
        Sub System Id                     : 0x147F10DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 4
                Device Current            : 4
                Device Max                : 4
                Host Max                  : 5
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 81920 MiB
        Reserved                          : 763 MiB
        Used                              : 1 MiB
        Free                              : 81158 MiB
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
            Max                           : 640 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 23 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 92 C
        GPU Slowdown Temp                 : 89 C
        GPU Max Operating Temp            : 85 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 39 C
        Memory Max Operating Temp         : 95 C
    GPU Power Readings
        Power Draw                        : 62.21 W
        Current Power Limit               : 500.00 W
        Requested Power Limit             : 500.00 W
        Default Power Limit               : 500.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 500.00 W
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
        Graphics                          : 930 MHz
        SM                                : 930 MHz
        Memory                            : 1593 MHz
        Video                             : 840 MHz
    Applications Clocks
        Graphics                          : 1140 MHz
        Memory                            : 1593 MHz
    Default Applications Clocks
        Graphics                          : 1140 MHz
        Memory                            : 1593 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1410 MHz
        SM                                : 1410 MHz
        Memory                            : 1593 MHz
        Video                             : 1290 MHz
    Max Customer Boost Clocks
        Graphics                          : 1410 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 725.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled
'''

def main():
    parser = argparse.ArgumentParser(description="nvidia-smi simulator")
    parser.add_argument('-a', action='store_true', help="simulate nvidia-smi -a")
    args = parser.parse_args()

    if args.a:
        print(out_a)
    else:
        print(out)

