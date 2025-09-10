import segno

def generate_qr(
    data: str,
    output: str = "qr.png",
    error: str = "H",
    dark: str = "black",
    light: str = "white",
    kind: str = "png",
):
    """
    Generate a QR code with segno.
    """
    qr = segno.make(
        content = data,
        error = error,
    )

    qr.save(
        output,
        kind = kind,
        dark = dark,
        light = light,
    )
    
    return output