from setuptools import setup

setup(
    name="webscraping_project",
    version="1.0",
    
    install_requires=[
        "MechanicalSoup",
        "beautifulsoup4"
    ],      
    author="Smreeta",
    packages=['Files', 'scraper'],
    
    description="A web scraping project",
   
    python_requires='>=3.6',
)
