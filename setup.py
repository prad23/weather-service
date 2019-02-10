import sys
sys.path.append("./modules")
from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

def get_version():
    with open('VERSION') as f:
        return f.read()

setup(
    name="weather-service",
    version=get_version(),
    description="Get weather for a service .",
    url="https://github.com/prad23/weather-service",
    author="Prad23",
    author_email="pradyu23@gmail.com",
    packages=find_packages(".",exclude=['concurrent','test']),
    #packages=["app"],
    install_requires=["requests","flask"],
    python_requires='>=3.5',
    py_modules=["os","config_loader","errors","logging"],
    keywords='distance',
    include_package_data=True
 #   zip_safe=False
)
