import click


@click.group()
@click.option(
    "-r",
    "--rank",
    help="run full ML pipeline",
    default=[],
    multiple=True,
)
def ml(**kwargs) -> None:
    pass


@ml.command(help="Run modeling training pipeline")
@click.option(
    "-s",
    "--steps",
    help="Specify which steps to run in the modeling pipeline",
    default=["extract", "transform", "load"],
    multiple=True,
)
def train(**kwargs):
    import reproml.ml

    reproml.ml.train(**kwargs)
