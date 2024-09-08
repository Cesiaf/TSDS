SELECT * FROM cuerda;
SELECT * FROM encordado;
SELECT * FROM encordadora;
SELECT * FROM tension;
SELECT * FROM cuerda;
SELECT * FROM patron_encordado;

SELECT material, longitud FROM cuerda;

SELECT id
FROM patron_encordado
WHERE cuerdas_verticales > 17;

SELECT id, material, longitud
FROM cuerda
ORDER BY id DESC;

SELECT id, material, longitud
FROM cuerda
ORDER BY id DESC
LIMIT 3;

SELECT id, cuerdas_verticales, cuerdas_horizontales
FROM patron_encordado
WHERE cuerdas_verticales > 13 AND cuerdas_horizontales < 18;

SELECT encordadora.marca, tension.valor, cuerda.material, patron_encordado.cuerdas_verticales, patron_encordado.cuerdas_horizontales
FROM encordado
JOIN encordadora ON encordado.encordadora_id = encordadora.id
JOIN tension ON encordado.tension_id = tension.id
JOIN cuerda ON encordado.cuerda_id = cuerda.id
JOIN patron_encordado ON encordado.patron_encordado_id = patron_encordado.id;

SELECT marca
FROM encordadora
WHERE id = (SELECT encordadora_id FROM encordado WHERE cuerda_id = '2');