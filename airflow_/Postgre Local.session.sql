create table animal(
    category varchar(10),
    alt varchar(1000) null,
    srcset varchar(1000) null,
    img_path varchar(1000) null,
    img_width smallint null,
    img_height smallint null,
    label varchar(20),
    time Time null
);
update animal
set label = '';