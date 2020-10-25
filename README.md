# github-actions-unittest (In Development)

This repository shows how you can use github actions to automatically run unit tests on your python
code every time code is pushed to your repository.

# Guide

The `addition.py` script has an `add_one` function which takes a number and
adds one to it.  The `test_addition.py` script has a unit test that checks
if the `add_one` function is working properly.

To run the unit tests, open your terminal and run

```bash
python -m unittest discover
```