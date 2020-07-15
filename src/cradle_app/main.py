# standard libraries
from pathlib import Path

# internal libraries
from config.model import Config

# external libraries
import typer
import gradio as gr


app = typer.Typer()


def greet(name):
    return "Hello " + name + "!"


@app.callback()
def callback():
    """
    cradle is tool to test ML models in production.
    """


@app.command()
def init():
    """
    init cradle app
    """
    typer.echo("Bootstrapping cradle app")


@app.command()
def register(file: Path = typer.Option(None)):
    """
    Register model config for evaluation
    """
    if file is None:
        typer.echo("No config file")
        raise typer.Abort()
    if file.is_file():
        typer.echo("Registering model config...\n")
        model = Config(file)
        typer.echo("Show Model Config\n")
        model.show()
    elif file.is_dir():
        typer.echo("This is a directory, please give a file as input.")
    elif not file.exists():
        typer.echo("The Model Config file doesn't exist.")


@app.command()
def launch():
    """
    Launch gradio instance
    """
    typer.echo("Launching gradio instance")
    _, gradio_interface_url, _ = gr.Interface(
        fn=greet, inputs="text", outputs="text"
    ).launch()
    typer.launch(gradio_interface_url)


if __name__ == "__main__":
    app()
