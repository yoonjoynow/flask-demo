import json

from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename


def create_api(app, poie_service):
    # 파일 업로드 처리
    @app.route('/api/poie', methods=['POST'])
    def analysis():
        file = request.files["file"]

        print("전달받은 파일 : " + str(file))

        poie_service.analysis_audio

        result = poie_service.analysis_audio(file)
        # # 저장할 경로 + 파일명
        # file.save(secure_filename(file.filename))
        # print("저장된 파일 명 : " + file.filename)
        #
        # a = request.content_type
        # print(a)

        # return jsonify({"filename": file.filename})
        print("결과 : " + str(result))
        return jsonify(result)