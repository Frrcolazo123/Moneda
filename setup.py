from setuptools import setup, find_packages

setup(
    name='mi_utilidad',  # Cambia esto por el nombre de tu paquete
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'psycopg2-binary'
    ],
    extras_require={
        'dev': ['pytest', 'pytest-mock']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)