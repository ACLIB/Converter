from distutils.core import setup, Extension


class Library:
    def __init__(self, name: str, sources: list, include_dirs: list):
        self._name = name
        self._sources = sources
        self._include_dirs = include_dirs

    def __call__(self, *args, **kwargs):
        return [self._name, {'sources': self._sources, 'include_dirs': self._include_dirs}]


common_lib = Library(
    name='ACLIBCommon',
    sources=[
        '../Common/source/util/Mutex.cpp',
        '../Common/source/util/LockGuard.cpp',
        '../Common/source/util/Thread.cpp'],
    include_dirs=['../Common/include'])


extension = Extension(
    name='aclib_converter',
    sources=[
        'source/python/ACLIBConverter.cpp',
        'source/Converter.cpp'
    ],
    include_dirs=['source', '../Common/include'],
    library_dirs=[],
    libraries=['ACLIBCommon'],
    extra_compile_args=['/Ot'])


setup(name='aclib_converter',
      version='1.0',
      ext_modules=[extension],
      libraries=[common_lib()])
