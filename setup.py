from setuptools import setup

setup(
    name='twisted-dev-tools',
    version='0.0',
    url='https://github.com/tomprince/twisted-dev-tools',
    description="Tools for twisted development",
    license='MIT',
    author='Tom Prince',
    author_email='tom.prince@ualberta.net',
    packages=['twisted_tools', 'twisted_tools.scripts', 'twisted_tools.test'],
    scripts=[
        'bin/force-build',
        'bin/mkbranch',
        'bin/fetch-ticket',
        'bin/review-tickets',
        'bin/get-attachment',
    ],
    install_requires=[
        'twisted >= 13.0.0',
        'treq',
        'amptrac >= 0.1',
    ],
    zip_safe=False,
)
