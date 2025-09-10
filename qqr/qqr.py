import typer
from typing_extensions import Annotated
from core.utils.options import ErrorTolerance, Format
from core.core import generate_qr

app = typer.Typer(
    help="""# QR CLI Application

A simple tool to generate **QR codes** with different encoding modes.

Supported modes:
1. Byte — for general binary data
2. Alphanumeric — for numbers, uppercase letters, and a few symbols
3. Numeric — efficient encoding for digits
4. Kanji — optimized for Japanese characters
""",
    rich_markup_mode="markdown",
    pretty_exceptions_show_locals=False,
    epilog="Made with :heart:  by [0spol](https://github.com/0spol)"
)

@app.command(help="Generate QR codes with customizable options")
def qqr(
    data: Annotated[
        str,
        typer.Argument(
            help="""
The input data to encode in the QR code.

Supported formats:

* **URL / Website** — e.g., `https://example.com`
* **Contact / vCard** — e.g., 
  `BEGIN:VCARD\\nVERSION:3.0\\nFN:John Doe\\nTEL:+1234567890\\nEMAIL:john@example.com\\nEND:VCARD`
* **Wi-Fi network** — e.g., `WIFI:T:WPA;S:MyNetwork;P:mypassword;;`
* **Payment / App link** — e.g., `https://paypal.me/username/10`
* **Event / Calendar** — e.g., 
  `BEGIN:VEVENT\\nSUMMARY:Meeting\\nDTSTART:20250905T120000Z\\nDTEND:20250905T130000Z\\nLOCATION:Office\\nEND:VEVENT`
* **Custom text / file** — plain text or Base64-encoded file
"""
        )
    ],
    output: Annotated[
        str,
        typer.Option(
            "--output", "-o",
            envvar="QR_OUTPUT",
            help="Output file name (from env: QR_OUTPUT)"
        )
    ] = "qr.png",
    error: Annotated[
        ErrorTolerance,
        typer.Option("--error", "-e", rich_help_panel="Encoding", help="Error correction level")
    ] = ErrorTolerance.L,
    version: Annotated[
        int,
        typer.Option("--version", "-v", show_default=False, help="QR code version (1–40)")
    ] = None,
    scale: Annotated[
        int,
        typer.Option("--scale", rich_help_panel="Styling", help="Pixel size of each QR module")
    ] = 10,
    border: Annotated[
        int,
        typer.Option("--border", rich_help_panel="Styling", help="Border width in modules")
    ] = 4,
    dark: Annotated[
        str,
        typer.Option("--dark", envvar="QR_DARK_COLOR", rich_help_panel="Styling", help="Dark module color")
    ] = "black",
    light: Annotated[
        str,
        typer.Option("--light", envvar="QR_LIGHT_COLOR", rich_help_panel="Styling", help="Background color")
    ] = "white",
    kind: Annotated[
        Format,
        typer.Option("--kind", rich_help_panel="Output", help="Output file format (png, svg, pdf, eps)")
    ] = Format.PNG
):
    """
    Generate a QR code with full customization.

    Examples:
    - Generate a simple QR:
      `python cli.py qqr "Hello World"`

    - Generate a QR in Kanji mode with high error correction:
      `python cli.py qqr "日本語" --mode kanji --error h`

    - Export as SVG with custom colors:
      `python cli.py qqr "Portfolio" --dark "#1e3a8a" --light "#facc15" --kind svg`
    """
    generate_qr(
        data=data,
        output=output,
        error=error,
        version=version,
        scale=scale,
        border=border,
        dark=dark,
        light=light,
        kind=kind,
    )
    
    typer.echo(f"[green]QR code generated successfully:[/green] {output}")

if __name__ == "__main__":
    app()