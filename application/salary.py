from datetime import datetime
def calculate_salary(hours, rate):
    print(f'Дата вызова функции calculate_salary {datetime.now().date()}')
    print(hours*rate)

if __name__ == '__main__':
    calculate_salary(20, 300)