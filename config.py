from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'thecolorblue970710'
app.config['MYSQL_DATABASE_DB'] = 'ILikeTurtles'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
