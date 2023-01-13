import click


@click.group()
@click.option(
    "-r",
    "--rank",
    help="run full ML pipeline",
    default=[],
    multiple=True,
)
def validate(**kwargs) -> None:
    pass


@validate.command(help="Run modeling validation pipeline")
@click.option(
    "-s",
    "--steps",
    help="Specify which steps to run in the modeling validation pipeline",
    default=["extract", "transform", "load"],
    multiple=True,
)
def metrics(**kwargs):
    import reproml.validation.validate

    reproml.validation.validate(**kwargs)
