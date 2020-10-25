# github-actions-unittest

This repository shows how you can use github actions to automatically run unit 
tests on your python code every time code is pushed to your repository.

The `addition.py` script has an `add_one` function which takes a number and
adds one to it.  The `test_addition.py` script has a unit test that checks
if the `add_one` function is working properly.

The [python-unitest.yml](.github/workflows/python-unitest.yml) file contains the 
instructions for GitHub Actions that say to run the unit tests each time someone 
pushes code to the repository.


### Manually Run Tests
To run the unit tests locally on your own machine, open your terminal and run
```bash
python -m unittest discover
```
