"""
# -*- coding: utf-8 -*-
# python 3.7
"""
# 导入相关包
import face_recognition  # 人脸识别基础包
import cv2  # OpenCV调用摄像头，进行图像处理
import datetime  # 时间
import glob2 as gb  # 文件处理


def face_recognition_module():
    video_capture = cv2.VideoCapture(0)  # 调用摄像头
    img_path = gb.glob(r'E:\Pycharm\Python_Project\Dlib_FaceRecTime\photo\\*.jpg')  # 加载图库路径
    known_face_names = []
    known_face_encodings = []

    # 图库图片处理
    for i in img_path:
        picture_name = i.replace('E:\Pycharm\Python_Project\Dlib_FaceRecTime\photo\\*.jpg', '')  # 处理文件路径名称
        picture_newname = picture_name.replace('.jpg', '')
        someone_img = face_recognition.load_image_file(i)
        someone_face_encoding = face_recognition.face_encodings(someone_img)[0]  # 获取图片中人脸编码
        known_face_names.append(picture_newname)  # 将处理得到的人名添加到人名列表中
        known_face_encodings.append(someone_face_encoding)  # 将人脸编码添加到编码列表中
        someone_img = []
        someone_face_encoding = []
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    # 人脸检测模块
    camera_test, test_frame = video_capture.read()  # 测试是否能获取到摄像头帧
    if camera_test:
        print('Camera Open Success!')
        print('开始时间：' + str(datetime.datetime.now()))
        # 人脸检测循环
        while True:
            ret, frame = video_capture.read()  # 加载摄像头
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.3)  # 缩小图像提高性能
            rgb_small_frame = small_frame[:, :, ::-1]  # 将BGR格式转换为RGB格式
            # 判断循环
            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)  # 定位人脸
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)  # 获取定位人脸处的人脸编码
                face_names = []
                # 跟图像库中的人脸编码对比
                for i in face_encodings:
                    match = face_recognition.compare_faces(known_face_encodings, i,
                                                           tolerance=0.4)  # 阈值0.4，compare返回判断结果
                    # 识别成功处理
                    if True in match:
                        match_index = match.index(True)
                        name = "match"
                        # To print name and time
                        cute_clock = datetime.datetime.now()
                        print(known_face_names[match_index] + ':' + str(cute_clock))
                    else:
                        name = "unknown"
                    face_names.append(name)

            process_this_frame = not process_this_frame
            # 为人脸加框并显示match
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            # OpenCV显示摄像头实时图像
            cv2.imshow('Video', frame)
            # 等待退出
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # 结束后处理
        print('结束时间：' + str(datetime.datetime.now()))
        # 设标志位，后续返回
        return 123
        video_capture.release()
        cv2.destroyAllWindows()
    else:
        print('Camera Open Failure!')
        exit(-1)


if __name__ == '__main__':
    print('Waiting...')
    a = face_recognition_module()
    print(a)
    print('over!')