# Real-time Object Detection with TensorRT
This is an implementation of real-time object detection with TensorRT. The architecutre used for the object detection inference is MobileNet-v2. This inference script is designed for use on NVIDIA Jetson Nano and requires access to a USB camera. If such a camera is not available, the phrase `"display://0"` in the Display loop of `object_detection.py` can be replaced by an absolute path to the video to allow for 

# Usage
To download the pretraind model and required Python packages, the below docker image can be created from which the 
## Docker Image

## Cloning the Repo

Run the below script from the base of github repository for real-time object detection.
```python src/object_detection.py```


# Example
<p align="center">
  <img src="https://github.com/artanzand/object_detection_tensorRT/blob/main/examples/Screenshot%20from%202022-03-25%2020-31-26.png" />
</p>

# Credits
Hello AI World - Jetson Nano [repository](https://github.com/artanzand/jetson-inference)
