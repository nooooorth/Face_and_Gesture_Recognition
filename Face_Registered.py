import cv2

camera = cv2.VideoCapture(0)
import cv2

cap = cv2.VideoCapture(0)#打开摄像头
# 人脸识别分类器
faceCascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

face_id= str(input("你的编号:"))
path="./FR_dir"# 储存路径
count = 0
ObjectNum = count+10# 目标储存个数
while(True):
    ret, frame = cap.read()#获得图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#转化为灰度图

    faces = faceCascade.detectMultiScale(  # 人脸检测
        gray,#灰度图，使用灰度图会提高效率
        scaleFactor=1.05,#图片缩小的值
        minNeighbors=20,#判断次数
        minSize=(16, 16)#人脸最小尺寸
    )

    for (x, y, w, h) in faces:#faces中时一个图片中所有识别出来的人脸，有可能时多个
        #画脸的方框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)#图像源，原点，终点，线的颜色，粗细
        count+=1#个数加一
        fac_gray = gray[y: (y + h), x: (x + w)]#获取脸部图片
        cv2.imwrite(path+'/' + str(face_id) + '_' + str(count) + '.jpg', fac_gray) # 保存图像
        break #只取一个，取完就退。


    cv2.imshow('Frame', frame)#显示
    k = cv2.waitKey(1) #设置视频刷新频率，单位为毫秒，返回值为键盘按键的值
    if k == 27:#如果摁下esc键则退出
        break
    elif count>=ObjectNum:#收集的数量足够则退出
        break

cap.release()#关闭摄像头
cv2.destroyAllWindows()#销毁全部窗体