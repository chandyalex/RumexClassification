# RumexClassification

[LabelImg](https://github.com/tzutalin/labelImg) was used to label all images.

~1 minute of video ≈ 1 hour of annotating

## Install Conda

1. Download [Anaconda Navigator](https://www.anaconda.com/distribution/)
2. Mac: Open Terminal, Windows: Open Anaconda Prompt
3. `conda create -n env_name` and replace env_name with the desired name for the environment
4. `conda activate env_name`
5. Continue on to the guide

## Guide

Install the Pandas and cv2 package by `pip install opencv-python pandas`

1. Get a video in a 1280x720 (720p / 16:9) format
2. Modify the path in the script and run the script by `python video_to_images.py`. You need to get the images in a new directory where they have no images have been labelled yet.
3. Clone LabelImg by `git clone https://github.com/tzutalin/labelImg.git` and `cd labelImg`
4. Follow their installation guide [here](https://github.com/tzutalin/labelImg#installation)
- `pip install pyqt5 lxml`
5. Run LabelImg by `python labelImg.py`
6. Open your directory with images that need tagging
7. Start drawing boundary boxes where the rumex images are by pressing W and saving by CTRL+S or CMD+S. This saves an XML file.
8. Do that for all images with rumex in them (skip the one's where there is no rumex)
9. Put all your images in the /images/ directory, and all your XML files in the /annotation/ directory
10. Run the next script `python image_files_to_dataset.py` to save your to a dataset we can use.

Done.. now go get more videos! And repeat..
