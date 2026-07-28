import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pines_rimas_analysis_toolkit',
    version='1.0.0',
    author='Fira Fatmasiefa',
    author_email='ffsiefa@bu.edu',
    description='Analysis pipeline for LDT-RIMAS.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/firafsiefa/pines_rimas_analysis_toolkit',
    license='BU',
    packages=['pines_rimas_analysis_toolkit'],
    install_requires=['julian'],
)
