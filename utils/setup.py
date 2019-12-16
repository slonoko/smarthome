import setuptools
# To install type: pip install -e .
setuptools.setup(
    name="smarthomeutils", # Replace with your own username
    version="0.0.1",
    author="Elie Khoury",
    author_email="elie.kh@gmail.com",
    description="Utility package for smart home app",
    include_package_data=False,
    zip_safe=False,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'argparse'
    ], 
)