class secure_input:
    def __init__(self, data_type=str, error_message="Invalid input. Try again."):
        self.data_type = data_type
        self.error_message = error_message

    def get_input(self, prompt):
        while True:
            try:
                user_input = self.data_type(input(prompt))
                return user_input
            except ValueError:
                print(self.error_message)
