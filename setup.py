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
            'nvidia-smi=package.main:main',  # nvidia-smiが実行可能なコマンド
        ],
    },
)
