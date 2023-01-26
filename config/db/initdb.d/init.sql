CREATE TABLE IF NOT EXISTS savepaint(
    id SERIAL PRIMARY KEY,
    created_time timestamp,
    category varchar(100),
    label varchar(100),
    img_height int,
    img_width int,
    img_path varchar(100),
);


