from setuptools import setup, find_packages

setup(
    name="objectionpy",
    version="0.0.1",
    author="Adamanti",
    author_email="adam@sallome.com",
    url="https://github.com/adamantii/objection.py",
    description="A modular python library for creating objection.lol projects",
    packages=find_packages("objectionpy"),
    keywords=['objection.lol', 'objection', 'generator', 'case', 'scene'],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Topic :: Artistic Software",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        "Bug Reports": "https://github.com/adamantii/objection.py/issues",
        "Source": "https://github.com/adamantii/objection.py/",
    },
)
