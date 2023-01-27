CREATE TABLE IF NOT EXISTS animal(
    id SERIAL PRIMARY KEY,
    created_time datetime,
    label varchar(100),
    img_height int,
    img_width int,
    img_path varchar(100),
    correct_cnt boolean,
    incorrect_cnt boolean,
);


