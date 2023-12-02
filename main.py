from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    get_employees('Ivan')
    calculate_salary(20, 600)