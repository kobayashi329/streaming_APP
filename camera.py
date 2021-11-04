import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)#カメラを指定
    def __del__(self):
        self.video.release()#カメラを解放

    def get_frame(self):
        success, image = self.video.read()#readはに変数を返す。(success,image)に分けて格納
        ret, jpeg = cv2.imencode('.jpg', image)#imencodeは二変数を返す.(ret,jpeg)に分けて格納
        return jpeg.tobytes()#numpyをbytes型に変換し返す.