from qqr.res.markdown import MD
from qqr.core.utils.options import ErrorTolerance, Format
from qqr.core.utils.checkers import text_path_check, error_check, format_check, name_check, color_check
from qqr.core.core import generate_qr
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import ScrollableContainer, Grid, Container
from textual import on
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets.selection_list import Selection
from textual.widgets import (
    Button,
    Footer,
    Header,
    Input,
    Markdown,
    Select,
    Button,
    Footer,
    Header,
    Input,
    Select,
    SelectionList,
)

class Help(Screen):
    BINDINGS = [
        Binding("escape,space,q,question_mark", "app.pop_screen()", "Close")
        ]
    def compose(self) -> ComposeResult:
        self.border_title = "Help"
        self.border_subtitle = "Press space to come back"
        yield Markdown(MD.HELP_S_MD)

class FormHeader(Widget):
    def compose(self) -> ComposeResult:
        yield Header(
            name=self.app.title,
            show_clock=True,
            icon="⚙️"
        )
    
class FormGrid(Widget):

    @on(Button.Pressed, "#qr_button")
    def generate_qr(self) -> None:
        content = self.query_one("#qrcontent", Input).value
        error = self.query_one("#qrerror", Select).value
        name = self.query_one("#qrname", Input).value
        dark = self.query_one("#qrdark", Input).value
        light = self.query_one("#qrlight", Input).value
        formats = [fmt.value for fmt in self.query_one("#qrformat", SelectionList).selected]

        if not text_path_check(content):
            self.action_notify(
                title="Warning",
                message="QR content must be a non-empty string, shorter than 2000 characters, and contain only printable ASCII characters.",
                severity="warning"
            )
            return

        if not name_check(name):
            self.action_notify(
                title="Warning",
                message="Filename must be a non-empty string, shorter than 255 characters, and can only contain letters, numbers, underscores, or hyphens.",
                severity="warning"
            )
            return

        if not error_check(error):
            self.action_notify(
                title="Warning",
                message="Invalid error tolerance. Must be one of: L, M, Q, H.",
                severity="warning"
            )
            return

        if not format_check(formats):
            self.action_notify(
                title="Warning",
                message=f"At least one valid format must be selected. Accepted values are: {', '.join(Format)}.",
                severity="warning"
            )
            return

        if not color_check(dark):
            self.action_notify(
                title="Warning",
                message=f"Color must be a valid HEX code (#RRGGBB) or a recognized name.",
                severity="warning"
            )
            return
        
        if not color_check(light):
            self.action_notify(
                title="Warning",
                message=f"Color must be a valid HEX code (#RRGGBB) or a recognized name.",
                severity="warning"
            )
            return

        try:
            for i in formats:
               generate_qr(
                    data=content,
                    output=name + "." + i,
                    error=error,
                    dark=dark,
                    light=light,
                    kind=i
                )

            self.action_notify(
                title="Success",
                message="All inputs are valid! Generating QR code...",
                severity="information"
            )

        except Exception as e:
            self.action_notify(
                title="Error",
                message=f"Something went wrong! 🫠 Details: {e}",
                severity="error"
            )

    
        
    def compose(self) -> ComposeResult:
        yield Markdown(MD.WELCOME_MD)
        with ScrollableContainer():
            with Container(id="surface") as container:
                with Grid():
                    with Container(id="content") as container:
                        container.border_title = "Content"
                        yield Input(placeholder="Enter the text or .txt file path", id="qrcontent")
                    
                    with Container(id="name") as container:
                        container.border_title = "File Name"
                        yield Input(placeholder="e.g, my-qr", id="qrname")
                        
                    with Container(id="error") as container:
                        container.border_title = "Error tolerance"
                        yield Select(
                            options=[
                                ("Low (L)", ErrorTolerance.L),
                                ("Medium (M)", ErrorTolerance.M),
                                ("High (Q)", ErrorTolerance.Q),
                                ("Super High (H)", ErrorTolerance.H),
                            ],
                            id="qrerror",
                            prompt="Pick your error tolerance!",
                        )
                        
                    with Container(id="dark") as container:
                        container.border_title = "QR color"
                        yield Input(placeholder="e.g, green or hexadecimal format", id="qrdark")
                    
                    with Container(id="light") as container:
                        container.border_title = "QR background color"
                        yield Input(placeholder="e.g, green or hexadecimal format", id="qrlight")
                    
                    with Container(id="format") as container:
                        container.border_title = "Format"
                        yield SelectionList(
                            Selection("PNG", Format.PNG, True, id="png"),
                            Selection("PDF", Format.PDF, id="pdf"),
                            Selection("SVG", Format.SVG, id="svg"),
                            id="qrformat"
                        )
                        # yield SelectionList(
                        #     *[
                        #         Selection(f.name, f.value, id=f.value)
                        #         for f in Format
                        #     ],
                        # )
                    
                
                yield Button("Generate QR!", id="qr_button")
                
class Form(Screen):
    """Main screen."""

    def compose(self) -> ComposeResult:
        """Compose the form screen."""
        yield FormHeader()
        yield FormGrid()
        yield Footer()
    
class QQR(App[None]):
    """Main application"""

    CSS_PATH = "res/tui.tcss"

    SCREENS = {"help": Help}
    """Pre-loaded screens for the application."""

    BINDINGS = [
        Binding("ctrl+d",
                "app.quit",
                "Exit"),
        Binding("ctrl+t",
                "toggle_theme",
                "Toggle Theme",
                tooltip = "To switch between two themes, light and dark."),
        Binding("question_mark",
                "app.push_screen('help')",
                "Help",
                tooltip="To show Help screen.",
                key_display="?",
                ),
    ]
    """Bindings"""

    TITLE = "QQR"
    """Application's title."""

    HORIZONTAL_BREAKPOINTS = [
        (0, "-narrow"),
        (40, "-normal"),
        (80, "-wide"),
        (120, "-very-wide"),
    ]
    """Breakpoints"""

    def on_mount(self) -> None:
        """Set up at startup."""
        self.theme = "nord"
        self.push_screen(Form())
        
    def action_toggle_theme(self) -> None:
        self.theme = (
        "nord" if self.theme == "gruvbox" else "gruvbox"
        )
        
if __name__ == "__main__":
    QQR().run()