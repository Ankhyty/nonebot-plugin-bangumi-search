
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="nonebot-plugin-bangumi-search",
    version="1.0.1",
    description="a nonebot2 plugin to help you search anime on bgm.tv and return some information to you",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["nonebot-plugin-bangumi-search"],
    author="Ankhyty",
    author_email="ankhyty@gmail.com",
    url="https://github.com/Ankhyty/nonebot-plugin-bangumi-search",
    install_requires = ["nonebot2>=2.0.0b2","nonebot-adapter-onebot>=2.0.0b1"],
    python_requires=">=3.8.10"
)