from enum import Enum

class MD(str, Enum):
    HELP_S_MD = """
# **QQR** Help

Welcome to **QQR**, your terminal-based QR generator.  
This guide explains how to use **QQR** effectively.

## Encoding Modes
**QQR** uses the **Segno** library to automatically support the main QR Code encoding modes:

- **Byte mode**  
  Encodes any binary data (UTF-8 text, symbols, etc.). Most flexible.

- **Numeric mode**  
  Optimized for digits only (`0–9`). Produces the smallest QR code.

- **Alphanumeric mode**  
  Encodes a restricted character set (`0–9`, `A–Z`, space, and a few symbols).  
  More efficient than Byte when input matches.

- **Kanji mode**  
  Optimized for Japanese characters (Shift JIS).

- **Hanzi mode**  
  Optimized for simplified Chinese characters (GB2312).

## Error Correction Levels
QR Codes include redundancy to allow recovery from damage or dirt.  
You can pick the error tolerance level:

- **L (Low):** Recovers ~7% of data  
- **M (Medium):** Recovers ~15% of data  
- **Q (Quartile):** Recovers ~25% of data  
- **H (High):** Recovers ~30% of data  

## Export Formats
**QQR** lets you export QR codes in multiple formats:

- **PNG** → Standard raster image  
- **SVG** → Scalable vector image  
- **PDF** → Printable document  
- **ASCII** → Rendered as text in the terminal  
""",
    WELCOME_MD = """ 
# Create your QR
**Fill in the details below to generate your custom QR.**
"""