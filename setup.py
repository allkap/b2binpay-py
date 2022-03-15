import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="b2binpay-py",
    version="0.0.1",
    author="allkap",
    author_email="author@example.com",
    description="Library for working with b2binpay api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allkap/b2binpay-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)