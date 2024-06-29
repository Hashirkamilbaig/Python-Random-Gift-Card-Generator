#!/usr/bin/env python
"""Assignment 4 Part 1 Version 3 template"""
print(__doc__)

from typing import IO

class Circle:
    """CircleShape Class"""
    def __init__(self, cir: tuple, col: tuple) -> None:
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

class Rectangle:
    """RectangleShape Class"""
    def __init__(self, rec: tuple, col: tuple) ->None:
        self.rx: int = rec[0]
        self.ry: int = rec[1]
        self.width: int = rec[2]
        self.height: int = rec[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        

class HtmlComponent:
    """HTML Components SUPER CLASS"""

    def __init__(self, fd: IO[str]) -> None:
        self.fd: IO[str] = fd

    def write_html_comment(self, t: int, com: str) -> None:
        """Writing Html comment Method"""
        ts: str = "   " * t
        self.fd.write(f"{ts}<!-- {com} -->\n")

    def write_html_line(self, t: int, line: str) -> None:
        """Writing Html Line Method"""
        ts: str = "   " * t
        self.fd.write(f"{ts}{line}\n")

class SvgCanvas(HtmlComponent):
    """SvgCanvas class from HtmlComponent"""

    def __init__(self, fd: IO[str]) -> None:
        super().__init__(fd)

    def openSVGcanvas(self, t: int, canvas: tuple) -> None:
        """Start SVG canvas"""
        ts: str = "   " * t
        self.write_html_comment(t, "Define SVG drawing box")
        self.fd.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

    def drawCircleLine(self, t: int, c: Circle) -> None:
        """Write SVG command for Circle"""
        ts: str = "   " * t
        line1: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" '
        line2: str = f'fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
        self.fd.write(f"{ts}{line1+line2}\n")

    def drawRectangleLine(self, t: int, c: Rectangle) -> None:
        """Write SVG Command for Rectangle"""
        ts: str = "   " * t
        line1: str = f'<rect x="{c.rx}" y="{c.ry}" width="{c.width}" height="{c.height}" '
        line2: str = f'fill="rgb({c.red}, {c.green}, {c.blue})"/>'
        self.fd.write(f"{ts}{line1+line2}\n")

    def genArt(self, t: int) -> None:
        """Generate CircleShape"""
        self.drawCircleLine(t, Circle((50,50,50), (255,0,0,1.0)))
        self.drawCircleLine(t, Circle((150,50,50), (255,0,0,1.0)))
        self.drawCircleLine(t, Circle((250,50,50), (255,0,0,1.0)))
        self.drawCircleLine(t, Circle((350,50,50), (255,0,0,1.0)))
        self.drawCircleLine(t, Circle((450,50,50), (255,0,0,1.0)))
        self.drawCircleLine(t, Circle((50,250,50), (0,0,255,1.0)))
        self.drawCircleLine(t, Circle((150,250,50), (0,0,255,1.0)))
        self.drawCircleLine(t, Circle((250,250,50), (0,0,255,1.0)))
        self.drawCircleLine(t, Circle((350,250,50), (0,0,255,1.0)))
        self.drawCircleLine(t, Circle((450,250,50), (0,0,255,1.0)))

    def genArtRec(self, t: int) -> None:
        """Generate RecatangleShape"""
        self.drawRectangleLine(t, Rectangle((50,50,50,50), (255,0,0)))
    
    def write_html_tail(self) -> None:
        """End Html File"""
        self.write_html_line(1, "</svg>")
        self.write_html_line(0, "</body>")
        self.write_html_line(0, "</html>")

class htmldocument(HtmlComponent):
    """HTML Document class"""

    def __init__(self, fd: IO[str], title: str) -> None:
        super().__init__(fd)
        self.__title: str = title

    def generate_html_file(self) -> None:
        """Generate HTML File"""
        self.write_html_head()

    def generate_circles(self):
        """Generate CirclesShape"""
        svg_canvas = SvgCanvas(self.fd)
        svg_canvas.openSVGcanvas(1, (1000, 1000))
        svg_canvas.genArt(2)

    def write_html_head(self) -> None:
        """Write HTML Header"""
        self.write_html_line(0, "<html>")
        self.write_html_line(0, "<head>")
        self.write_html_line(1, f"<title>{self.__title}</title>")
        self.write_html_line(0, "</head>")
        self.write_html_line(0, "<body>")

    def write_html_tail(self) -> None:
        """Write HTML Tail"""
        self.write_html_line(1, "</svg>")
        self.write_html_line(0, "</body>")
        self.write_html_line(0, "</html>")

def main() -> None:
    """main Method"""
    with open("a41.html", "w") as f:
        hd: htmldocument = htmldocument(f, "My Art")
        hd.generate_html_file()
        hd.generate_circles()
        hd.write_html_tail()

if __name__ == "__main__":
    main()
