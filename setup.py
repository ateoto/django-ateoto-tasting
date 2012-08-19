from setuptools import setup

version = __import__('ateoto_tasting').__version__

setup(name = 'django-ateoto-tasting',
    version = version,
    author = 'Matthew McCants',
    author_email = 'mattmccants@gmail.com',
    description = 'Cupping application for django.',
    license = 'BSD',
    url = 'https://github.com/Ateoto/django-ateoto-tasting',
    packages = ['ateoto_tasting'],
    install_requires = ['django>=1.4'])
