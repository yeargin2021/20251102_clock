#!/usr/bin/env python3
"""
Setup script for Digital Clock App
"""

from setuptools import setup, find_packages
import os

# Read the README file for the long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "A simple digital clock application built with Python and tkinter."

setup(
    name="digital-clock-app",
    version="1.0.0",
    author="Tommy",
    description="A simple, elegant digital clock application with GUI",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    py_modules=["digital_clock_app"],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Desktop Environment",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "digital-clock=digital_clock_app:main",
        ],
    },
    keywords="clock digital time gui tkinter desktop utility",
    project_urls={
        "Source": "https://github.com/your-username/digital-clock-app",
        "Bug Reports": "https://github.com/your-username/digital-clock-app/issues",
    },
)