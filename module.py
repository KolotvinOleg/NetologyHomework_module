import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('data.csv', encoding='windows-1251')
    print(df.head())