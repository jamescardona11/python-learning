-- Tested https://sqliteonline.com
--
-- Table structure for table animal
--

CREATE TABLE IF NOT EXISTS Animal (
  AnimalId INTEGER PRIMARY KEY AUTOINCREMENT,
  Name VARCHAR(255),
  Age INTEGER,
  FavoriteFood VARCHAR(50),
  Type VARCHAR(50) DEFAULT 'Cat'
);


CREATE TABLE IF NOT EXISTS AnimalPastName (
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  Name VARCHAR(255) NOT NULL,
  AnimalId FOREIGNKEY REFERENCES Animal(AnimalId)
);



--
-- Dumping data for table animal
--

INSERT INTO Animal (AnimalId, Name, Age, FavoriteFood, Type) VALUES
(1, 'Poncho', 5, NULL, 'Cat'),
(2, 'Mateo', 6, 'Fish', 'Cat'),
(3, 'Coco', 8, 'Chiken', 'Dog');



INSERT INTO AnimalPastName (Id, Name, AnimalId) VALUES
('Poncho', 1);
('Miguel', 1),
('Bert', 1),
('Albert', 1);


SELECT * FROM Animal
SELECT * FROM AnimalPastName
SELECT * FROM Animal WHERE type = "Cat"
SELECT name FROM AnimalPastName where animalid = 1