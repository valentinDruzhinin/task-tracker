INSERT INTO "User"(name, email, "password")
  VALUES ('Ivan', 'ivan@test.com', 'ivantestpassword');
INSERT INTO "User"(name, email, "password")
  VALUES ('Igor', 'igor@test.com', 'igortestpassword');
INSERT INTO "User"(name, email, "password")
  VALUES ('Ben', 'ben@test.com', 'bentestpassword');

INSERT INTO ticket(title, description, date_of_creation, creator_id)
  VALUES ('Ticket1', 'First ticket', now(), 1);
INSERT INTO ticket(title, description, date_of_creation, creator_id)
  VALUES ('Ticket2', 'Second ticket', now(), 2);
INSERT INTO ticket(title, description, date_of_creation, creator_id)
  VALUES ('Ticket3', 'Third ticket', now(), 3);
INSERT INTO ticket(title, description, date_of_creation, creator_id)
  VALUES ('Ticket4', 'Fourth ticket', now(), 1);