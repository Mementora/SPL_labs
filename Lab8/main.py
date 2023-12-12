from csv_visualizer import MockDataVisualizer

def main():
    csv_filepath = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/Lab8/Data/MOCK_DATA.csv'

    while True:
        data_visualizer = MockDataVisualizer(csv_filepath)

        data_visualizer.explore_data()

        user_choice = user_choice = input("1. Кругова діаграма \n2. Діаграма розсіювання \n3. Стовпцева діаграма \n4. Вивести всі діаграми \nВведіть номер діаграми (1-4) або 'x' для виходу: ")

        if user_choice.lower() == 'x':
            break

        data_visualizer.visualize_data(user_choice)

if __name__ == '__main__':
    main()