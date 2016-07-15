from setuptools import setup

setup(
    name='consulkv',
    version='0.1.0',
    description='Multi-environment Consul KV tool',
    long_description=open('README.md').read(),
    author='Brian Clark',
    author_email='brian@clark.zone',
    scripts=['consulkv'],
    install_requires=['pyaml', 'tabulate', 'consulate'],
)
