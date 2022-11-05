# set shell := [ "bash", "-uc" ]
_default:
    @- just --unsorted --list
menu:
    @- just --unsorted --choose

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# VARIABLES
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PYTHON := if os_family() == "windows" { "py -3" } else { "python3" }
PROJECT_NAME := "quantumcomputing"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Macros
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

_clean-all-files path pattern:
    @find {{path}} -type f -name "{{pattern}}" -exec basename {} \; 2> /dev/null
    @- find {{path}} -type f -name "{{pattern}}" -exec rm {} \; 2> /dev/null

_clean-all-folders path pattern:
    @find {{path}} -type d -name "{{pattern}}" -exec basename {} \; 2> /dev/null
    @- find {{path}} -type d -name "{{pattern}}" -exec rm -rf {} \; 2> /dev/null

_create-folder-if-not-exists path:
    @if ! [ -d "{{path}}" ]; then mkdir -p "{{path}}"; fi

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TARGETS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

build:
    @{{PYTHON}} -m pip install --disable-pip-version-check -r requirements.txt
run:
    @{{PYTHON}} main.py
dist:
    @just _create-folder-if-not-exists "dist"
    @zip \
        -r dist/{{PROJECT_NAME}}-$(cat dist/VERSION).zip ./* \
        -x dist/*.zip \
        -x **/.DS_Store \
        -x __archive__\* \
        -x **/__pycache__\*
clean:
    @echo "All system artefacts will be force removed."
    @- just _clean-all-files "." ".DS_Store" 2> /dev/null
    @echo "All build artefacts will be force removed."
    @- just _clean-all-folders "." "__pycache__" 2> /dev/null
