#!/usr/bin/env python3

from distutils.core import setup, Extension

pysequoia_sources = ['module_py.c', 'session_py.c', 'sequence_py.c',
                        'trigger_py.c', 'outport_py.c', 'inport_py.c']

sequoia_extension = Extension("sequoia",
                                sources=pysequoia_sources,
                                libraries=['sequoia', 'jack', 'json-c'])

setup(name="sequoia", ext_modules=[sequoia_extension])
