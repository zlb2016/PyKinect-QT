import numpy as np
import cv2
import pickle
import time 
import datetime
import glob as gb
import os

from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime

class capture_self:
    def trans_video(self,image_path,video_name,fps,res,type):
        img_path = gb.glob(image_path+"/*.png")
        videoWriter = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), fps, res)
        for path in img_path:
            img = cv2.imread(path)
            img = cv2.resize(img, res)
            videoWriter.write(img)
        print('transform '+type+' video done!')

    def remove(self, path):
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith(".png"):  # 填写规则
                    os.remove(os.path.join(root, name))
                    print("Delete File: " + os.path.join(root, name))

    def save_frames(self, image_num ):
        #records and saves colour and depth frames from the Kinect

        print("Saving colour and depth frames")

        #initialise kinect recording, and some time variables for tracking the framerate of the recordings
        kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Depth)
        starttime = time.time()
        oldtime = 0
        i = 0
        fpsmax = 0
        fpsmin = 100

        # Actual recording loop, exit by pressing escape to close the pop-up window
        while True:

            if kinect.has_new_depth_frame() and kinect.has_new_color_frame() :
                elapsedtime = time.time() - starttime
                if(elapsedtime> i/10):

                    #Only for high i try evalutaing FPS or else you get some divide by 0 errors
                    if i >10:
                        try:
                            fps =  1/(elapsedtime - oldtime)
                            print(fps)
                            if fps> fpsmax:
                                fpsmax= fps
                            if fps < fpsmin:
                                fpsmin = fps

                        except ZeroDivisionError:
                            print("Divide by zero error")
                            pass

                    oldtime = elapsedtime

                    #read kinect colour and depth data (somehow the two formats below differ, think one is and one isnt ctypes)
                    depthframe = kinect.get_last_depth_frame() #data for display
                    depthframeD = kinect._depth_frame_data
                    colourframe = kinect.get_last_color_frame()
                    colourframeD = kinect._color_frame_data


                    #reformat the other depth frame format for it to be displayed on screen
                    depthframe = depthframe.astype(np.uint8)
                    depthframe = np.reshape(depthframe, (424, 512))
                    depthframe = cv2.cvtColor(depthframe, cv2.COLOR_GRAY2RGB)

                    #Reslice to remove every 4th colour value, which is superfluous
                    colourframe = np.reshape(colourframe, (2073600, 4))
                    colourframe = colourframe[:,0:3]

                    #extract then combine the RBG data
                    colourframeR = colourframe[:,0]
                    colourframeR = np.reshape(colourframeR, (1080, 1920))
                    colourframeG = colourframe[:,1]
                    colourframeG = np.reshape(colourframeG, (1080, 1920))
                    colourframeB = colourframe[:,2]
                    colourframeB = np.reshape(colourframeB, (1080, 1920))
                    framefullcolour = cv2.merge([colourframeR, colourframeG, colourframeB])

                    # if display_type == "COLOUR":

                    #Show colour frames as they are recorded
                    # cv2.imshow('Recording KINECT Video Stream', framefullcolour)
                    cv2.imwrite('./image/color/colorimage-' + str(i) + '.png', framefullcolour)  # save images


                    # if display_type == "DEPTH":
                    #show depth frames as they are recorded
                    # cv2.imshow('Recording KINECT Video Stream', depthframe)
                    cv2.imwrite('./image/depth/depthimage-'+str(i)+'.png', depthframe)#save images
                    i = i+1

            #end recording if the escape key (key 27) is pressed
            key = cv2.waitKey(1)
            key=i
            if key == int(image_num): break
        cv2.destroyAllWindows()
        return 1

    def save_video(self):#存储视频
        currentdate = datetime.datetime.now()
        file_name = str(currentdate.day) + "." + str(currentdate.month) + "." + str(currentdate.hour) + "." + str(
            currentdate.minute)
        color_path='./image/color'
        depth_path = 'image/depth'
        self.trans_video(color_path,color_path+'/color-' + file_name + '.avi', 30, (1920, 1080), 'color')
        self.trans_video(depth_path, depth_path+'/depth-' + file_name + '.avi', 10, (512, 424), 'depth')
        self.remove(color_path)
        self.remove(depth_path)
        return file_name


# if __name__ == "__main__":
#     currentdate = datetime.datetime.now()
#     file_name = str(currentdate.day) + "." + str(currentdate.month) + "."+ str(currentdate.hour) + "."+ str(currentdate.minute)
#     display_type="COLOUR"
#     #Save colour and depth frames
#     save_frames(file_name,display_type)