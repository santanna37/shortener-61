
from sqlalchemy.orm import sessionmaker
import sqlite3
import os
from src.adapters.database.models.links_models import LinkModel
from sqlalchemy import create_engine
from .config.base import Base



# Criação do Banco de dados 
class CreatedDB:
    
    def __init__(self) -> None:
        self.__dir = os.path.dirname(os.path.abspath(__file__))
        self.__dbpath = os.path.join(self.__dir, "db_base.db")
        print(self.__dbpath)

    def check_and_create_database(self) -> None:
        if not os.path.exists(self.__dbpath):
            conn = sqlite3.connect(self.__dbpath)
            print(f'Banco criado -- {self.__dbpath}')
            conn.close()
        else:
            print('Banco de dados já existente')


# Motor do banco de dados
class Database:
    
    def __init__(self) ->None:
        self.__dir = os.path.dirname(os.path.abspath(__file__))
        self.__dbpath = os.path.join(self.__dir, "db_base.db")
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(f'sqlite:///{self.__dbpath}')
        return engine 

    def get_engine(self):
        return self.__engine

    def create_table(self):
        Base.metadata.create_all(self.__engine)
        print('Tabelas criadas')

    def add(self, obj):
        self.session.add(obj)
        self.session.commit()
        print('Data adicionada')

    def get(self, model_class, **filters):
        result = self.session.query(model_class).filter_by(**filters).first()
        return result     

    def __enter__(self):
        session_make = sessionmaker(bind= self.__engine)
        self.session = session_make()
        return self 

    def __exit__(self, exc_type, exec_vel, exc_tb):
        self.session.close()
