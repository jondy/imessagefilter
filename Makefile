PYTHON := C:/Python34/python
GCC := i686-pc-mingw32-gcc

.PHONY: setup build clean

setup: build
	$(PYTHON) setup.py sdist --formats=zip
	$(PYTHON) setup.py bdist_wheel --universal

build: msgfilter.c
	${GCC} -shared -o msgfilter.dll $< -lole32 -luuid
	@echo 'Build msgfilter.dll OK'

clean:
	rm -rf *.pyc *.pyo __pycache__ build imessagefilter.egg-info
