DROP TABLE IF EXISTS tbUczniowie;


CREATE TABLE tbUczniowie
(
  id_Ucznia INTEGER PRIMARY KEY AUTOINCREMENT,
  nazwisko TEXT,
  imie TEXT
  ulica TEXT,
  dom TEXT,
  id_Klasy INTEGER
 
);

DROP TABLE IF EXISTS tbOceny;

CREATE TABLE tbOceny
(
 id_Ucznia INTEGER NOT NULL,
 ocena INTEGER,
 data DATE,
 id_Przedmiotu INTEGER,
 FOREIGN KEY (id_ucznia) REFERENCES tbUczniowie(id_Ucznia)
 
);

DROP TABLE IF EXISTS tbPrzedmioty;

CREATE TABLE tbPrzedmioty
(
 id_Przedmiotu INTEGER NOT NULL,
 nazwa_Przedmiotu TEXT   
 nazwisko_Nauczyciela TEXT,
 imie_Naucz TEXT,
 FOREIGN KEY (id_Przedmiotu) REFERENCES tbOceny(id_Przedmiotu)

);
