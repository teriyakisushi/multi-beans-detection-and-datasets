import os
import cv2
import ultralytics
from ultralytics import YOLO
n=''
v=0.0
# Load local weight model best.pt
model = YOLO('best.pt')

# Predict a img from local,and obtain the classes which contained in the img
res=model.predict('any.jpg')
cls_ids=res[0].boxes.cls
cls_names=[model.names[i.item()] for i in cls_ids]
cls_var=[i.item() for i in cls_ids]
for name,var in zip(cls_names,cls_var):
    n=name
    v=var

if (v==1.0 and n=='green beans'):
    print("Green Beans~")
else :print("Other")