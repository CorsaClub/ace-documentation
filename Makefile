PYTHON     := /opt/homebrew/bin/python3.12
VENV       := .venv
PIP        := $(VENV)/bin/pip
MARKER     := $(VENV)/bin/marker_single
OUTPUT_DIR := docs/markdown

.PHONY: all convert setup clean distclean list

all: list

## List available file IDs
list:
	@./convert.sh 2>/dev/null || true

## Install dependencies into the local virtualenv
setup: $(MARKER)

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --quiet --upgrade pip

$(MARKER): $(VENV)/bin/activate
	$(PIP) install --quiet marker-pdf

## Convert a PDF by ID: make convert ID=1
convert: $(MARKER)
ifndef ID
	$(error ID is required. Usage: make convert ID=1)
endif
	./convert.sh $(ID)

## Remove generated output
clean:
	rm -rf "$(OUTPUT_DIR)"

## Remove virtualenv and output
distclean: clean
	rm -rf "$(VENV)"
