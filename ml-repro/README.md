# reproml

This repo contains the `reproml` project.

## Just let me run it!

To pull down and reproduce everything and get access to the CLI just run:

if you don't already have `pipenv`, you can install it using `pip`
```commandline
pip install pipenv
```

Then do

```commandline
git clone https://github.com/tmthyjames/ds-meetup-ml-repro.git

cd ds-meetup-ml-repro

pipenv install --dev
```

That's it! You're ready to start reproducing the data and ML pipelines.

## Now you have access to the `reproml` CLI:

To activate the virtual env shell
```commandline
pipenv shell
```

Now you can run the `reproml` commands:

```commandline
❯ reproml --help                                                                                                                                 ─╯
Usage: reproml [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  etl
  ml
  prepro
  validate
```

Which comes with sub commands for each phase (ETL, Preprocessing, ML, Validating).
To view the help page for each subcommand run `reproml <subcommand> --help` like so:

```commandline
❯ reproml etl --help                                                                                                                             ─╯
Usage: reproml etl [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  get-lyrics  run the lyrics data jobs.
  run-all     Run all jobs
```

So to run the ETL just do this:

```commandline
reproml etl get-lyrics
```

And this will populate the `data/raw` folder, then you can run the propro subcommand
to populate the `data/processed` folder:

```commandline
reproml prepro process
```

You can also import these commands into a notebook environment and use as python functions:

```python
import pandas as pd
from reproml.etl.lyrics import get_lyrics
from reproml.preprocess import process_lyrics

raw_path = get_lyrics()
prepro_path = process_lyrics(srcpath=raw_path)
df = pd.read_parquet(prepro_path)

df.head()
```

## DVC (Data Version Control)

To run this with DVC and thus track all the outputs and dependencies:

```commandline
dvc repro
```

Will reproduce all the stages (etl, ml, preprocessing, validation). Here's a DAG to see the full pipeline:

```commandline
❯ dvc dag
               +------------+
               | get-lyrics |
               +------------+
                      *
                      *
                      *
              +---------------+
              | prepro-lyrics |
              +---------------+
                      *
                      *
                      *
              +--------------+
              | split-lyrics |
              +--------------+
              ***            ***
            **                  **
          **                      **
+-------------+                     **
| train-model |                   **
+-------------+                 **
              ***            ***
                 **        **
                   **    **
             +----------------+
             | validate-model |
             +----------------+
```

# To run individual stages with DVC:

The names of the nodes in the DAG are the names of the stages, so to run `get-lyrics`
for example:

```commandline
dvc repro -s get-lyrics
```

## To contribute or set up for development, here are the development pre-requisites

To work with this repo install the following prerequisites:

* python 3.8+
* pre-commit:

```
brew install pre-commit
```

* pipenv

```
conda install pip
pip install pipenv
```

**Setup for Development**

After prerequisites are installed, run the following commands to clone the repo and configure it for development:

```
cd <REPO_ROOT>

# Install pre-commit hooks to local clone
pre-commit install

# Install pipenv environment
pipenv install --dev

# Create IPython Kernel for the virtual environment
pipenv run ipython kernel install --user --name=reproml
```

The `pipenv install` command above creates an isolated virtual environment for this repo with
all dev dependencies installed. There are two main ways of using the virtual environment. To
run a one off command in the environment use `pipenv run`. For example, the following command
will show the location of the python executable for the environment:

```
pipenv run which python
```

Alternatively, for running many commands `pipenv shell` is used to spawn a new shell in the
virtual environment.

```
cd <REPO_ROOT>
pipenv shell
```

## Running Tests

To run the unit tests run the following command (optionally adding `--cov` for a coverage report):

```
pytest
```

## Troubleshooting

If you ever have trouble with the python environment,
many problems can be resolved by "rebooting" it
by running these commands in the repo root:

```
pipenv --rm
pipenv install --dev
```

This will resolve common problems with packages not being found, etc.
