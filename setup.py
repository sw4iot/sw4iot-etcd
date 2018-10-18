import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sw4iot_etcd",
    version="0.0.2",
    author="SOFTWAY4IoT",
    author_email="sw4iot@gmail.com",
    description="Etcd of SOFTWAY4IoT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sw4iot/sw4iot-etcd",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'etcd3'
    ]
)