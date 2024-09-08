create schema maquina_raquetas;
use maquina_raquetas;

DROP TABLE IF EXISTS encordadora;
CREATE TABLE encordadora (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    estado ENUM('en uso', 'en mantenimiento', 'disponible')
);

DROP TABLE IF EXISTS tension;
CREATE TABLE tension (
    id INT AUTO_INCREMENT PRIMARY KEY,
    valor INT NOT NULL
);

DROP TABLE IF EXISTS patron_encordado;
CREATE TABLE patron_encordado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cuerdas_verticales INT NOT NULL,
    cuerdas_horizontales INT NOT NULL
);

DROP TABLE IF EXISTS cuerda;
CREATE TABLE cuerda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    material VARCHAR(50) NOT NULL,
    longitud INT NOT NULL
);

DROP TABLE IF EXISTS encordado;
CREATE TABLE encordado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    encordadora_id INT,
    tension_id INT,
    cuerda_id INT,
    patron_encordado_id INT,
    FOREIGN KEY (encordadora_id) REFERENCES encordadora(id),
    FOREIGN KEY (tension_id) REFERENCES tension(id),
    FOREIGN KEY (cuerda_id) REFERENCES cuerda(id),
    FOREIGN KEY (patron_encordado_id) REFERENCES patron_encordado(id)
);

