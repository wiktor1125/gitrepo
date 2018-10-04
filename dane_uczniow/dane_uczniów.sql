DROP TABLE IF EXISTS tbnazwiska;
DROP TABLE IF EXISTS tboceny;
DROP TABLE IF EXISTS tbdane_osobiste;


CREATE TABLE tbnazwiska
(
  nr_ucznia INTEGER PRIMARY KEY,
  nazwisko TEXT,
  imie TEXT,
  imie2 TEXT

);

CREATE TABLE tbdane_osobiste
(
 nr_ucznia INTEGER,
 dzien INTEGER,
 miesiac  INTEGER,
 rok INTEGER,
 miejsce_urodzenia TEXT,
 wojewodztwo TEXT,

FOREIGN KEY (nr_ucznia) REFERENCES tbnazwiska(nr_ucznia)

);



CREATE TABLE tboceny
(
 nr_ucznia INTEGER,
 zachowanie TEXT,
 rel  INTEGER,
 etyka INTEGER,
 jpol INTEGER,
 jang INTEGER,
 jniem INTEGER,
 mat INTEGER,
 hist INTEGER,
 geog INTEGER,
 biol INTEGER,
 fiz INTEGER,
 che INTEGER,
 tech INTEGER,
 info INTEGER,
 plas INTEGER,
 po INTEGER,
 wf INTEGER,
 
 FOREIGN KEY (nr_ucznia) REFERENCES tbnazwiska(nr_ucznia)
 
);

