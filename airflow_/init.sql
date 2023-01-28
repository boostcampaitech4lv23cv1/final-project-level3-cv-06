create table animals(
    tag varchar(1000) null,
    img_path varchar(1000) null,
    img_width smallint null,
    img_height smallint null,
    label varchar(20),
    crawled_time Time null
);
update animals
set label = '';