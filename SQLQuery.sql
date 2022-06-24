use artgallery;

CREATE TABLE Художник
(
  `Код художника` INT NOT NULL,
  Фамилия VARCHAR(255) NOT NULL,
  Имя VARCHAR(255) NOT NULL,
  Отчество VARCHAR(255) NOT NULL,
  `Дата рождения` VARCHAR(255) NOT NULL,
  `Место рождения` VARCHAR(255) NOT NULL,
  Жанр VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Код художника`)
);

CREATE TABLE Выставки
(
  `Код выставки` INT NOT NULL,
  `Тема выставки` VARCHAR(255) NOT NULL,
  `Дата начала` DATE NOT NULL,
  `Дата окончания` DATE NOT NULL,
  PRIMARY KEY (`Код выставки`)
);

CREATE TABLE `Тип картины`
(
  `Код типа` INT NOT NULL,
  Тип VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Код типа`)
);

CREATE TABLE `Техника картины`
(
  `Код техники` INT NOT NULL,
  Техника VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Код техники`)
);

CREATE TABLE Зал
(
  `Код зала` INT NOT NULL,
  `Наименование зала` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`Код зала`)
);

CREATE TABLE Категории
(
  `Код категории` INT NOT NULL,
  `Скидка (%)` INT NOT NULL,
  `Наименование категории` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Код категории`)
);

CREATE TABLE Сотрудник
(
  `Код сотрудника` INT NOT NULL,
  Фамилия VARCHAR(255) NOT NULL,
  Имя VARCHAR(255) NOT NULL,
  Отчество VARCHAR(255) NOT NULL,
  Должность VARCHAR(255) NOT NULL,
  `Дата рождения` DATE NOT NULL,
  `Паспортные данные` INT NOT NULL,
  Логин VARCHAR(255) NOT NULL,
  Пароль VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Код сотрудника`)
);

CREATE TABLE Посетитель
(
  `Код посетителя` INT NOT NULL,
  Фамилия VARCHAR(255) NOT NULL,
  Имя VARCHAR(255) NOT NULL,
  Отчество VARCHAR(255) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  `Дата рождения` INT NOT NULL,
  PRIMARY KEY (`Код посетителя`)
);

CREATE TABLE `История входа`
(
  `Код авторизации` INT NOT NULL,
  `Время входа` DATETIME NOT NULL,
  `Код сотрудника` INT,
  PRIMARY KEY (`Код авторизации`),
  FOREIGN KEY (`Код сотрудника`) REFERENCES Сотрудник(`Код сотрудника`)
);

CREATE TABLE Картина
(
  `Код картины` INT NOT NULL,
  Название VARCHAR(255) NOT NULL,
  `Дата написания` VARCHAR(255) NOT NULL,
  `Код художника` INT NOT NULL,
  `Код техники` INT NOT NULL,
  `Код типа` INT NOT NULL,
  PRIMARY KEY (`Код картины`),
  FOREIGN KEY (`Код художника`) REFERENCES Художник(`Код художника`),
  FOREIGN KEY (`Код техники`) REFERENCES `Техника картины`(`Код техники`),
  FOREIGN KEY (`Код типа`) REFERENCES `Тип картины`(`Код типа`)
);

CREATE TABLE `Выставленные картины`
(
  `Код картины` INT,
  `Код выставки` INT NOT NULL,
  `Код зала` INT NOT NULL,
  FOREIGN KEY (`Код картины`) REFERENCES Картина(`Код картины`),
  FOREIGN KEY (`Код выставки`) REFERENCES Выставки(`Код выставки`),
  FOREIGN KEY (`Код зала`) REFERENCES Зал(`Код зала`)
);

CREATE TABLE Билет
(
  `Код билета` INT NOT NULL,
  `Штрих-код` VARCHAR(255) NOT NULL,
  `Дата посещения` DATE NOT NULL,
  `Код категории` INT NOT NULL,
  `Код выставки` INT NOT NULL,
  `Код посетителя` INT NOT NULL,
  `Код сотрудника` INT NOT NULL,
  PRIMARY KEY (`Код билета`),
  FOREIGN KEY (`Код категории`) REFERENCES Категории(`Код категории`),
  FOREIGN KEY (`Код выставки`) REFERENCES Выставки(`Код выставки`),
  FOREIGN KEY (`Код посетителя`) REFERENCES Посетитель(`Код посетителя`),
  FOREIGN KEY (`Код сотрудника`) REFERENCES Сотрудник(`Код сотрудника`)
);