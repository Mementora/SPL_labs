import CubeObject
import pickle

class ConsoleInterface:
    def __init__(self, cube):
        self.cube = cube
        pass

    def run(self):
        self.print_interface()

    #print both menu and object
    def print_interface(self):
        cube = CubeObject.CubeObject()
        print("To draw a cube, press 1: ")
        user_choice = input()
        if user_choice == '1':
            self.set_cube_preferences()
            cube_to_draw = cube.build_3d(self.x, self.y, self.z)
            for i in cube_to_draw:
                print(i)
            self.save_option(cube_to_draw)

    #let the user to set preferences of object
    def set_cube_preferences(self):
        print("please enter the x, y and z value:")
        self.x = int(input("x: "))
        self.y = int(input("y: "))
        self.z = int(input("z: "))

    #provide option to save object
    def save_option(self, obj_to_save):
        print("do you want to save the object? (y or n)")
        user_choice = input()
        if user_choice == 'y':
            file_name = input("enter the file name: ")
            self.save_object(obj_to_save, file_name)

    #save project into a text file
    def save_object(self, obj, filename):
        try:
            with open(f"{filename}.txt", 'w') as file:
                for line in obj:
                    file.write(str(line) + "\n")
            print(f"Object saved successfully to {filename}.txt")
        except Exception as e:
            print(f"Error occurred while saving: {e}")

