from setuptools import setup, find_packages

setup(
    name="supply_chain_platform",
    version="0.1.0",
    description="An end-to-end supply chain analytics and intelligence platform.",
    author="Analytics Team",
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open("requirements.txt").readlines()
    ],
    python_requires=">=3.9",
)
