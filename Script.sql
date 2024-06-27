CREATE DATABASE Друзья_человека;
USE Друзья_человека;

CREATE TABLE Животные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(50),
    дата_рождения DATE
);

CREATE TABLE Домашние_животные (
    id INT PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES Животные(id)
);

CREATE TABLE Вьючные_животные (
    id INT PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES Животные(id)
);

CREATE TABLE Собаки (
    id INT PRIMARY KEY,
    команда VARCHAR(100),
    FOREIGN KEY (id) REFERENCES Домашние_животные(id)
);

CREATE TABLE Кошки (
    id INT PRIMARY KEY,
    команда VARCHAR(100),
    FOREIGN KEY (id) REFERENCES Домашние_животные(id)
);

CREATE TABLE Хомяки (
    id INT PRIMARY KEY,
    команда VARCHAR(100),
    FOREIGN KEY (id) REFERENCES Домашние_животные(id)
);

CREATE TABLE Лошади (
    id INT PRIMARY KEY,
    команда VARCHAR(100),
    FOREIGN KEY (id) REFERENCES Вьючные_животные(id)
);

CREATE TABLE Верблюды (
    id INT PRIMARY KEY,
    команда VARCHAR(100),
    FOREIGN KEY (id) REFERENCES Вьючные_животные(id)
);

CREATE TABLE Ослы (
    id INT PRIMARY KEY,
    команда VARCHAR(100),
    FOREIGN KEY (id) REFERENCES Вьючные_животные(id)
);

INSERT INTO Животные (имя, дата_рождения) VALUES 
('Шарик', '2022-01-01'),
('Мурка', '2021-05-15'),
('Хома', '2020-08-08'),
('Буцефал', '2019-04-20'),
('Гоша', '2018-11-11'),
('Иа', '2020-02-28');

INSERT INTO Домашние_животные (id) VALUES 
(1), (2), (3);

INSERT INTO Вьючные_животные (id) VALUES 
(4), (5), (6);

INSERT INTO Собаки (id, команда) VALUES 
(1, 'сидеть');

INSERT INTO Кошки (id, команда) VALUES 
(2, 'дай лапу');

INSERT INTO Хомяки (id, команда) VALUES 
(3, 'крутить колесо');

INSERT INTO Лошади (id, команда) VALUES 
(4, 'бежать');

INSERT INTO Верблюды (id, команда) VALUES 
(5, 'нести груз');

INSERT INTO Ослы (id, команда) VALUES 
(6, 'брести');

CREATE TABLE Лошади_Ослы AS 
SELECT * FROM Лошади
UNION
SELECT * FROM Ослы;

CREATE TABLE Молодые_животные AS
SELECT id, имя, TIMESTAMPDIFF(MONTH, дата_рождения, CURDATE()) AS возраст_в_месяцах
FROM Животные
WHERE TIMESTAMPDIFF(YEAR, дата_рождения, CURDATE()) BETWEEN 1 AND 3;