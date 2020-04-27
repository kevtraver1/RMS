CREATE DATABASE rms;
use rms;

CREATE TABLE affiliate (
  name VARCHAR(20),
  id VARCHAR(10)
);

INSERT INTO affiliate
  (name, id)
VALUES
  ('Comcast', '1'),
  ('Test', '0'),
  ('Kevin', '2');