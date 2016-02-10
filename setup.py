from distutils.core      import setup
from distutils.extension import Extension
from Cython.Build        import cythonize

extensions = [
    Extension('bokuro.processor', ['bokuro/processor.pyx'])
]

setup(
    name='bokuro',
    version='0.1.0',
    ext_modules=cythonize(extensions)
)
