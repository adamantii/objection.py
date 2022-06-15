from setuptools import setup, find_packages
import pathlib
from objectionpy import _version

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="objectionpy",
    version=_version.__version__,
    author="Adamanti",
    author_email="adam@sallome.com",
    url="https://github.com/adamantii/objection.py",
    description="A modular python library for creating objection.lol projects",
    long_description=(here / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=["objectionpy"],
    keywords=["objection.lol", "objection", "generator", "case", "scene"],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Topic :: Artistic Software",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        "Documentation": "https://adamantii.github.io/objection.py/",
        "Bug Reports": "https://github.com/adamantii/objection.py/issues",
        "Source": "https://github.com/adamantii/objection.py/",
    },
)
