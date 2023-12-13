from labs.classes.Lab5.Rectangle import Rectangle

class ConsoleRectangle(Rectangle):
    figure = Rectangle

    @classmethod
    def set_parameters(cls, dct, input_message):
        for key, value in dct.items():
            print(f"{key}: {value}")
        value = input(f"Select {input_message}: ")
        current_value = dct.get(value, None)
        if current_value:
            return current_value
        else:
            return None

    def input_function(self, dct, input_message, default):
        check = input(f"do you want to set {input_message}? (y/n): ")
        font = None
        if check == '1':
            font = self.set_parameters(dct, input_message)
        if font:
            return font
        else:
            return default

    def configuration(self):
        rect_to_draw = Rectangle()
        self.size_x = int(input("Input size_x: "))
        self.size_y = int(input("Input size_y: "))
        self.size_z = int(input("Input size_z: "))

        self._color_1 = self.input_function(self._COLORS, 'color_1', self._color_1)
        self._color_2 = self.input_function(self._COLORS, 'color_2', self._color_2)
        self._color_3 = self.input_function(self._COLORS, 'color_3', self._color_3)

        change_space = input('do you want to create space? (y/n): ')
        if change_space == 'y':
            space = int(input("Input space: "))
            self._space(space)

        change_zoom = input('do you want to create zoom? (y/n): ')
        if change_zoom == '1':
            self._zoom = int(input("Input zoom: "))
            self.set_zoom()

    def save_object(self, obj, filename):
        try:
            with open(f"{filename}.txt", 'w') as file:
                for line in obj:
                    file.write(str(line) + "\n")
            print(f"Object saved successfully to {filename}.txt")
        except Exception as e:
            print(f"Error occurred while saving: {e}")

    def run(self):
        stop = ''
        while stop != 'f':
            try:
                self.configuration()
                self.create()
                print(self)
            except Exception as e:
                print(e)
            finally:
                stop = input("Press 'f' if you want to exit: ")