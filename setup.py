import setuptools 

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name="gita",
  version="1.0.0",
  author="Shubhendra Kushwaha",
  author_email="shubhendrakushwaha94@gmail.com",
  description="A API wrapper of bhagavadgita.io",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/TheShubhendra/gita",
  packages = setuptools.find_packages(),
  classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
