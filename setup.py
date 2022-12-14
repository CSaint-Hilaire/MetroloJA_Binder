from setuptools import find_packages, setup


setup(
    name='metroloja_lib',
    version='0.1.0',
    author='Cadisha Saint-Hilaire',
    author_email='sainthilaire.cadisha@gmail.com',
    packages=find_packages(include=['metroloja_lib']),
    scripts=['metroloja_lib/psf_analyze.py',
             'metroloja_lib/coreg_analyze.py'],
    description='metroloja_lib is a python library allowing a simplified display'
    'of MetroloJ_QC analyze result.',
    url='https://github.com/CSaint-Hilaire/MetroloJA',
    install_requires=[
        "pandas",
        "scipy",
        "PyPDF2==2.4.2",
        "alive_progress==2.4.1", 
        "plotly==5.1.0", 
        "setuptools==58.0.4",
        "PyQt5==5.15.6",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
