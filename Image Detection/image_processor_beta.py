import cv2

def ProcessImage():
    
    global filename
    global processing_factor
    
    OriginalImage = cv2.imread(filename,1)
    cv2.imshow("Original Image",OriginalImage)
    cv2.waitKey(0)
    
    blue_original = OriginalImage[:, :, 0]
    green_original = OriginalImage[:, :, 1]
    red_original = OriginalImage[:, :, 2]
    Disease = red_original - green_original
    
    global Processed
    #global Disease
    Processed = blue_original
    GetProcessed(OriginalImage)
    
    ProcessingFactor = processing_factor
    for i in range(0, OriginalImage.shape[0]):
        for j in range(0, OriginalImage.shape[1]):
            if int(green_original[i, j]) > ProcessingFactor:
                Disease[i, j] = 255
    cv2.imshow("Disease Image", Disease)
    cv2.waitKey(0)
    return DisplayDiseasePercentage(Disease), Disease


def GetProcessed(OriginalImage):
    global Processed
    for i in range(0, OriginalImage.shape[0]):
        for j in range(0, OriginalImage.shape[1]):
            if OriginalImage[i, j, 0] > 200 and OriginalImage[i, j, 1] > 200 and OriginalImage[i, j, 2] > 200:
                Processed[i, j] = 255
            else:
                Processed[i, j] = 0



def DisplayDiseasePercentage(Disease):
    global processing_factor
    Count = 0
    Res = 0
    for i in range(0, Disease.shape[0]):
        for j in range(0, Disease.shape[1]):
            if Processed[i, j] == 0:
                Res += 1
            if Disease[i, j] < processing_factor:
                Count += 1
    Percent = (Count / Res) * 100
    return Percent


Processed = None
processing_factor=142
# These are testing cases
#filename=r"D:\Coding Workspace\Agrover\Agrover\Image Detection\0a8a68ee-f587-4dea-beec-79d02e7d3fa4___RS_Early.B 8461.JPG"
#filename=r"D:\Coding Workspace\Agrover\Agrover\Image Detection\0b3e5032-8ae8-49ac-8157-a1cac3df01dd___RS_HL 1817.JPG"
#filename=r"D:\Coding Workspace\Agrover\Agrover\Image Detection\0a8a68ee-f587-4dea-beec-79d02e7d3fa4___RS_Early.B 8461.JPG"
#filename=r"D:\Coding Workspace\Agrover\Agrover\Image Detection\PotatoPics\Potato___Early_blight\0a6983a5-895e-4e68-9edb-88adf79211e9___RS_Early.B 9072.JPG"
#filename=r"D:\Coding Workspace\Agrover\Agrover\Image Detection\PotatoPics\Potato___healthy\0f4ebc5a-d646-436a-919d-961342997cde___RS_HL 4183.JPG"
filename="D:\Coding Workspace\Agrover\Agrover\Image Detection\download.jpg"
#filename=r"D:\Coding Workspace\Agrover\Agrover\Image Detection\fresh-green-leaf-potato-plant-260nw-449327257.jpg"
result,Disease=ProcessImage()
if result>20:
    print("Disease")
else:
    print("Normal")

cv2.imshow("Diseased",Disease)
cv2.waitKey(0)