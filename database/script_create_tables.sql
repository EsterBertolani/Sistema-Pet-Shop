-- Active: 1764975893585@@127.0.0.1@3306@sistema_petshop
CREATE DATABASE sistema_petshop;
USE sistema_petshop;

-- Especie 
CREATE TABLE ESPECIE (
    id_especie INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

-- Pessoa
CREATE TABLE PESSOA (
    id_pessoa INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    telefone VARCHAR(18) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Produto
CREATE TABLE PRODUTO (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INT DEFAULT 1
);

-- Animal 
CREATE TABLE ANIMAL (
    id_animal INT AUTO_INCREMENT PRIMARY KEY,
    id_especie INT NOT NULL,
    Foreign Key (id_especie) REFERENCES ESPECIE(id_especie)
    nome VARCHAR(50) NOT NULL,
    idade TINYINT NOT NULL,
    sexo CHARACTER NOT NULL,
    raca VARCHAR(50) NULL,
    cor VARCHAR(50) NOT NULL,
    porte VARCHAR(50) NOT NULL,
    castrado BOOLEAN NOT NULL,
    vacinado BOOLEAN NOT NULL,
    adotado BOOLEAN DEFAULT FALSE,
);

-- Adocao
CREATE TABLE ADOCAO (
    id_adocao INT AUTO_INCREMENT PRIMARY KEY,
    data_adocao DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_animal INT NOT NULL UNIQUE,
    id_pessoa INT NOT NULL,
    Foreign Key (id_animal) REFERENCES ANIMAL(id_animal),
    Foreign Key (id_pessoa) REFERENCES PESSOA(id_pessoa)
);

-- Venda
CREATE TABLE VENDA (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
    valor_total DECIMAL(10, 2) DEFAULT 0,
    id_pessoa INT,
    Foreign Key (id_pessoa) REFERENCES PESSOA(id_pessoa)
);

-- ItemVenda
CREATE TABLE ITEM_VENDA (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    qtd INT NOT NULL,
    preco_unit DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    id_produto INT NOT NULL,
    id_venda INT NOT NULL,
    Foreign Key (id_produto) REFERENCES PRODUTO(id_produto),
    Foreign Key (id_venda) REFERENCES VENDA(id_venda)
);