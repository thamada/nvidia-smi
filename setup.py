from setuptools import setup, find_packages

setup(
    name="nvidia-smi-simulator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # 依存パッケージをここに記述
    ],
    entry_points={
        'console_scripts': [
            'nvidia-smi=nvsim.H100SXMx8_smi:main',
            'deviceQuery=nvsim.H100SXMx8_deviceQuery:main',

            'nvidia-smi.h100x8=nvsim.H100SXMx8_smi:main',
            'deviceQuery.h100x8=nvsim.H100SXMx8_deviceQuery:main',

            'nvidia-smi.rtx2000ada=nvsim.RTX2000Ada_smi:main',
            'deviceQuery.rtx2000ada=nvsim.RTX2000Ada_deviceQuery:main',

            'nvidia-smi.rtx4000ada=nvsim.RTX4000Ada_smi:main',
            'deviceQuery.rtx4000ada=nvsim.RTX4000Ada_deviceQuery:main',

            'nvidia-smi.rtx4060ti=nvsim.RTX4060Ti_smi:main',
            'deviceQuery.rtx4060ti=nvsim.RTX4060Ti_deviceQuery:main',

            'nvidia-smi.rtx4090=nvsim.RTX4090_smi:main',  # 8 devices
            'deviceQuery.rtx4090=nvsim.RTX4090_deviceQuery:main', # 8 devices

            'nvidia-smi.l40s=nvsim.L40S_smi:main',
            'deviceQuery.l40s=nvsim.L40S_deviceQuery:main',

            'nvidia-smi.l4=nvsim.L4_smi:main',
            'deviceQuery.l4=nvsim.L4_deviceQuery:main',

            'rocm-smi=nvsim.MI300X_smi:main',
            'deviceQuery.mi300x=nvsim.MI300X_deviceQuery:main',
        ],
    },
)
