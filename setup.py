"""
Setup configuration for Genesis10000+ Framework
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="genesis10000",
    version="1.0.0",
    author="Genesis Research Team",
    author_email="genesis@example.com",
    description="A paradigm-shifting AI framework merging ethical kernels, conscious design protocols, and adaptive self-reflection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alvoradozerouno/Genesis-Level-Paradigm-Shift",
    packages=find_packages(exclude=["tests", "tests.*", "examples"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies required for core functionality
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "mypy>=0.950",
        ],
    },
    keywords="ai ethics responsible-ai alignment eira orion ethical-ai",
    project_urls={
        "Bug Reports": "https://github.com/Alvoradozerouno/Genesis-Level-Paradigm-Shift/issues",
        "Source": "https://github.com/Alvoradozerouno/Genesis-Level-Paradigm-Shift",
        "Documentation": "https://github.com/Alvoradozerouno/Genesis-Level-Paradigm-Shift/tree/main/docs",
    },
)
