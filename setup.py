from setuptools import setup

version = __import__('ateoto_cupping').__version__

setup(name = 'django-ateoto-cupping',
    version = version,
    author = 'Matthew McCants',
    author_email = 'mattmccants@gmail.com',
    description = 'Cupping application for django.',
    license = 'BSD',
    url = 'https://github.com/Ateoto/django-ateoto-cupping',
    packages = ['ateoto_cupping'],
    install_requires = ['django>=1.4'])
