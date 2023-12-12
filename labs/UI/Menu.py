class main:
    if __name__ == '__main__':
        print("if you want to open lab1, press 1:")
        print("if you want to open lab2, press 2:")
        print("if you want to open lab3, press 3:")
        print("if you want to open lab4, press 4:")
        print("if you want to open lab5, press 5:")
        print("if you want to open lab6, press 6:")
        print("if you want to open lab7, press 7:")

        user_choice = input()
    if user_choice == '1':
            import labs.UI.Menu_Builder.Lab1.LabMenu1 as menu1

            calculator_lab1 = menu1.LabMenu1()
            calculator_lab1.run()

    if user_choice == '2':
            import labs.UI.Menu_Builder.Lab2.LabMenu2 as menu2
            import labs.classes.Lab2.Solutions
            calculator_lab2_instance = labs.classes.Lab2.Calculator()
            calculator = menu2.LabMenu2(calculator_lab2_instance)
            calculator.run()

    if user_choice == '3':
            import labs.UI.Menu_Builder.Lab3.LabMenu3 as menu3
            ascii_art_generator = menu3.LabMenu3()
            user_input, selected_font, selected_color, width, height, char_set, preview_enabled = ascii_art_generator.get_user_input()
            if preview_enabled == 'y':
                ascii_text = ascii_art_generator.generate_ascii_art(user_input, selected_font, selected_color, width, height,
                                                              char_set)
                ascii_art_generator.preview_ascii_art(ascii_text, selected_color)
                ascii_art_generator.ask_save_ascii_art(ascii_text)

    if user_choice == '4':
        import labs.UI.Menu_Builder.Lab4.LabMenu4 as menu4
        import labs.classes.Lab4.ASCIIArtGenerator
        ascii_generator = labs.classes.Lab4.ASCIIArtGenerator.AsciiArtGenerator()
        ascii = menu4.LabMenu4(ascii_generator)
        ascii.run()

    if user_choice == '5':
        import labs.UI.Menu_Builder.Lab5.LabMenu5 as menu5
        rectangle = menu5.ConsoleInterface()
        rectangle.run()

    if user_choice == '6':
        import labs.UI.Menu_Builder.Lab6.LabMenu6 as menu6
        tests = menu6.LabMenu6()
        tests.run_tests()

    if user_choice == '7':
        import labs.UI.Menu_Builder.Lab7.LabMenu7 as menu7
        api_caller = menu7.MenuLab7()
        api_caller.main()


