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
def launch():
    """
    Launch gradio instance
    """
    typer.echo("Launching gradio instance")
    _, gradio_interface_url, _ = gr.Interface(
        fn=greet, inputs="text", outputs="text"
    ).launch()
    typer.launch(gradio_interface_url)
