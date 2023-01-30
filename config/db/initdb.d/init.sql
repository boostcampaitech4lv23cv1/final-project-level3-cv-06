CREATE TABLE IF NOT EXISTS animal(
    "id" SERIAL PRIMARY KEY,
    "created_time" varchar(20),
    "tag" varchar(300),
    "label" varchar(100),
    "img_height" integer,
    "img_width" integer,
    "img_path" varchar(100) NOT NULL,
    "correct_cnt" integer DEFAULT 0,
    "incorrect_cnt" integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS celebrity(
    id SERIAL PRIMARY KEY,
    created_time varchar(20),
    label varchar(100),
    img_height integer,
    img_width integer,
    img_path varchar(100) NOT NULL,
    correct_cnt integer DEFAULT 0,
    incorrect_cnt integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS landmark(
    id SERIAL PRIMARY KEY,
    created_time varchar(20),
    label varchar(100),
    img_height integer,
    img_width integer,
    img_path varchar(100) NOT NULL,
    correct_cnt integer DEFAULT 0,
    incorrect_cnt integer DEFAULT 0
);