INSERT INTO ESPECIE (nome) VALUES
('Gato'),
('Cachorro'),
('Coelho'),
('Calopsita');

INSERT INTO PESSOA (nome, cpf, telefone, email) VALUES
('Ester', '187.108.017-74', '(27) 99296-7315', 'estersb@gmail.com'),
('Vandin', '123.321.231-11', '(27) 99715-6574', 'vandinAlvrs@gmail.com');

INSERT INTO PRODUTO (nome, descricao, preco, estoque) VALUES
('Ração Premium 10kg', 'Ração sabor frango para adultos', 150.00, 20),
('Brinquedo Osso', 'Osso de borracha resistente', 25.50, 50),
('Shampoo Pet', 'Shampoo neutro para cães e gatos', 35.00, 15),
('Arranhador Gato', 'Torre de sisal para gatos', 200.00, 5);

INSERT INTO ANIMAL (nome, idade, sexo, raca, cor, porte, castrado, vacinado, adotado, id_especie) VALUES
('Bonitinha', 4, 'F', 'Siamês', 'Marrom/Branca', 'Médio', true, false, true, 13),
('Rex', 3, 'M', 'Vira-lata', 'Marrom', 'Médio', true, true, false, 14),
('Mel', 1, 'F', 'Poodle', 'Branca', 'Pequeno', false, true, true, 14),
('Garfield', 5, 'M', 'Persa', 'Laranja', 'Grande', true, true, false, 13),
('Pernalonga', 1, 'M', 'Angorá', 'Branco', 'Pequeno', false, false, false, 15),
('Falquito', 1, 'M', 'N/A', 'Cinza', 'Pequeno', false, false, false, 16);

INSERT INTO ADOCAO (data_adocao, id_animal, id_pessoa) VALUES
('2023-10-25 10:00:00', 21, 6);

INSERT INTO VENDA (data_venda, valor_total, id_pessoa) VALUES
('2023-10-26 14:30:00', 201.00, 6); 

INSERT INTO ITEM_VENDA (qtd, preco_unit, subtotal, id_produto, id_venda) VALUES
(1, 150.00, 150.00, 12, 4),  -- 1 Ração (id 1) na Venda 1
(2, 25.50, 51.00, 11, 4);