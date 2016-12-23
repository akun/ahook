SRC_DIR = ahook
DOC_DIR = docs
MAKE = make

all:
	make install
	make test
	make html
	make clean

install:
	pip install -q -e .[dev,test,docs]

lint:
	prospector $(SRC_DIR) --strictness veryhigh
	bandit $(SRC_DIR)

test:
	nosetests -c nose.cfg

testall:
	tox

html:
	cd $(DOC_DIR) && $(MAKE) html

htmlci:
	curl -X POST http://readthedocs.org/build/ahook

sdist:
	python setup.py register upload

clean:
	rm -rf *.egg-info $(SRC_DIR)/*.egg-info build dist
	find $(SRC_DIR) -name "*.pyc" | xargs rm -rf
