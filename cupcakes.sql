DROP DATABASE IF EXISTS cupcakes_db;

CREATE DATABASE cupcakes_db;

\c cupcakes_db

CREATE TABLE cupcake
(
  id SERIAL PRIMARY KEY,
  flavor TEXT NOT NULL,
  size TEXT NOT NULL,
  rating FLOAT NOT NULL,
  image TEXT NOT NULL DEFAULT 'https://tinyurl.com/demo-cupcake'
);

-- ADD SOME DATA

INSERT INTO cupcake
  (flavor, size, rating, image)
VALUES
  ('chocolate', 'small', 4.2, 'https://tinyurl.com/demo-cupcake');

INSERT INTO cupcake
  (flavor, size, rating, image)
VALUES
  ('strawberry', 'medium', 4.2, 'https://www.recipegirl.com/wp-content/uploads/2017/07/Pink-Strawberry-Cupcakes.jpg');
