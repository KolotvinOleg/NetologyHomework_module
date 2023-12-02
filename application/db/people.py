from datetime import datetime

def get_employees(name):
    print(f'Дата вызова функции get_employees {datetime.now().date()}')
    print(f'Сотдник {name} готов к работе')

if __name__ == '__main__':
    get_employees('Oleg')