from setuptools import find_packages, setup

setup(
    name="rocksteady",
    description="Pytestarooooo",
    python_requires=">=3.7.0",
    packages=find_packages(exclude=("tests*",)),
    setup_requires=[],
    tests_require=["pytest", "requests_mock"],
    install_requires=["requests"],
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
