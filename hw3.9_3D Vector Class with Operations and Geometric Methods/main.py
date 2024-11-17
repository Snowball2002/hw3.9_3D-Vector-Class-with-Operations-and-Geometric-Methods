# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Class Vector
class Vector:

    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c


    def getX(self):
        return self.x


    def getY(self):
        return self.y


    def getZ(self):
        return self.z


    def add(self, v):

        new_v_x = self.x + v.x

        new_v_y = self.y + v.y

        new_v_z = self.z + v.z

        new_v = Vector(new_v_x, new_v_y, new_v_z)

        return new_v


    def dotProduct(self, v):

        product = 0


        product += (self.y * v.y)

        product += (self.z * v.z)

        return product

if __name__ == '__main__':
    v1 = Vector(1, 1, 1)
    v2 = Vector(2, 3, 1)

    print("\nAdd Method New Vector : ")
    add_vector = v1.add(v2)
    print(add_vector.x, add_vector.y, add_vector.z)


    print("\n\nDot Product Method : ")
    product_answer = v1.dotProduct(v2)
    print(product_answer)


    class Vector:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def __str__(self):
            return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

        def __sub__(self, other):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

        def __mul__(self, other):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

        def __truediv__(self, other):
            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y and self.z == other.z

        def __ne__(self, other):
            return self.x != other.x or self.y != other.y or self.z != other.z

        def dotProduct(self, other):
            return self.x * other.x + self.y * other.y + self.z * other.z

        def crossProduct(self, other):
            return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                          self.x * other.y - self.y * other.x)

        def computeMagnitude(self):
            return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

        def normalize(self):
            magnitude = self.computeMagnitude()
            self.x = self.x / magnitude
            self.y = self.y / magnitude
            self.z = self.z / magnitude

        def scaleVector(self, factor):
            self.x = self.x * factor
            self.y = self.y * factor
            self.z = self.z * factor

        def projectOnto(self, v):
            return v * (self.dotProduct(v) / v.dotProduct(v))

        print("Paolo hw 3 ")