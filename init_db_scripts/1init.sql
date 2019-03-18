CREATE TYPE status AS ENUM (
  'open', 'in progress', 'review', 'test', 'closed'
);

CREATE TABLE "User" (
  id serial PRIMARY KEY,
  name varchar(100) not null,
  email varchar(150) not null,
  password varchar(50) not null,
  UNIQUE (email),
  CONSTRAINT valid_user CHECK (
    name <> '' and email <> '' and password <> ''
  )
);

CREATE TABLE Ticket (
  id serial PRIMARY KEY,
  title varchar(300) not null,
  description character varying,
  date_of_creation timestamp not null,
  creator_id integer REFERENCES "User" not null,
  assignee integer REFERENCES "User",
  status status default 'open',
  CONSTRAINT valid_ticket CHECK (
    title <> ''
  )
);
