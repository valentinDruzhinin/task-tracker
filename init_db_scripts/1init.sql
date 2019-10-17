CREATE TYPE ticketProgressStatus AS ENUM (
  'open', 'in progress', 'review', 'test', 'closed'
);

CREATE TYPE userRole AS ENUM (
  'admin', 'write', 'read'
);

CREATE TABLE Users (
  id serial PRIMARY KEY,
  name varchar(100) not null,
  email varchar(150) not null,
  password varchar not null,
  UNIQUE (email),
  CONSTRAINT valid_user CHECK (
    name <> '' and email <> '' and password <> ''
  )
);

CREATE TABLE Dashboards (
  id serial PRIMARY KEY,
  name varchar(100) not null,
  description character varying,
  date_of_creation timestamp not null,
  creator_id integer REFERENCES Users not null
);

CREATE TABLE Tickets (
  id serial PRIMARY KEY,
  title varchar(300) not null,
  description character varying,
  date_of_creation timestamp not null,
  creator_id integer REFERENCES Users not null,
  dashboard_id integer REFERENCES Dashboards not null,
  assignee integer REFERENCES Users,
  status ticketProgressStatus default 'open',
  CONSTRAINT valid_ticket CHECK (
    title <> ''
  ),
  UNIQUE (dashboard_id, creator_id)
);

CREATE TABLE DashboardToUser (
  id serial PRIMARY KEY,
  dashboard_id integer REFERENCES Dashboards not null,
  user_id integer REFERENCES Users not null,
  role userRole not null,
  UNIQUE (dashboard_id, user_id)
);
