def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")


def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14159 * (radius ** 2)  # Using π ≈ 3.14159
    print(f"The area of the circle is: {area:.2f}")


def triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")


rectangle_area()
circle_area()
triangle_area()
