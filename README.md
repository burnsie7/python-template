# python-teplate

A repo with a template for creating python applications

## Get started

You must run python version 3.9 for this application.

### Initialization

In order to get started you have to:

1. Create your `.env` file: `cp .env.example .env`
2. Set the value in your `.env` file:

    |  Param         | Description                                                                   |
    | -------------- | ----------------------------------------------------------------------------- |
    | `MY_FOO`       | Description                                                                   |
    | `MY_BAR`       | Description                                                                   |

### Work with the app

1. [Install venv if it's not done already](https://docs.python.org/3/tutorial/venv.html)
2. Create the venv environement: `make venv-init`
3. Launch the application `make app`

### Developement

To start developping the application:

1. Create the venv environement: `make venv-init`
2. Activate the venv environment: `. penv/bin/activate`

**Note**:

If you get:

```shell
ModuleNotFoundError: No module named 'src'
```

run: `export PYTHONPATH=./src/:$PYTHONPATH` in your venv

If you get the following when running `make venv-init`

```
[ERROR] Cowardly refusing to install hooks with `core.hooksPath` set.
hint: `git config --unset-all core.hooksPath`
```

1. Comment out `hooksPath` in ~/.gitconfig
2. Run `make venv-init`
3. Uncomment `hooksPath` in ~/.gitconfig

### Testing

The testing library used is: `py.test`

- To install: `pip install pytest`
- To launch the test: `py.test`

### Notes

Unit test: You provide the input and assert the output.
Integration testing: Test the components of the application are being called.

## TO DO

Objective:

- [ ] Clone this project
- [ ] Make something fun
