from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from poie.model.poie_repository import PoieDao
from poie.services.poie_service import PoieService
from poie.api.poie_controller import create_api
from keras.models import load_model
from poie.services.mfcc_service import AudioConvertor

def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile("config.py")

    database = create_engine('mysql+pymysql://root:1111@127.0.0.1:3306/flask?charset=utf8', max_overflow=0, echo=True)
    Session = sessionmaker(bind=database)
    session = Session()

    model_path = "/Users/yoon/Downloads/0527VGG16-48-100-32(9596).h5"
    model = load_model(model_path)
    # model.summary()


    poie_dao = PoieDao(database, session)

    convertor = AudioConvertor()
    poie_service = PoieService(poie_dao, convertor, model)
    create_api(app, poie_service)

    return app
