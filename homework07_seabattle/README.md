# Homework 07 - SeaBattle game
Task details in Russian:

Какие модели используются в игре?
- Игрок, свойства: очередь, имя
- Поле, свойства: размер, количество кораблей
- Корабль, свойства: размер (длина), место на поле
- Выстрел, свойства: кем, координаты, промах или попадание

Как будем хранить текущие данные?
- Нам нужно хранить: игроков, позиции кораблей, сделанные выстрелы
- Возможно использовать синглтон, смотри реализацию список дел и покупок

Какая последовательность действий?
- Создается пустое поле
- Создаются два игрока
- Каждый игрок по очередности правильным образом размещает все свои корабли на поле
- Перед каждым выстрелом отрисовывается новое поле, с известными выстрелами, пустыми пространствами и уничтоженными
кораблями
- По очереди каждый игрок делает выстрел, если выстрел приходится в цель, то игрок продолжает стрелять.
- Игра длится, пока все корабли одно из игроков не будут уничтожены