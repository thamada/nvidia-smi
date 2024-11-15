from setuptools import setup, find_packages

setup(
    name="nvidia-smi-simulator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # 必要なライブラリとそのバージョンを指定
        "mdv>=1.7.4",
        "requests>=2.32.3",
    ],
    entry_points={
        'console_scripts': [
            'nvidia-smi=nvsim.H100SXMx8_smi:main',
            'deviceQuery=nvsim.H100SXMx8_deviceQuery:main',

            'nvidia-smi.h100=nvsim.H100SXMx8_smi:main',
            'deviceQuery.h100=nvsim.H100SXMx8_deviceQuery:main',

            'nvidia-smi.h100nvl=nvsim.H100NVLx2_smi:main', # 2 devices
            'deviceQuery.h100nvl=nvsim.H100NVLx2_deviceQuery:main', # 2 devices

            'nvidia-smi.rtx2000ada=nvsim.RTX2000Ada_smi:main',
            'deviceQuery.rtx2000ada=nvsim.RTX2000Ada_deviceQuery:main',

            'nvidia-smi.rtx4000ada=nvsim.RTX4000Ada_smi:main',
            'deviceQuery.rtx4000ada=nvsim.RTX4000Ada_deviceQuery:main',

            'nvidia-smi.rtx6000ada=nvsim.RTX6000Ada_x8_smi:main', # 8 devices
            'deviceQuery.rtx6000ada=nvsim.RTX6000Ada_x8_deviceQuery:main', # 8 devices

            'nvidia-smi.rtx4060ti=nvsim.RTX4060Ti_smi:main',
            'deviceQuery.rtx4060ti=nvsim.RTX4060Ti_deviceQuery:main',

            'nvidia-smi.rtx4090=nvsim.RTX4090_smi:main', # 8 devices
            'deviceQuery.rtx4090=nvsim.RTX4090_deviceQuery:main', # 8 devices

            'nvidia-smi.l40s=nvsim.L40S_smi:main',
            'deviceQuery.l40s=nvsim.L40S_deviceQuery:main',

            'nvidia-smi.l4=nvsim.L4_smi:main',
            'deviceQuery.l4=nvsim.L4_deviceQuery:main',

            'nvidia-smi.a100=nvsim.A100SXMx4_smi:main',  # 4 devices
            'deviceQuery.a100=nvsim.A100SXMx4_deviceQuery:main', # 4 devices

            'nvidia-smi.rtx3090=nvsim.RTX3090_smi:main',  # 2 devices
            'deviceQuery.rtx3090=nvsim.RTX3090_deviceQuery:main', # 2 devices

            'nvidia-smi.a40=nvsim.A40x10_smi:main',  # 10 devices
            'deviceQuery.a40=nvsim.A40x10_deviceQuery:main', # 10 devices

            'rocm-smi=nvsim.MI300X_x4_smi:main', # 4 devices
            'rocminfo=nvsim.MI300X_x4_rocminfo:main', # 4 devices
            'deviceQuery.mi300x=nvsim.MI300X_x4_deviceQuery:main', # 4 devices

            'nvsim=nvsim.help:main', # help
        ],
    },
)
