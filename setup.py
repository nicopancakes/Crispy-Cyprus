from setuptools import setup, find_packages

setup(
    name="crispy-cyprus",
    version="1.0.0",
    author="nicopancakes",
    description="None",
    packages=find_packages(),
    install_requires=[
        # Any dependencies you need
    ],
    entry_points={
        "console_scripts": [
            "discord-injector = discord_injector.launcher:main"
        ]
    },
    python_requires='>=3.10'
)
