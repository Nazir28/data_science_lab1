import os

import pandas as pd
import matplotlib.pyplot as plt


def tips():
    # 1) Выясните, сколько в среднем выходи полный счёт по пятницам на ланч у курящих мужчин (датасет tips)
    file_path = 'data/tips.csv'
    df = pd.read_csv(file_path)
    friday_smoking_male = df[(df['day'] == 'Fri') & (df['sex'] == 'Male')]
    average_total_bill = friday_smoking_male['total_bill'].mean()
    return average_total_bill


def iris():
    # 2) Загрузите iris и посмотрите разбросы по всем числовым значениям для всех трёх классов цветов (датасет iris)
    output_dir = 'графики'
    os.makedirs(output_dir, exist_ok=True)

    file_path = 'data/iris.csv'
    df = pd.read_csv(file_path)
    setosa = df[df['Name'] == 'Iris-setosa']
    versicolor = df[df['Name'] == 'Iris-versicolor']
    virginica = df[df['Name'] == 'Iris-virginica']

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 2, 1)
    plt.hist(setosa['SepalLength'], alpha=0.5, label='Iris-setosa')
    plt.hist(versicolor['SepalLength'], alpha=0.5, label='Iris-versicolor')
    plt.hist(virginica['SepalLength'], alpha=0.5, label='Iris-virginica')
    plt.xlabel('Sepal Length')
    plt.ylabel('Frequency')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.hist(setosa['SepalWidth'], alpha=0.5, label='Iris-setosa')
    plt.hist(versicolor['SepalWidth'], alpha=0.5, label='Iris-versicolor')
    plt.hist(virginica['SepalWidth'], alpha=0.5, label='Iris-virginica')
    plt.xlabel('Sepal Width')
    plt.ylabel('Frequency')
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.hist(setosa['PetalLength'], alpha=0.5, label='Iris-setosa')
    plt.hist(versicolor['PetalLength'], alpha=0.5, label='Iris-versicolor')
    plt.hist(virginica['PetalLength'], alpha=0.5, label='Iris-virginica')
    plt.xlabel('Petal Length')
    plt.ylabel('Frequency')
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.hist(setosa['PetalWidth'], alpha=0.5, label='Iris-setosa')
    plt.hist(versicolor['PetalWidth'], alpha=0.5, label='Iris-versicolor')
    plt.hist(virginica['PetalWidth'], alpha=0.5, label='Iris-virginica')
    plt.xlabel('Petal Width')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'график4.png'))
    plt.clf()
    plt.tight_layout()
    plt.show()


def data_frame():
    # 3) Создайте новый столбец с плотностью населения. Переименуйте названия первого и третьего столбца на русский язык
    df = pd.DataFrame({
        'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
        'population': [17.04, 143.5, 9.5, 45.5],
        'square': [2724902, 17125191, 207600, 603628]
    })
    df['density'] = df['population'] / df['square']
    df.rename(
        columns={'country': 'Страна', 'population': 'Население', 'square': 'Площадь', 'density': 'Плотность населения'},
        inplace=True)

    return df


def run_dz_3():
    print("Задача 3 Pandas")
    print("Средний total_bill для курящих мужчин по пятницам:", tips())
    iris()
    print(data_frame())
