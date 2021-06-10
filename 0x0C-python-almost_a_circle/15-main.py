#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    Rectangle.save_to_file([Rectangle(3, 4), Rectangle(5, 8, 1), Rectangle(9, 1, 3, 2)])

    with open("Rectangle.json", "r") as file:
        print(file.read())
