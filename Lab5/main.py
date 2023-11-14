import ConsoleApp
import CubeObject

if __name__ == '__main__':
    cube = CubeObject.CubeObject()
    app = ConsoleApp.ConsoleInterface(cube)
    app.run()

