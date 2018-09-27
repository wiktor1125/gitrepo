DROP TABLE IF EXISTS tbmiasta;


CREATE TABLE tbmiasta
(
  id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
  nazwa_miasta TEXT(30),
  wojewodztwo TEXT(35)
);

DROP TABLE IF EXISTS tbmieszkancy;

CREATE TABLE tbmieszkancy
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  liczba_mieszkancow  INTEGER,
  liczba_kobiet INTEGER,
  grupa_wiekowa TEXT(20),
  data_aktualizacji DATE,
  id_miasta INTEGER,
  FOREIGN KEY (id_miasta) REFERENCES tbmiasta(id)
  
);

DROP TABLE IF EXISTS tbpowierzchnie;

CREATE TABLE tbpowierzchnie
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  powierzchnia_miasta DECIMAL,
  powierzcnia_zielona INTEGER,
  data_aktualizacji DATE,
  id_miasta INTEGER,
  FOREIGN KEY (id_miasta) REFERENCES tbmieszkancy(id),
  FOREIGN KEY (id_miasta) REFERENCES tbmiasta(id)
);
