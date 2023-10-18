class ConsoleApp:
    def __init__(self, ascii):
        self.ascii = ascii

    def run(self):
        self.user_interface()

    def user_interface(self):
        while True:
            print("press 1 to print ascii art to console")
            print("press 2 to customize ascii art style")
            user_choice = input()
            if user_choice == '1':
                text = input("enter text: ")
                self.ascii.perform_ascii_covnentor(text)


