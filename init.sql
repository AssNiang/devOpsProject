CREATE TABLE public.persons(
    id int PRIMARY KEY,
    username varchar(255), 
    email varchar(255), 
    firstName varchar(255), 
    lastName varchar(255)
);


INSERT INTO public.persons(
   id, username, email, firstName, lastName
   ) VALUES 
   (1,'sadio','sa@sa.sn','sadio', 'MANE'),
   (2,'fode','fo@fo.sn','balo','toure'),
   (3,'lahm','plam@pl.du','philippe','lahm');

