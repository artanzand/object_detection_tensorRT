# Real-time Object Detection with TensorRT
This is an implementation of real-time object detection with TensorRT. The architecutre used for the object detection inference is MobileNet-v2. This inference script is designed for use on NVIDIA Jetson Nano and requires access to a USB camera. If such a camera is not available, the phrase `"display://0"` in the Display loop of `object_detection.py` can be replaced by an absolute path to the video to allow for object detection on the video file.

# Usage
An NVIDIA Jetson product is required to do real-time object detection with the `object_detection.py` script. It is assumed that the latest version of JetPack-L4T has been installed on your Jetson. If not, please follow the instructions [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#write) to set up your Jetson nano.  

## Docker Image
To download the pretraind model and required Python packages, the below docker image can be created from which the `object_detection.py` can be executed. See the "Running the Script" section for details.

```
$ git clone --recursive https://github.com/dusty-nv/jetson-inference
$ cd jetson-inference
$ docker/run.sh
```

## Running the Script
Clone this repository and run the below script by replacing the repo path and desired container path. 
```$ docker/run.sh --volume /my/host/path:/my/container/path    # these should be absolute paths```

Run the below command from within the container image for real-time object detection.
```python src/object_detection.py```


# Example
As observed in the below example, the pretrained MobileNet-v2 does a good job of drawing a bounding box on the detected objects (the 91 object classes that it is trained on). Also included in the real-time annotation is model's confidence in the detected object.
<p align="center">
  <img src="https://github.com/artanzand/object_detection_tensorRT/blob/main/examples/mouse_keyboard_person.png" />
</p>

# Credits
Hello AI World - Jetson Nano [repository](https://github.com/artanzand/jetson-inference)
