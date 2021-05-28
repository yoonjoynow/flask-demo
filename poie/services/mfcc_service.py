import numpy
import skimage.io
from skimage.transform import resize
import librosa
import librosa.display
import os.path
import cv2
import numpy as np
from tensorflow.python.keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt


class AudioConvertor:

    def convert(self, wav_file):
        audio_file, sr = librosa.load(wav_file)
        mfcc_file = self.to_mfcc(audio_file, 16000, 512, 40)

        image = self.to_image(mfcc_file)

        return image

    def to_mfcc(self, audio_file, sr, hop_length, n_mfcc):
        mfcc_file = librosa.feature.mfcc(
            audio_file,
            sr=sr,
            hop_length=hop_length,
            n_fft=hop_length * 2,
            n_mfcc=n_mfcc
        )

        return mfcc_file

    def scale_minmax(self, x, min=0.0, max=255.0):
        x_std = (x - x.min()) / (x.max() - x.min())
        x_scaled = x_std * (max - min) + min

        return x_scaled

    def to_image(self, file_mfcc):
        # 8비트 범위에 맞는 최소-최대 스케일
        img = self.scale_minmax(file_mfcc, 0, 255).astype(numpy.uint8)
        img = numpy.flip(img, axis=0)  # 이미지의 저주파수
        img = 255 - img  # 반전. 검정==더 많은 에너지
        # img = resize(img, (48, 48))

        file_name = "file.png"

        save_directory = "/Users/yoon/mydata/dev/poie/image/"
        is_exist = os.path.exists(save_directory)
        if is_exist is False:
            print("존재하지않음")
            os.makedirs(save_directory)
            print(os.path.exists(save_directory))

        save_file_path = save_directory + file_name
        skimage.io.imsave(save_file_path, img)

        data = []
        image = cv2.imread(save_file_path)
        image = cv2.resize(image, (48, 48))
        image = img_to_array(image)
        image = np.array(image)

        data.append(image)
        data = np.array(data)

        return data
