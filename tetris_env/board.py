import random

def random_bag():
    """Returns a bag with unique pieces ala classic tetris rules."""
    random_shapes = list(SHAPES)
    random.shuffle(random_shapes)
    return [Tetromino(0, 0, shape) for shape in random_shapes]



class Shape:
    def __init__(self, number, shapes):
        self.number = number
        self.shapes = shapes


class Tetromino:
    def __init__(self, x, y, shape: Shape, rotation=0):
        i =0

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]


# Define the Tetromino 'S' shape with both possible orientations
SHAPE_I = Shape(1, [
    [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]
    ],
    [
        [1, 1, 1, 1]
    ]
])

# Define the Tetromino 'O' shape
SHAPE_O = Shape(2, [
    [
        [1, 1],
        [1, 1]
    ]
])

# Define the Tetromino 'T' shape with all four possible orientations
SHAPE_T = Shape(3, [
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 0, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ]
])

# Define the Tetromino 'S' shape with both possible orientations
SHAPE_S = Shape(4, [
    [
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
    ],
    [
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
    ]
])

# Define the Tetromino 'Z' shape with both possible orientations
SHAPE_Z = Shape(5, [
    [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 0]
    ],
    [
        [0, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ]
])

# Define the Tetromino 'J' shape with all four possible orientations
SHAPE_J = Shape(6, [
    [
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
    ],
    [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 1]
    ],
    [
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 0]
    ]
])

# Define the Tetromino 'L' shape with all four possible orientations
SHAPE_L = Shape(7, [
    [
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ],
    [
        [0, 0, 0],
        [1, 1, 1],
        [1, 0, 0]
    ],
    [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
])

SHAPES = [SHAPE_I, SHAPE_O, SHAPE_T, SHAPE_S, SHAPE_Z, SHAPE_J, SHAPE_L]