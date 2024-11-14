# Makefile for Python Project

# Variables
VENV := .venv
PYTHON := $(VENV)/bin/python3.10
PIP := $(VENV)/bin/pip
TESTS_DIR := tests
ARGS ?=
SRC := .

all: install lint test

$(VENV)/bin/activate: requirements.txt
	python3.10 -m venv $(VENV)
	$(PIP) install -r requirements.txt

install: $(VENV)/bin/activate

$(TESTS_DIR):
	mkdir -p $(TESTS_DIR)
	touch $(TESTS_DIR)/__init__.py  # Makes it a package

test: $(VENV)/bin/activate $(TESTS_DIR)
	$(PYTHON) -m unittest discover -s $(TESTS_DIR) $(ARGS)

lint: $(VENV)/bin/activate
	$(PYTHON) -m flake8 --exclude=.venv $(SRC) $(ARGS)

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

fclean: clean
		rm -rf $(TESTS_DIR)

run: $(VENV)/bin/activate
	$(PYTHON) $(SRC)/load_csv.py $(ARGS)
.PHONY: all install test lint clean run help
