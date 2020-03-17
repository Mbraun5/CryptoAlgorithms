#!/bin/bash
find . -name "*.py[co]" -o -name __pycache__ -exec rm -rf {} +

