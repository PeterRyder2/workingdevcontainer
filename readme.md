##### Description 

This is working docker application using dev conatainer extensions
this has a mysql db container and app contanier



#### TO START

- run the make_env.py file and follow directions to get the db name and password

- if using vscode you can use dev container extension to run the container (https://code.visualstudio.com/docs/devcontainers/tutorial)


### ALembic database migrations
    for mysql migrations you can use alembic
    tutorial here https://simplyprashant.medium.com/how-to-use-alembic-for-your-database-migrations-d3e93cacf9e8
   

    - make sure env.py is setup correctly and the env.py
    '''
    db_password = os.environ.get("MYSQL_ROOT_PASSWORD")
    db_nanme = os.environ.get("MYSQL_DB_NAME")
    SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://root:{db_password}@db/{db_nanme}"
    config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
    '''



#### Helpful mysql tips
- bash into mysql container
-   mysql -uroot -p 
- show databases;
- ensure the database is there
- use db_name;
- show tables; # shows the tables within the DB
- DESCRIBE TableName # shows the schema structure of a particular table