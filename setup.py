from setuptools import setup, find_packages

setup(
    name="airflow-census-jeetendra",
    license="MIT",
    version="0.0.1",
    description="This is the project to ingest data from densu API",
    author="Jeetendra Shakya",
    packages=find_packages(),
    install_requires=['tfx==1.6.1', 'apache-beam[interactive]', 'apache-airflow']
)
