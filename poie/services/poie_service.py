import json

import numpy as np


class PoieService:

    def __init__(self, poie_dao, convertor, model):
        self.poie_dao = poie_dao
        self.convertor = convertor
        self.model = model

    def analysis_audio(self, wave_file):
        # self.poie_dao.save(wave_file)
        target = self.convertor.convert(wave_file)

        try:
            print("분석 시작 ==> " + str(target.shape))
            prediction = self.model.predict(target)
            print("result ===> " + str(prediction))
            print("result ===> " + str(prediction.shape))
            print("분석 끝")

            id = 2,
            sound_name = 'dog'

            result = {
                "id": id,
                "sound_name": sound_name
            }

            # return json.dumps(result)
            return result

        except Exception as e:
            print("오류 발생 : " + str(e))
