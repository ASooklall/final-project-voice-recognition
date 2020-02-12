DROP TABLE pokemon;
DROP TABLE pokemon_moves;

CREATE TABLE pokemon (
	pokemon_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	type1 VARCHAR(30) NOT NULL,
	type2 VARCHAR(30) NOT NULL,
	hp INT,
	atk INT,
	def INT,
	spd INT,
	move1 INT,
	move2 INT,
	move3 INT,
	move4 INT,
	front_image VARCHAR(30) NOT NULL,
	back_image VARCHAR(30) NOT NULL	
)

INSERT INTO pokemon (name, type1, type2, hp, atk, def, spd, move1, move2, move3, move4, front_image, back_image)
VALUES ('mewtwo', 'psychic', 'ptype2', 3, 1, 1, 1, 5, 6, 7, 8, 'images/mewtwo_front.png', 'images/mewtwo_back.png'),
('charizard', 'fire', 'flying', 3, 1, 1, 1, 9, 10, 11, 36, 'images/charizard_front.png', 'images/charizard_back.png'),
('venasaur', 'grass', 'ptype2', 3, 1, 1, 1, 12, 13, 14, 15, 'images/venasaur_front.png', 'images/venasaur_back.png'),
('blastoise', 'water', 'ptype2', 3, 1, 1, 1, 16, 17, 18, 19, 'images/blastoise_front.png', 'images/blastoise_back.png'),
('eevee', 'normal', 'ptype2', 3, 1, 1, 1, 2, 6, 14, 20, 'images/eevee_front.png', 'images/eevee_back.png'),
('onyx', 'rock', 'ground', 3, 1, 1, 1, 4, 21, 22, 23, 'images/onyx_front.png', 'images/onyx_back.png'),
('alakazam', 'psychic', 'ptype2', 3, 1, 1, 1, 5, 7, 8, 24, 'images/alakazam_front.png', 'images/alakazam_back.png'),
('gengar', 'ghost', 'poison', 3, 1, 1, 1, 25, 262, 27, 28, 'images/gengar_front.png', 'images/gengar_back.png'),
('nidoqueen', 'poison', 'ptype2', 3, 1, 1, 1, 29, 30, 31, 32, 'images/nidoqueen_front.png', 'images/nidoqueen_back.png'),
('machamp', 'fighting', 'ptype2', 3, 1, 1, 1, 18, 33, 34, 35, 'images/machamp_front.png', 'images/machamp_back.png');


CREATE TABLE pokemon_moves (
	move_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	power INT,
	type VARCHAR(30) NOT NULL,
	checker INT
);

INSERT INTO pokemon_moves (name, power, type, checker)
VALUES ('thundershock', 1, 'electric', 0),
('quick attack', 1, 'normal', 0),
('thunderbolt', 1, 'electric', 0),
('iron tail', 1, 'steel', 0),
('psychic', 1, 'psychic', 0),
('swift', 1, 'normal', 0),
('recover', 1, 'normal', 1),
('psybeam', 1, 'psychic', 0),
('fire blast', 1, 'fire', 0),
('slash', 1, 'normal', 0),
('steel wing', 1, 'steel', 0),
('solar beam', 1, 'grass', 0),
('razor leaf', 1, 'grass', 0),
('take down', 1, 'normal', 0),
('earthquake', 1, 'ground', 0),
('surf', 1, 'water', 0),
('hydro pump', 1, 'water', 0),
('strength', 1, 'normal', 0),
('water gun', 1, 'water', 0),
('last resort', 1, 'normal', 0),
('dig', 1, 'ground', 0),
('stone edge', 1, 'rock', 0),
('slam', 1, 'normal', 0),
('night shade', 1, 'ghost', 0),
('shadow ball', 1, 'ghost', 0),
('dark pulse', 1, 'dark', 0),
('hypnosis', 1, 'normal', 2),
('dream eater', 1, 'ghost', 0),
('body slam', 1, 'normal', 0),
('super power', 1, 'fighting', 0),
('counter', 1, 'fighting', 0),
('dragon tail', 1, 'dragon', 0),
('cross chop', 1, 'fighting', 0),
('dynamic punch', 1, 'fighting', 0),
('seismic toss', 1, 'fighting', 0),
('flamethrower', 1, 'fire', 0);



SELECT * FROM pokemon;
SELECT * FROM pokemon_moves;
