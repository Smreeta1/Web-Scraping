from setuptools import setup

setup(
    name="webscraping_project",
    version="1.0",
    
    install_requires=[
        "MechanicalSoup",
        "beautifulsoup4"
    ],      
    author="Smreeta",
    description="A web scraping project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
