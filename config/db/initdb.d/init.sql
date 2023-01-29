CREATE TABLE IF NOT EXISTS animal(
    id SERIAL PRIMARY KEY,
    created_time datetime,
    tag varchar(300),
    label varchar(100),
    img_height int,
    img_width int,
    img_path varchar(100),
    correct_cnt int,
    incorrect_cnt int,
)

CREATE TABLE IF NOT EXISTS celebrity(
    id SERIAL PRIMARY KEY,
    created_time datetime,
    label varchar(100),
    img_height int,
    img_width int,
    img_path varchar(100),
    correct_cnt int,
    incorrect_cnt int,
)

CREATE TABLE IF NOT EXISTS landmark(
    id SERIAL PRIMARY KEY,
    created_time datetime,
    label varchar(100),
    img_height int,
    img_width int,
    img_path varchar(100),
    correct_cnt int,
    incorrect_cnt int,
);