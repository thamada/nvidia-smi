#!/usr/bin/env python3
import argparse

out = '''
========================================= ROCm System Management Interface =========================================
=================================================== Concise Info ===================================================
Device  [Model : Revision]    Temp        Power     Partitions      SCLK    MCLK    Fan  Perf  PwrCap  VRAM%  GPU%  
        Name (20 chars)       (Junction)  (Socket)  (Mem, Compute)                                                  
====================================================================================================================
0       [0x74a1 : 0x00]       35.0°C      133.0W    NPS1, SPX       131Mhz  900Mhz  0%   auto  750.0W    0%   0%    
        AMD Instinct MI300X                                                                                         
1       [0x74a1 : 0x00]       37.0°C      131.0W    NPS1, SPX       132Mhz  900Mhz  0%   auto  750.0W    0%   0%    
        AMD Instinct MI300X                                                                                         
2       [0x74a1 : 0x00]       34.0°C      131.0W    NPS1, SPX       132Mhz  900Mhz  0%   auto  750.0W    0%   0%    
        AMD Instinct MI300X                                                                                         
3       [0x74a1 : 0x00]       38.0°C      137.0W    NPS1, SPX       131Mhz  900Mhz  0%   auto  750.0W    0%   0%    
        AMD Instinct MI300X                                                                                         
====================================================================================================================
=============================================== End of ROCm SMI Log ================================================
'''

