INSERT INTO encordadora (modelo, marca, estado)
VALUES
	('Wilson Baiardo', 'Wilson', 'disponible'),
	('Prince NEOS 1000', 'Prince', 'en uso'),
	('Gamma 6004', 'Gamma', 'en mantenimiento'),
	('Alpha Ghost', 'Alpha', 'en uso'),
	('Yonex Protech 8', 'Yonex', 'en uso');
    
INSERT INTO tension (valor)
VALUES
	(20),
	(16),
	(26),
	(28),
	(30);

INSERT INTO patron_encordado (cuerdas_verticales, cuerdas_horizontales)
VALUES
	(16,19),
	(18,20),
	(16,18),
	(14,16),
	(20,18),
	(16,15);

INSERT INTO cuerda (material, longitud)
VALUES
	('Tripa Natural', 12),
	('Nylon', 12),
	('Poliéster', 12),
	('Aramida', 12),
	('Poliamida', 12),
	('Vectran', 12);

INSERT INTO encordado (encordadora_id, tension_id, cuerda_id, patron_encordado_id)
VALUES
	(1, 2, 2, 2),
    (2, 4, 3, 5),
    (4, 5, 1, 3),
    (3, 3, 5, 1);
