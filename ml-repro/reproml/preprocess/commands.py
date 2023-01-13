import click


@click.group(invoke_without_command=True)
def prepro(**kwargs):
    pass


@prepro.command(help="Run all preprocessing jobs")
def run_all(**kwargs) -> None:
    pass


@prepro.command(help="run the lyrics data jobs.")
@click.option(
    "-s",
    "--steps",
    help="Specify which steps to run in the lyrics preprocessing pipeline",
    default=["clean", "split"],
    multiple=True,
)
def process(steps, **kwargs) -> None:
    from reproml.preprocess import process_lyrics

    process_lyrics()


@prepro.command(help="run the lyrics data jobs.")
@click.option(
    "-s",
    "--steps",
    help="Specify which steps to run in the lyrics preprocessing pipeline",
    default=["clean", "split"],
    multiple=True,
)
def split(steps, **kwargs) -> None:
    from reproml.preprocess import split_lyrics

    split_lyrics()
