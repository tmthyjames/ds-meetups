import click


@click.group(invoke_without_command=True)
def etl(**kwargs):
    pass


@etl.command(help="Run all jobs")
def run_all(**kwargs) -> None:
    pass


@etl.command(help="run the lyrics data jobs.")
@click.option(
    "-s",
    "--steps",
    help="Specify which steps to run in the lyrics pipeline",
    default=["extract", "transform", "load"],
    multiple=True,
)
def get_lyrics(steps, **kwargs) -> None:
    from reproml.etl.lyrics import get_lyrics

    path = get_lyrics()
    return path
