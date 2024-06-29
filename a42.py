"""Assignment 4 Part 2"""
print(__doc__)
import random

class Shape:
    """CircleShape Class"""
    shape_count = 0

    def __init__(self, kind_of_shape, x_coordinate, y_coordinate, radius, rx, ry, rectangle_width,
                 rectangle_height, color_red, color_green, color_blue, shape_opacity):
        self.kind_of_shape = kind_of_shape
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.radius = radius
        self.rx = rx
        self.ry = ry
        self.rectangle_width = rectangle_width
        self.rectangle_height = rectangle_height
        self.color_red = color_red
        self.color_green = color_green
        self.color_blue = color_blue
        self.shape_opacity = shape_opacity
        self.shape_id = Shape.shape_count
        Shape.shape_count += 1

    def __str__(self):
        """Writing Object Data Method"""
        return f"Shape {self.shape_id}: Kind of Shape: {self.kind_of_shape}, Coordinates: ({self.x_coordinate}, {self.y_coordinate}), " \
               f"Radius: {self.radius}, RX: {self.rx}, RY: {self.ry}, Rectangle Width: {self.rectangle_width}, " \
               f"Rectangle Height: {self.rectangle_height}, Color (R, G, B): ({self.color_red}, {self.color_green}, {self.color_blue}), " \
               f"Opacity: {self.shape_opacity}"

    def as_Part2_line(self):
        """Writing Object Data in Table format Method"""
        return f"{self.shape_id:>3} {self.kind_of_shape:>3} {self.x_coordinate:>3} {self.y_coordinate:>3} {self.radius:>3} {self.rx:>3} {self.ry:>3} {self.rectangle_width:>3} {self.rectangle_height:>3} {self.color_red:>3} {self.color_green:>3} {self.color_blue:>3} {self.shape_opacity:>3}"
   
    def as_svg(self):
        """Writing SVG Commands Method"""
        if self.kind_of_shape == 0:  # Circle
            return f"<circle cx='{self.x_coordinate}' cy='{self.y_coordinate}' " \
                   f"r='{self.radius}' fill='rgb({self.color_red},{self.color_green},{self.color_blue})' " \
                   f"opacity='{self.shape_opacity}'></circle>"
        elif self.kind_of_shape == 1:  # Rectangle
            return f"<rect x='{self.x_coordinate}' y='{self.y_coordinate}' " \
                   f"width='{self.rectangle_width}' height='{self.rectangle_height}' " \
                   f"fill='rgb({self.color_red},{self.color_green},{self.color_blue})' " \
                   f"opacity='{self.shape_opacity}'></rect>"
        elif self.kind_of_shape == 2:  # Ellipse
            return f"<ellipse cx='{self.x_coordinate}' cy='{self.y_coordinate}' " \
                   f"rx='{self.rx}' ry='{self.ry}' fill='rgb({self.color_red},{self.color_green},{self.color_blue})' " \
                   f"opacity='{self.shape_opacity}'></ellipse>"

class PyArtConfig:
    """Shape ArtWork"""
    default_ranges = {
        'kind_of_shape': (0, 2),  # 0: circle, 1: rectangle, 2: ellipse
        'x_coordinate': (0, 600),
        'y_coordinate': (0, 400),
        'radius': (0, 100),
        'rx': (10, 30),
        'ry': (10, 30),
        'rectangle_width': (10, 100),
        'rectangle_height': (10, 100),
        'color_red': (0, 255),
        'color_green': (0, 255),
        'color_blue': (0, 255),
        'shape_opacity': (0.0, 1.0)
    }

    def __init__(self, **kwargs):
        """Using default values and using keyword argument"""
        self.ranges = {param: kwargs.get(param, self.default_ranges[param]) for param in self.default_ranges}
        self.shape_count = 0

    def generate_random_shape(self, num_shapes: int):
        """Generate Random Shapes"""
        shapes = []
        for _ in range(num_shapes):  # Up to ten shapes
            kind_of_shape = random.randint(*self.ranges['kind_of_shape'])
            x_coordinate = random.randint(*self.ranges['x_coordinate'])
            y_coordinate = random.randint(*self.ranges['y_coordinate'])
            radius = random.randint(*self.ranges['radius'])
            rx = random.randint(*self.ranges['rx'])
            ry = random.randint(*self.ranges['ry'])
            rectangle_width = random.randint(*self.ranges['rectangle_width'])
            rectangle_height = random.randint(*self.ranges['rectangle_height'])
            color_red = random.randint(*self.ranges['color_red'])
            color_green = random.randint(*self.ranges['color_green'])
            color_blue = random.randint(*self.ranges['color_blue'])
            shape_opacity = round(random.uniform(*self.ranges['shape_opacity']), 1)

            shape = Shape(kind_of_shape, x_coordinate, y_coordinate, radius, rx, ry, rectangle_width,
                          rectangle_height, color_red, color_green, color_blue, shape_opacity)
            shapes.append(shape)
            self.shape_count += 1
        
        return shapes

class RandomShape:
    """RandomShape Class"""
    def __init__(self, art_config):
        self.art_config = art_config
        self.shapes = self.art_config.generate_random_shape(10)

    def __str__(self):
        """Writing object values"""
        result = ""
        for shape in self.shapes:
            result += str(shape) + "\n"
        return result

    def as_Part2_line(self):
        """Table for Object Values"""
        print("CNT"+ " "+ "SHA"+" "+" "+" "+ "X" +" "+" "+" "+ "Y" +" "+ "RAD" + " " + " " + "RX" +" "+" "+"RY"+" "+" "+" " + "W" +" "+" "+" "+ "H" +" "+" "+" "+ "R"+" "+" "+" "+ "G" +" "+" "+" "+ "B"+" "+" "+"OP")
        result = ""
        
        for shape in self.shapes:
            result += shape.as_Part2_line() + "\n"
        return result

    def as_svg(self):
        """SVG commands for Random Shape generated"""
        result = ""
        for shape in self.shapes:
            result += shape.as_svg() + "\n"
        return result
    
def main():
    """main method"""
    config = PyArtConfig()
    shape = RandomShape(config)
    print("Random Shapes:")
    print(shape)
    print("As Part 2 Lines:")
    print(f"{shape.as_Part2_line()}")
    print("As SVG:")
    print(f"{shape.as_svg()}")
    print(__doc__)

if __name__ == "__main__":
    main()
