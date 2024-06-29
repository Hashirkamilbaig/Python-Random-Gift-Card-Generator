"""Assignment 4 Part 3"""
print(__doc__)
import sys
sys.path.append("..")
import random
from typing import IO

# Importing classes from file1
from a41.a41 import SvgCanvas, htmldocument

# Importing classes from file2
from a42.a42 import PyArtConfig, RandomShape

def generate_greeting_cards(filename: str) -> None:
    """Generating greeting cards"""
    """Writing html file"""
    with open(filename, "w") as f:
        i : int =0
        example1 = htmldocument(f, "Random Greeting Cards")
        example1.generate_html_file()
        # Generating random shapes
        config = PyArtConfig()
        shapes = config.generate_random_shape(1000)  # Generate how many shapes you want
        # Writing random shapes to the SVG canvas
        svg_canvas = SvgCanvas(f)
        svg_canvas.openSVGcanvas(2, (600, 400)) # Write canvas size
        svg_canvas.write_html_comment(3, "SVG")
        for shape in shapes:
            svg_canvas.write_html_line(3, shape.as_svg())
        svg_canvas.write_html_tail()
        

def main() -> None:
    """main method"""
    generate_greeting_cards("a433.html")

if __name__ == "__main__":
    main()