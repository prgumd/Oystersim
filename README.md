# Underwater-Robotics
Development of underwater rover simulator that can be used to detect oysters for this [project](https://isr.umd.edu/news/story/using-underwater-robots-to-detect-and-count-oysters). IMU and SONAR sensors are simulated mounted onto the rover. The simulator can be initialized with random landscapes, water turbidity, and with any underwater object randomly scattered in clusters. A custom rover path can be provided by user, which the rover will use to collect data and count oysters from and build the oyster map.

### Generated underwater Scene
<p align="center">
<img src="https://github.com/niteshjha08/Underwater-Robotics/blob/main/media/render.png"/>
</p>

### Camera, IMU and SONAR sensors integration
<p align="center">
<img src="https://github.com/niteshjha08/Underwater-Robotics/blob/main/media/simulator-sensors.gif"/>
</p>

### Segmentation for oyster detection
https://user-images.githubusercontent.com/51222320/160022136-1d19570c-cf9c-4df5-988a-3882d69b64cf.mp4

### Visual SLAM
https://user-images.githubusercontent.com/51222320/160022185-2de0b217-801e-40d9-bf05-2156adf3aecf.mp4

### Oyster Map Generation using SLAM and segmentation output

<p align="center">
<img src="https://github.com/niteshjha08/Underwater-Robotics/blob/main/media/oyster_map.gif"/>
</p>





## Tasks
- [x] 2D bounding Box of objects from Blender `2.93`
- [x] Integrate IMU with blender
- [x] Integrate LiDAR/SONAR with blender
- [x] Train yolo on the generated data from blender
- [ ] Rover position data with detections on PCL

## Google Colab Notebook
* colab notebook used to train the yolov4-tiny, find it [here](https://colab.research.google.com/drive/1RePfSTb7c1tPAuh_D-ySLhrG78gxkF9D?usp=sharing)
* Modified the colab notebook provided [here](https://colab.research.google.com/drive/1_GdoqCJWXsChrOiY8sZMr_zbr_fH-0Fg)

## Models
* We trained a yoloV4-tiny on a dataset of around 5000 images
* Download the model best weights file from [here](https://drive.google.com/file/d/1ffx9uFeBLUgfymSTHV5pO_OoLnYB7EVT/view?usp=sharing) 
* Copy the model weights in [here](https://github.com/mjoshi07/Underwater-Robotics/tree/main/data/model)

## Blender model
* BlueROV model downlaod from [here](https://github.com/patrickelectric/bluerov_ros_playground)
* Oysters model download from [here](https://drive.google.com/drive/folders/1XY2yMnFDCiSR8H6S84OS8WX1tzu2OnCW?usp=sharing)  
