drop database if exists pypo;
create database pypo;
use pypo;
CREATE TABLE Usuario 
( 
 senha VARCHAR(25) NOT NULL,  
 idUsuario INT PRIMARY KEY AUTO_INCREMENT,  
 email VARCHAR(45) NOT NULL,  
 nickname VARCHAR(25) NOT NULL,  
 UNIQUE (nickname)
); 

CREATE TABLE Item 
( 
 idItem INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(25) NOT NULL,  
 valor INT NOT NULL 
); 

CREATE TABLE Exercicio 
( 
 titulo VARCHAR(25) NOT NULL,  
 Enunciado VARCHAR(999) NOT NULL,  
 alternativas VARCHAR(999) NOT NULL,  
 resposta CHAR(1) NOT NULL,  
 idExercicio INT PRIMARY KEY AUTO_INCREMENT,  
 numero INT,  
 UNIQUE (titulo,Enunciado)
); 

CREATE TABLE Fase 
( 
 idFase INT PRIMARY KEY AUTO_INCREMENT,  
 MaterialApoio VARCHAR(999) NOT NULL,  
 idExercicio INT,
FOREIGN KEY(idExercicio) REFERENCES Exercicio(idExercicio)
); 

CREATE TABLE Modulo 
( 
 idModulo INT PRIMARY KEY AUTO_INCREMENT,  
 numero INT NOT NULL,  
 nome VARCHAR(25) NOT NULL UNIQUE,  
 idFase INT,
 FOREIGN KEY(idFase) REFERENCES Fase(idFase)
); 


CREATE TABLE Mundo 
( 
 idMundo INT PRIMARY KEY AUTO_INCREMENT,  
 linguagem VARCHAR(8) NOT NULL UNIQUE,  
 idModulo INT,  
 FOREIGN KEY(idModulo) REFERENCES Modulo(idModulo)
); 



CREATE TABLE Estoque 
( 
 qtd INT NOT NULL,  
 idUsuario INT,  
 idItem INT, 
 PRIMARY KEY(idUsuario, idItem),
 FOREIGN KEY(idUsuario) REFERENCES Usuario(idUsuario),
 FOREIGN KEY(idItem) REFERENCES Item(idItem)
); 

CREATE TABLE Progresso 
( 
 idUsuario INT,  
 idFase INT,
 PRIMARY KEY(idUsuario, idFase),
 FOREIGN KEY(idUsuario) REFERENCES Usuario(idUsuario),
 FOREIGN KEY(idFase) REFERENCES Fase(idFase)
); 
