# farmos odoo
Personal settings installing farmos
I am using odoo traefik 
.env must be created and populated

comprobar que el usuario esté en el grupo sudo

crear red, contenedor de traefik, traefik.yml y docker-compose.yml
contenedor de odoo y su  docker-compose.yml con volumenes persistentes, crear usuario y grupo odoo darles privilegios
   tambien hay que crear el odoo.conf y las carpetas 
contenedor de farmos con volumenes persistentes con usuario y grupo. chequear permisos, en la creacion de la databse en vez de localhost se conecta es a db que es nombre del contenedor


