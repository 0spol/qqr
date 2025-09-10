from enum import Enum

class ErrorTolerance(str, Enum):
    L = "l"
    M = "m"
    Q = "q"
    H = "h"

class Format(str, Enum):
    PNG = "png"
    SVG = "svg"
    PDF = "pdf"
    EPS = "eps"
    TXT = "txt"
    PBM = "pbm"
    PAM = "pam"
    PPM = "ppm"
    TEX = "tex"
    XBM = "xbm"
    XPM = "xpm"