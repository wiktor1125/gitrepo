DROP TABLE IF EXISTS tbUczniowie;

CREATE TABLE tbUczniowie( 
id INTEGER PRIMARY KEY AUTOINCREMENT, 
imie TEXT,
nazwisko TEXT,
plec BOOLEAN,
id_klasa INTEGER,
egz_hum NUMERIC NOT NULL DEFAULT 0,
egz_mat NUMERIC NOT NULL DEFAULT 0,
egz_jez NUMERIC NOT NULL DEFAULT 0,
FOREIGN KEY (id_klasa) REFERENCES klasy(id)
);

DROP TABLE IF EXISTS tbKlasy;

CREATE TABLE tbKlasy(
id INTEGER PRIMARY KEY AUTOINCREMET,
klasa TEXT,
rok_naboru STRING,
rok_matury STRING


);

DROP TABLE IF EXISTS tbPrzedmioty;

CREATE TABLE tbPrzedmioty(
id INTEGER PRIAMRY KEY AUTOINCREMENT,
przedmiot TEXT,
imie_naucz TEXT,
nazwisko_naucz TEXT,
plec_naucz BOOLEAN
);

DROP TABLE IF EXISTS tbOceny;

CREATE TABLE tbOceny(
id INTEGER NOT NULL,
datad DATE,
id_uczen INTEGER NOT NULL,
id_przedmiot INTEGER NOT NULL,
ocena INTEGER NOT NULL,
FOREIGN KEY (id_uczen) REFERENCES uczniowie(id),
FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
);
