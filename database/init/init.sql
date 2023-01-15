CREATE TABLE IF NOT EXISTS savepaint_img_data (
    id SERIAL PRIMARY KEY,
    timestamp timestamp,
    category varchar(100),
    label varchar(100),
    img_height int,
    img_width int,
    original_fn varchar(100),
    processed_fn varchar(100),
    processed boolean
);