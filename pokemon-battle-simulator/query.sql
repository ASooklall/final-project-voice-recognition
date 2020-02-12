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
VALUES ('pikachu', 'electric', 'none', 8, 15, 10, 17, 1, 2, 3, 4, 'images/pikachu_front.png', 'images/pikachu_back.png'),
('mewtwo', 'psychic', 'none', 12, 16, 9, 13, 5, 6, 7, 8, 'images/mewtwo_front.png', 'images/mewtwo_back.png'),
('charizard', 'fire', 'flying', 11, 15, 11, 13, 9, 10, 11, 12, 'images/charizard_front.png', 'images/charizard_back.png'),
('venasaur', 'grass', 'poison', 12, 13, 14, 11, 13, 14, 15, 16, 'images/venasaur_front.png', 'images/venasaur_back.png'),
('blastoise', 'water', 'none', 11, 13, 15, 11, 17, 18, 19, 20, 'images/blastoise_front.png', 'images/blastoise_back.png'),
('eevee', 'normal', 'none', 12, 11, 14, 13, 21, 2, 22, 4, 'images/eevee_front.png', 'images/eevee_back.png'),
('onyx', 'rock', 'ground', 8, 8, 24, 10, 23, 16, 24, 3, 'images/onyx_front.png', 'images/onyx_back.png'),
('alakazam', 'psychic', 'none', 7, 17, 11, 15, 5, 25, 26, 27, 'images/alakazam_front.png', 'images/alakazam_back.png'),
('gengar', 'ghost', 'poison', 8, 18, 10, 14, 7, 28, 29, 30, 'images/gengar_front.png', 'images/gengar_back.png'),
('nidoqueen', 'ground', 'poison', 14, 13, 12, 11, 16, 31, 8, 32, 'images/nidoqueen_front.png', 'images/nidoqueen_back.png'),
('machamp', 'fighting', 'none', 13, 18, 12, 7, 33, 34, 35, 36, 'images/machamp_front.png', 'images/machamp_back.png'),
('gyarados', 'water', 'flying', 12, 16, 12, 10, 17, 29, 37, 38, 'images/gyarados_front.png', 'images/gyarados_back.png'),
('scizor', 'bug', 'steel', 11, 17, 14, 8, 39, 40, 41, 42, 'images/scizor_front.png', 'images/scizor_back.png'),
('snorlax', 'normal', 'none', 18, 13, 13, 6, 43, 5, 9, 44, 'images/snorlax_front.png', 'images/snorlax_back.png'),
('dragonite', 'dragon', 'flying', 13, 16, 12, 9, 45, 46, 47, 48, 'images/dragonite_front.png', 'images/dragonite_back.png'),
('dewgone', 'water', 'ice', 13, 11, 14, 12, 49, 50, 46, 51, 'images/dewgong_front.png', 'images/dewgong_back.png'),
;


CREATE TABLE pokemon_moves (
	move_id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	power INT,
	type VARCHAR(30) NOT NULL,
	checker INT
);

INSERT INTO pokemon_moves (name, power, type, priority)
VALUES ('thunderbolt', 21, 'electric', 0),
('quick attack', 18, 'normal', 1),
('slam', 24, 'normal', 0),
('iron tail', 21, 'steel', 0),
('psychic', 21, 'psychic', 0),
('hyperbeam', 24, 'normal', 0),
('shadow ball', 21, 'ghost', 0),
('poison jab', 21, 'poison', 0),
('fire blast', 21, 'fire', 0),
('slash', 24, 'normal', 0),
('dragon claw', 21, 'dragon', 0),
('hurricane', 21, 'flying', 0),
('solar beam', 21, 'grass', 0),
('sludge bomb', 21, 'poison', 0),
('take down', 24, 'normal', 0),
('earthquake', 12, 'ground', 0),
('hydro pump', 21, 'water', 0),
('skull bash', 24, 'normal', 0),
('blizzard', 21, 'ice', 0),
('flash cannon', 21, 'steel', 0),
('swift', 24, 'noraml', 0),
('bite', 21, 'dark', 0),
('stone edge', 21, 'rock', 0),
('dragon breath', 21, 'dragon', 0),
('seismic toss', 21, 'fighting', 0),
('thunder punch', 21, 'electric', 0),
('ice punch', 21, 'ice', 0),
('sucker punch', 15, 'dark', 1),
('thunder', 21, 'electric', 0),
('dream eater', 21, 'psychic', 0),
('super power', 21, 'fighting', 0),
('dragon tail', 21, 'dragon', 0),
('cross chop', 21, 'fighting', 0),
('payback', 21, 'dark', 0),
('giga impact', 24, 'normal', 0),
('dual chop', 21, 'dragon', 0),
('crunch', 21, 'dark', 0),
('dragon pulse', 21, 'dragon', 0),
('furry cutter', 21, 'bug', 0),
('bullet punch', 15, 'steel', 1),
('vacuum wave', 15, 'fighting', 1),
('night slash', 21, 'dark', 0),
('body slam', 24, 'normal', 0),
('surf', 21, 'water', 0),
('dragon rage', 21, 'dragon', 0),
('aqua jet', 15, 'water', 1),
('wing attack', 21, 'flying', 0),
('fire punch', 21, 'fire', 0),
('aurora beam', 21, 'ice', 0),
('megahorn', 21, 'bug', 0),
('drill run', 21, 'ground', 0);




















SELECT * FROM pokemon;
SELECT * FROM pokemon_moves;
