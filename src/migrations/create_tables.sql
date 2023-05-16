drop table if exists bartenders;

CREATE TABlE IF NOT EXISTS bartenders (
  id serial PRIMARY KEY,
  name TEXT,
  hometown TEXT,
  birthyear INTEGER
);