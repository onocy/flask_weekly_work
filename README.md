 

# Weekly Work &middot;  [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE) 


 ### Built With 

- Flask
- Materialize CSS
- psycopg2
- SQLAlchemy (PostgreSQL)

#### Getting started 

* `pip install psycopg2`
* `pip install Flask-SQLALchemy`
* Note: You may need to update pip or a precompiled python library that you can import to your work_dir and reference  



#### Database Setup

Set the internal config of the app from a key of SQLALCHEMY_DATABASE_URI to the uri of the database on your local system. 
`app.config(['SQLALCHEMY_DATABASE_URI'] = \'postgresql://user:password@serveraddress(usually localhost)/databasename`
* Within a python instance in the working directory, run `from app.py impor db` and then run `db.create_all()` to create the table on your local instance of PostgreSQL. 


