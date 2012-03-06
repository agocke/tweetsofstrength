CREATE TABLE IF NOT EXISTS tweets (
  id            INTEGER   PRIMARY KEY,
  text          TEXT      NOT NULL,
  user_id       INTEGER   NOT NULL,
  user_name     TEXT      NOT NULL,
  date_tweeted  TEXT      NOT NULL,
  location      TEXT      NULL
);
