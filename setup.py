from setuptools import setup, find_packages

setup(
    name="TERMINALGOOGLECAL",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "gcsa",
        "colorama",
        "python-dotenv",
        "openai",
    ],
    description="A terminal-based Google Calendar application using OpenAI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
