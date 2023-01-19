# Setup
### Prerequisites
- Python [3.6.0 or higher](https://www.python.org/downloads/)
- [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- cloned [the repo]

### Setting up the project
- create new virtual env `mkvirtualenv -p <path/to/python3> WoT_test`,
you could use any other name instead of `WoT_test`

- activate the env by running `workon WoT_test`
- run `python setup.py install`


# Run tests
- run smoke tests `invoke test.smoke`
gfdfg