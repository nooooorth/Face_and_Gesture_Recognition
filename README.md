# Face_and_Gesture_Recognition
face recognition and gesture recognition
## 项目说明
	完成基于人脸识别的身份认证的手势识别
## 人脸识别
### 运行环境 
window 10，pycharm，python 3.7
### 第三方库
face_recognition 人脸识别基础库
opencv 
datetime 
glob2 文件处理库
### 运行说明
[1] 安装运行所需的库（要安装face_recognition需要提前安装dlib以及cmake等相关库，详见https://github.com/ageitgey/face_recognition  
[2] 将想要识别的人脸图片放至目录/photo下，图片尽量保证五官清晰且仅有一人，文件命名为该人物名称  
[3] 运行主目录下的branch_face.py文件，可在控制台看到输出识别到人脸姓名以及时间  
注：match = face_recognition.compare_faces(known_face_encodings, i,tolerance=0.4） tolerance越低检测越严格，反之相反，区间[0,1]，本例使用的tolerance=0.4
## 手势识别
### testing 
## 备注
