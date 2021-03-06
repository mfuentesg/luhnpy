from distutils.core import setup


setup(
    name='luhnpy',
    py_modules=['luhnpy'],
    version='1.0.0',
    description='A minimalistic implementation of Luhn algorithm',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Marcelo Fuentes',
    author_email='marceloe.fuentes@gmail.com',
    url='https://github.com/mfuentesg/luhnpy',
    download_url='https://github.com/mfuentesg/luhnpy/archive/1.0.0.tar.gz',
    keywords=['luhn', 'algorithm'],
    classifiers=[]
)
