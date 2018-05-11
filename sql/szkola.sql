DROP TABLE IF EXISTS tbUczniowie
DROP TABLE IF EXISTS tbKlasy


CREATE TABLE tbUczniowie
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  imie TEXT,
  nazwisko TEXT,
  plec INTEGER,
  id_klasy INTEGER,
  egzHum NUMERIC NOT NULL DEFAULT 0,
  egzMat NUMERIC NOT NULL DEFAULT 0,
  egzJez NUMERIC NOT NULL DEFAULT 0,
  FOREIGN KEY (id_klasa) REFERENCES tbKlasy(id)
);

CREATE TABLE tbKlasy
(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 klasa TEXT,
 rokNaboru INTEGER,
 rokMatury INTEGER,
);

INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1A', 2017,2020);
INSERT INTO tbKlasy VALUES (NULL, '2A', 2016,2019);
INSERT INTO tbKlasy VALUES (NULL, '1C', 2017,2020);

INSERT INTO tbUczniowie(id, klasa, nazwisko, ple, id_klasa, egzHum, egzMat, egzJez)
VALUES (NULL, 'Adam', 'Słodowy', 0, 3, 70.5, 80, 90);

INSERT INTO tbUczniowie(id, klasa, nazwisko, ple, id_klasa, egzHum, egzMat, egzJez)
VALUES (NULL, 'Dorota', 'Ładna', 0, 1, 60.5, 80, 60);

UPDATE tbUczniowie SET egzJez = 100 WHERE id = 1;