out_a = '''


============================ ROCm System Management Interface ============================
============================== Version of System Component ===============================
Driver version: 6.7.0
==========================================================================================
=========================================== ID ===========================================
GPU[0]		: Device ID: 0x74a1
GPU[0]		: Device Rev: 0x0
GPU[1]		: Device ID: 0x74a1
GPU[1]		: Device Rev: 0x0
GPU[2]		: Device ID: 0x74a1
GPU[2]		: Device Rev: 0x0
GPU[3]		: Device ID: 0x74a1
GPU[3]		: Device Rev: 0x0
==========================================================================================
======================================= Unique ID ========================================
GPU[0]		: Unique ID: 0x8d1457e2c20f59d2
GPU[1]		: Unique ID: 0xb4fa34630e85d42a
GPU[2]		: Unique ID: 0xe8986800e182538a
GPU[3]		: Unique ID: 0xeff71edc82169115
==========================================================================================
========================================= VBIOS ==========================================
GPU[0]		: VBIOS version: 113-MI3SRIOV-001
GPU[1]		: VBIOS version: 113-MI3SRIOV-001
GPU[2]		: VBIOS version: 113-MI3SRIOV-001
GPU[3]		: VBIOS version: 113-MI3SRIOV-001
==========================================================================================
====================================== Temperature =======================================
GPU[0]		: Temperature (Sensor junction) (C): 35.0
GPU[0]		: Temperature (Sensor memory) (C): 33.0
GPU[1]		: Temperature (Sensor junction) (C): 37.0
GPU[1]		: Temperature (Sensor memory) (C): 34.0
GPU[2]		: Temperature (Sensor junction) (C): 34.0
GPU[2]		: Temperature (Sensor memory) (C): 32.0
GPU[3]		: Temperature (Sensor junction) (C): 39.0
GPU[3]		: Temperature (Sensor memory) (C): 36.0
==========================================================================================
=============================== Current clock frequencies ================================
GPU[0]		: fclk clock level: 0: (1300Mhz)
GPU[0]		: mclk clock level: 0: (900Mhz)
GPU[0]		: sclk clock level: S: (137Mhz)
GPU[0]		: socclk clock level: S: (30Mhz)
GPU[1]		: fclk clock level: 0: (1300Mhz)
GPU[1]		: mclk clock level: 0: (900Mhz)
GPU[1]		: sclk clock level: S: (133Mhz)
GPU[1]		: socclk clock level: S: (30Mhz)
GPU[2]		: fclk clock level: 0: (1300Mhz)
GPU[2]		: mclk clock level: 0: (900Mhz)
GPU[2]		: sclk clock level: 1: (141Mhz)
GPU[2]		: socclk clock level: S: (30Mhz)
GPU[3]		: fclk clock level: 0: (1300Mhz)
GPU[3]		: mclk clock level: 0: (900Mhz)
GPU[3]		: sclk clock level: S: (132Mhz)
GPU[3]		: socclk clock level: S: (30Mhz)
==========================================================================================
=================================== Current Fan Metric ===================================
GPU[0]		: Not supported
GPU[1]		: Not supported
GPU[2]		: Not supported
GPU[3]		: Not supported
==========================================================================================
================================= Show Performance Level =================================
GPU[0]		: Performance Level: auto
GPU[1]		: Performance Level: auto
GPU[2]		: Performance Level: auto
GPU[3]		: Performance Level: auto
==========================================================================================
==================================== OverDrive Level =====================================
GPU[0]		: get_overdrive_level_sclk, Not supported on the given system
GPU[1]		: get_overdrive_level_sclk, Not supported on the given system
GPU[2]		: get_overdrive_level_sclk, Not supported on the given system
GPU[3]		: get_overdrive_level_sclk, Not supported on the given system
==========================================================================================
==================================== OverDrive Level =====================================
GPU[0]		: get_mem_overdrive_level_mclk, Not supported on the given system
GPU[1]		: get_mem_overdrive_level_mclk, Not supported on the given system
GPU[2]		: get_mem_overdrive_level_mclk, Not supported on the given system
GPU[3]		: get_mem_overdrive_level_mclk, Not supported on the given system
==========================================================================================
======================================= Power Cap ========================================
GPU[0]		: Max Graphics Package Power (W): 750.0
GPU[1]		: Max Graphics Package Power (W): 750.0
GPU[2]		: Max Graphics Package Power (W): 750.0
GPU[3]		: Max Graphics Package Power (W): 750.0
==========================================================================================
================================== Show Power Profiles ===================================
GPU[0]		: get_power_profiles, Not supported on the given system
GPU[1]		: get_power_profiles, Not supported on the given system
GPU[2]		: get_power_profiles, Not supported on the given system
GPU[3]		: get_power_profiles, Not supported on the given system
==========================================================================================
=================================== Power Consumption ====================================
GPU[0]		: Current Socket Graphics Package Power (W): 133.0
GPU[1]		: Current Socket Graphics Package Power (W): 130.0
GPU[2]		: Current Socket Graphics Package Power (W): 131.0
GPU[3]		: Current Socket Graphics Package Power (W): 136.0
==========================================================================================
============================== Supported clock frequencies ===============================
GPU[0]		: 
GPU[0]		: Supported fclk frequencies on GPU0
GPU[0]		: 0: 1300Mhz *
GPU[0]		: 1: 1550Mhz
GPU[0]		: 2: 1800Mhz
GPU[0]		: 
GPU[0]		: Supported mclk frequencies on GPU0
GPU[0]		: 0: 900Mhz *
GPU[0]		: 1: 1100Mhz
GPU[0]		: 2: 1300Mhz
GPU[0]		: 
GPU[0]		: Supported sclk frequencies on GPU0
GPU[0]		: 0: 500Mhz
GPU[0]		: 1: 142Mhz *
GPU[0]		: 2: 2100Mhz
GPU[0]		: 
GPU[0]		: Supported socclk frequencies on GPU0
GPU[0]		: S: 30Mhz *
GPU[0]		: 0: 889Mhz
GPU[0]		: 1: 1000Mhz
GPU[0]		: 2: 1143Mhz
GPU[0]		: 
GPU[0]		: 
------------------------------------------------------------------------------------------
GPU[1]		: 
GPU[1]		: Supported fclk frequencies on GPU1
GPU[1]		: 0: 1300Mhz *
GPU[1]		: 1: 1550Mhz
GPU[1]		: 2: 1800Mhz
GPU[1]		: 
GPU[1]		: Supported mclk frequencies on GPU1
GPU[1]		: 0: 900Mhz *
GPU[1]		: 1: 1100Mhz
GPU[1]		: 2: 1300Mhz
GPU[1]		: 
GPU[1]		: Supported sclk frequencies on GPU1
GPU[1]		: S: 133Mhz *
GPU[1]		: 0: 500Mhz
GPU[1]		: 1: 2100Mhz
GPU[1]		: 
GPU[1]		: Supported socclk frequencies on GPU1
GPU[1]		: S: 30Mhz *
GPU[1]		: 0: 889Mhz
GPU[1]		: 1: 1000Mhz
GPU[1]		: 2: 1143Mhz
GPU[1]		: 
GPU[1]		: 
------------------------------------------------------------------------------------------
GPU[2]		: 
GPU[2]		: Supported fclk frequencies on GPU2
GPU[2]		: 0: 1300Mhz *
GPU[2]		: 1: 1550Mhz
GPU[2]		: 2: 1800Mhz
GPU[2]		: 
GPU[2]		: Supported mclk frequencies on GPU2
GPU[2]		: 0: 900Mhz *
GPU[2]		: 1: 1100Mhz
GPU[2]		: 2: 1300Mhz
GPU[2]		: 
GPU[2]		: Supported sclk frequencies on GPU2
GPU[2]		: 0: 500Mhz
GPU[2]		: 1: 142Mhz *
GPU[2]		: 2: 2100Mhz
GPU[2]		: 
GPU[2]		: Supported socclk frequencies on GPU2
GPU[2]		: S: 30Mhz *
GPU[2]		: 0: 889Mhz
GPU[2]		: 1: 1000Mhz
GPU[2]		: 2: 1143Mhz
GPU[2]		: 
GPU[2]		: 
------------------------------------------------------------------------------------------
GPU[3]		: 
GPU[3]		: Supported fclk frequencies on GPU3
GPU[3]		: 0: 1300Mhz *
GPU[3]		: 1: 1550Mhz
GPU[3]		: 2: 1800Mhz
GPU[3]		: 
GPU[3]		: Supported mclk frequencies on GPU3
GPU[3]		: 0: 900Mhz *
GPU[3]		: 1: 1100Mhz
GPU[3]		: 2: 1300Mhz
GPU[3]		: 
GPU[3]		: Supported sclk frequencies on GPU3
GPU[3]		: S: 132Mhz *
GPU[3]		: 0: 500Mhz
GPU[3]		: 1: 2100Mhz
GPU[3]		: 
GPU[3]		: Supported socclk frequencies on GPU3
GPU[3]		: S: 30Mhz *
GPU[3]		: 0: 889Mhz
GPU[3]		: 1: 1000Mhz
GPU[3]		: 2: 1143Mhz
GPU[3]		: 
GPU[3]		: 
------------------------------------------------------------------------------------------
==========================================================================================
=================================== % time GPU is busy ===================================
GPU[0]		: GPU use (%): 0
GPU[0]		: GFX Activity: 50288
GPU[1]		: GPU use (%): 0
GPU[1]		: GFX Activity: 50288
GPU[2]		: GPU use (%): 0
GPU[2]		: GFX Activity: 50288
GPU[3]		: GPU use (%): 0
GPU[3]		: GFX Activity: 50288
==========================================================================================
=================================== Current Memory Use ===================================
GPU[0]		: GPU memory use (%): 0
GPU[0]		: Memory Activity: 0
GPU[0]		: Avg. Memory Bandwidth: 0
GPU[1]		: GPU memory use (%): 0
GPU[1]		: Memory Activity: 0
GPU[1]		: Avg. Memory Bandwidth: 0
GPU[2]		: GPU memory use (%): 0
GPU[2]		: Memory Activity: 0
GPU[2]		: Avg. Memory Bandwidth: 0
GPU[3]		: GPU memory use (%): 0
GPU[3]		: Memory Activity: 0
GPU[3]		: Avg. Memory Bandwidth: 0
==========================================================================================
===================================== Memory Vendor ======================================
GPU[0]		: GPU memory vendor: samsung
GPU[1]		: GPU memory vendor: samsung
GPU[2]		: GPU memory vendor: samsung
GPU[3]		: GPU memory vendor: samsung
==========================================================================================
================================== PCIe Replay Counter ===================================
GPU[0]		: PCIe Replay Count: 0
GPU[1]		: PCIe Replay Count: 0
GPU[2]		: PCIe Replay Count: 0
GPU[3]		: PCIe Replay Count: 0
==========================================================================================
===================================== Serial Number ======================================
GPU[0]		: Serial Number: 692347006052
GPU[1]		: Serial Number: 692347005894
GPU[2]		: Serial Number: 692347006047
GPU[3]		: Serial Number: 692347005902
==========================================================================================
===================================== KFD Processes ======================================
get_compute_process_info_by_pid, Not supported on the given system
KFD process information:
PID    	PROCESS NAME	GPU(s)	VRAM USED	SDMA USED	CU OCCUPANCY	
1188185	UNKNOWN     	0     	UNKNOWN  	UNKNOWN  	UNKNOWN     	
==========================================================================================
================================== GPUs Indexed by PID ===================================
PID 1188185 is using 0 DRM device(s)
==========================================================================================
======================= GPU Memory clock frequencies and voltages ========================
GPU[0]		: OD_SCLK:
GPU[0]		: 0: 500Mhz
GPU[0]		: 1: 2100Mhz
GPU[0]		: OD_MCLK:
GPU[0]		: 1: 1300Mhz
GPU[0]		: OD_VDDC_CURVE:
GPU[0]		: 0: 0Mhz 0mV
GPU[0]		: 1: 0Mhz 0mV
GPU[0]		: 2: 0Mhz 0mV
GPU[0]		: OD_RANGE:
GPU[0]		: SCLK:     0Mhz        0Mhz
GPU[0]		: MCLK:     0Mhz        0Mhz
GPU[0]		: VDDC_CURVE_SCLK[0]:     0Mhz
GPU[0]		: VDDC_CURVE_VOLT[0]:     0mV
GPU[0]		: VDDC_CURVE_SCLK[1]:     0Mhz
GPU[0]		: VDDC_CURVE_VOLT[1]:     0mV
GPU[0]		: VDDC_CURVE_SCLK[2]:     0Mhz
GPU[0]		: VDDC_CURVE_VOLT[2]:     0mV
GPU[1]		: OD_SCLK:
GPU[1]		: 0: 133Mhz
GPU[1]		: 1: 2100Mhz
GPU[1]		: OD_MCLK:
GPU[1]		: 1: 1300Mhz
GPU[1]		: OD_VDDC_CURVE:
GPU[1]		: 0: 0Mhz 0mV
GPU[1]		: 1: 0Mhz 0mV
GPU[1]		: 2: 0Mhz 0mV
GPU[1]		: OD_RANGE:
GPU[1]		: SCLK:     0Mhz        0Mhz
GPU[1]		: MCLK:     0Mhz        0Mhz
GPU[1]		: VDDC_CURVE_SCLK[0]:     0Mhz
GPU[1]		: VDDC_CURVE_VOLT[0]:     0mV
GPU[1]		: VDDC_CURVE_SCLK[1]:     0Mhz
GPU[1]		: VDDC_CURVE_VOLT[1]:     0mV
GPU[1]		: VDDC_CURVE_SCLK[2]:     0Mhz
GPU[1]		: VDDC_CURVE_VOLT[2]:     0mV
GPU[2]		: OD_SCLK:
GPU[2]		: 0: 500Mhz
GPU[2]		: 1: 2100Mhz
GPU[2]		: OD_MCLK:
GPU[2]		: 1: 1300Mhz
GPU[2]		: OD_VDDC_CURVE:
GPU[2]		: 0: 0Mhz 0mV
GPU[2]		: 1: 0Mhz 0mV
GPU[2]		: 2: 0Mhz 0mV
GPU[2]		: OD_RANGE:
GPU[2]		: SCLK:     0Mhz        0Mhz
GPU[2]		: MCLK:     0Mhz        0Mhz
GPU[2]		: VDDC_CURVE_SCLK[0]:     0Mhz
GPU[2]		: VDDC_CURVE_VOLT[0]:     0mV
GPU[2]		: VDDC_CURVE_SCLK[1]:     0Mhz
GPU[2]		: VDDC_CURVE_VOLT[1]:     0mV
GPU[2]		: VDDC_CURVE_SCLK[2]:     0Mhz
GPU[2]		: VDDC_CURVE_VOLT[2]:     0mV
GPU[3]		: OD_SCLK:
GPU[3]		: 0: 132Mhz
GPU[3]		: 1: 2100Mhz
GPU[3]		: OD_MCLK:
GPU[3]		: 1: 1300Mhz
GPU[3]		: OD_VDDC_CURVE:
GPU[3]		: 0: 0Mhz 0mV
GPU[3]		: 1: 0Mhz 0mV
GPU[3]		: 2: 0Mhz 0mV
GPU[3]		: OD_RANGE:
GPU[3]		: SCLK:     0Mhz        0Mhz
GPU[3]		: MCLK:     0Mhz        0Mhz
GPU[3]		: VDDC_CURVE_SCLK[0]:     0Mhz
GPU[3]		: VDDC_CURVE_VOLT[0]:     0mV
GPU[3]		: VDDC_CURVE_SCLK[1]:     0Mhz
GPU[3]		: VDDC_CURVE_VOLT[1]:     0mV
GPU[3]		: VDDC_CURVE_SCLK[2]:     0Mhz
GPU[3]		: VDDC_CURVE_VOLT[2]:     0mV
==========================================================================================
==================================== Current voltage =====================================
GPU[0]		: get_volt_metric, Not supported on the given system
GPU[1]		: get_volt_metric, Not supported on the given system
GPU[2]		: get_volt_metric, Not supported on the given system
GPU[3]		: get_volt_metric, Not supported on the given system
==========================================================================================
======================================= PCI Bus ID =======================================
GPU[0]		: PCI Bus: 0000:26:00.0
GPU[1]		: PCI Bus: 0000:46:00.0
GPU[2]		: PCI Bus: 0000:65:00.0
GPU[3]		: PCI Bus: 0000:85:00.0
==========================================================================================
================================== Firmware Information ==================================
GPU[0]		: get_firmware_version_ASD, Not supported on the given system
GPU[0]		: get_firmware_version_CE, Not supported on the given system
GPU[0]		: get_firmware_version_DMCU, Not supported on the given system
GPU[0]		: get_firmware_version_MC, Not supported on the given system
GPU[0]		: get_firmware_version_ME, Not supported on the given system
GPU[0]		: MEC firmware version: 	138
GPU[0]		: MEC2 firmware version: 	138
GPU[0]		: get_firmware_version_MES, Not supported on the given system
GPU[0]		: get_firmware_version_MES KIQ, Not supported on the given system
GPU[0]		: get_firmware_version_PFP, Not supported on the given system
GPU[0]		: RLC firmware version: 	63
GPU[0]		: get_firmware_version_RLC SRLC, Not supported on the given system
GPU[0]		: get_firmware_version_RLC SRLG, Not supported on the given system
GPU[0]		: get_firmware_version_RLC SRLS, Not supported on the given system
GPU[0]		: SDMA firmware version: 	19
GPU[0]		: SDMA2 firmware version: 	19
GPU[0]		: SMC firmware version: 	00.85.91.00
GPU[0]		: SOS firmware version: 	0x0036024b
GPU[0]		: TA RAS firmware version: 	32.00.00.12
GPU[0]		: TA XGMI firmware version: 	32.00.01.19
GPU[0]		: get_firmware_version_UVD, Not supported on the given system
GPU[0]		: get_firmware_version_VCE, Not supported on the given system
GPU[0]		: VCN firmware version: 	0x0611300c
GPU[1]		: get_firmware_version_ASD, Not supported on the given system
GPU[1]		: get_firmware_version_CE, Not supported on the given system
GPU[1]		: get_firmware_version_DMCU, Not supported on the given system
GPU[1]		: get_firmware_version_MC, Not supported on the given system
GPU[1]		: get_firmware_version_ME, Not supported on the given system
GPU[1]		: MEC firmware version: 	138
GPU[1]		: MEC2 firmware version: 	138
GPU[1]		: get_firmware_version_MES, Not supported on the given system
GPU[1]		: get_firmware_version_MES KIQ, Not supported on the given system
GPU[1]		: get_firmware_version_PFP, Not supported on the given system
GPU[1]		: RLC firmware version: 	63
GPU[1]		: get_firmware_version_RLC SRLC, Not supported on the given system
GPU[1]		: get_firmware_version_RLC SRLG, Not supported on the given system
GPU[1]		: get_firmware_version_RLC SRLS, Not supported on the given system
GPU[1]		: SDMA firmware version: 	19
GPU[1]		: SDMA2 firmware version: 	19
GPU[1]		: SMC firmware version: 	00.85.91.00
GPU[1]		: SOS firmware version: 	0x0036024b
GPU[1]		: TA RAS firmware version: 	32.00.00.12
GPU[1]		: TA XGMI firmware version: 	32.00.01.19
GPU[1]		: get_firmware_version_UVD, Not supported on the given system
GPU[1]		: get_firmware_version_VCE, Not supported on the given system
GPU[1]		: VCN firmware version: 	0x0611300c
GPU[2]		: get_firmware_version_ASD, Not supported on the given system
GPU[2]		: get_firmware_version_CE, Not supported on the given system
GPU[2]		: get_firmware_version_DMCU, Not supported on the given system
GPU[2]		: get_firmware_version_MC, Not supported on the given system
GPU[2]		: get_firmware_version_ME, Not supported on the given system
GPU[2]		: MEC firmware version: 	138
GPU[2]		: MEC2 firmware version: 	138
GPU[2]		: get_firmware_version_MES, Not supported on the given system
GPU[2]		: get_firmware_version_MES KIQ, Not supported on the given system
GPU[2]		: get_firmware_version_PFP, Not supported on the given system
GPU[2]		: RLC firmware version: 	63
GPU[2]		: get_firmware_version_RLC SRLC, Not supported on the given system
GPU[2]		: get_firmware_version_RLC SRLG, Not supported on the given system
GPU[2]		: get_firmware_version_RLC SRLS, Not supported on the given system
GPU[2]		: SDMA firmware version: 	19
GPU[2]		: SDMA2 firmware version: 	19
GPU[2]		: SMC firmware version: 	00.85.91.00
GPU[2]		: SOS firmware version: 	0x0036024b
GPU[2]		: TA RAS firmware version: 	32.00.00.12
GPU[2]		: TA XGMI firmware version: 	32.00.01.19
GPU[2]		: get_firmware_version_UVD, Not supported on the given system
GPU[2]		: get_firmware_version_VCE, Not supported on the given system
GPU[2]		: VCN firmware version: 	0x0611300c
GPU[3]		: get_firmware_version_ASD, Not supported on the given system
GPU[3]		: get_firmware_version_CE, Not supported on the given system
GPU[3]		: get_firmware_version_DMCU, Not supported on the given system
GPU[3]		: get_firmware_version_MC, Not supported on the given system
GPU[3]		: get_firmware_version_ME, Not supported on the given system
GPU[3]		: MEC firmware version: 	138
GPU[3]		: MEC2 firmware version: 	138
GPU[3]		: get_firmware_version_MES, Not supported on the given system
GPU[3]		: get_firmware_version_MES KIQ, Not supported on the given system
GPU[3]		: get_firmware_version_PFP, Not supported on the given system
GPU[3]		: RLC firmware version: 	63
GPU[3]		: get_firmware_version_RLC SRLC, Not supported on the given system
GPU[3]		: get_firmware_version_RLC SRLG, Not supported on the given system
GPU[3]		: get_firmware_version_RLC SRLS, Not supported on the given system
GPU[3]		: SDMA firmware version: 	19
GPU[3]		: SDMA2 firmware version: 	19
GPU[3]		: SMC firmware version: 	00.85.91.00
GPU[3]		: SOS firmware version: 	0x0036024b
GPU[3]		: TA RAS firmware version: 	32.00.00.12
GPU[3]		: TA XGMI firmware version: 	32.00.01.19
GPU[3]		: get_firmware_version_UVD, Not supported on the given system
GPU[3]		: get_firmware_version_VCE, Not supported on the given system
GPU[3]		: VCN firmware version: 	0x0611300c
==========================================================================================
====================================== Product Info ======================================
GPU[0]		: Card series: 		AMD Instinct MI300X OAM
GPU[0]		: Card model: 		0x74a1
GPU[0]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
GPU[0]		: Card SKU: 		MI3SRIOV
GPU[1]		: Card series: 		AMD Instinct MI300X OAM
GPU[1]		: Card model: 		0x74a1
GPU[1]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
GPU[1]		: Card SKU: 		MI3SRIOV
GPU[2]		: Card series: 		AMD Instinct MI300X OAM
GPU[2]		: Card model: 		0x74a1
GPU[2]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
GPU[2]		: Card SKU: 		MI3SRIOV
GPU[3]		: Card series: 		AMD Instinct MI300X OAM
GPU[3]		: Card model: 		0x74a1
GPU[3]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
GPU[3]		: Card SKU: 		MI3SRIOV
==========================================================================================
======================================= Pages Info =======================================
==========================================================================================
================================= Show Valid sclk Range ==================================
GPU[0]		: Valid sclk range: 139Mhz - 2100Mhz
GPU[1]		: Valid sclk range: 133Mhz - 2100Mhz
GPU[2]		: Valid sclk range: 139Mhz - 2100Mhz
GPU[3]		: Valid sclk range: 132Mhz - 2100Mhz
==========================================================================================
================================= Show Valid mclk Range ==================================
GPU[0]		: Valid mclk range: 900Mhz - 1300Mhz
GPU[1]		: Valid mclk range: 900Mhz - 1300Mhz
GPU[2]		: Valid mclk range: 900Mhz - 1300Mhz
GPU[3]		: Valid mclk range: 900Mhz - 1300Mhz
==========================================================================================
================================ Show Valid voltage Range ================================
==========================================================================================
================================== Voltage Curve Points ==================================
GPU[0]		: Voltage point 0: 0Mhz 0mV
GPU[0]		: Voltage point 1: 0Mhz 0mV
GPU[0]		: Voltage point 2: 0Mhz 0mV
GPU[1]		: Voltage point 0: 0Mhz 0mV
GPU[1]		: Voltage point 1: 0Mhz 0mV
GPU[1]		: Voltage point 2: 0Mhz 0mV
GPU[2]		: Voltage point 0: 0Mhz 0mV
GPU[2]		: Voltage point 1: 0Mhz 0mV
GPU[2]		: Voltage point 2: 0Mhz 0mV
GPU[3]		: Voltage point 0: 0Mhz 0mV
GPU[3]		: Voltage point 1: 0Mhz 0mV
GPU[3]		: Voltage point 2: 0Mhz 0mV
==========================================================================================
==================================== Consumed Energy =====================================
GPU[0]		: Energy counter: 5104503354501
GPU[0]		: Accumulated Energy (uJ): 78098902297472.05
GPU[1]		: Energy counter: 5104503354501
GPU[1]		: Accumulated Energy (uJ): 78098902297472.05
GPU[2]		: Energy counter: 5104503354501
GPU[2]		: Accumulated Energy (uJ): 78098902297472.05
GPU[3]		: Energy counter: 5104503354501
GPU[3]		: Accumulated Energy (uJ): 78098902297472.05
==========================================================================================
=============================== Current Compute Partition ================================
GPU[0]		: Compute Partition: SPX
GPU[1]		: Compute Partition: SPX
GPU[2]		: Compute Partition: SPX
GPU[3]		: Compute Partition: SPX
==========================================================================================
================================ Current Memory Partition ================================
GPU[0]		: Memory Partition: NPS1
GPU[1]		: Memory Partition: NPS1
GPU[2]		: Memory Partition: NPS1
GPU[3]		: Memory Partition: NPS1
==========================================================================================
================================== End of ROCm SMI Log ===================================
'''

def main():
    parser = argparse.ArgumentParser(description="nvidia-smi simulator")
    parser.add_argument('-a', action='store_true', help="simulate nvidia-smi -a")
    args = parser.parse_args()

    if args.a:
        print(out_a)
    else:
        print(out)

