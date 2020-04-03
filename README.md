# RumexClassification

[LabelImg](https://github.com/tzutalin/labelImg) was used to label all images.

~1 minute of video ≈ 1 hour of annotating.~

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



# Training the rumex model

## For detailed steps to install Object Detection API, follow the 

[Tensorflow installationinstructions](https://github.com/chandyalex/RumexClassification/blob/master/installation.md)

After installing the object detection API 

1. Convet xml to csv using `xml_to_csv.py` - It will create csv file contains all annoatations, make sure that the directory names annotations present in the same directory.
2. Run `"jupyter-notebook"` select split `labels.ipynb` and run, it will return the train and test csv files.
3. Now we need to create tf record by nunning generate_tfrecord.py 

```python generate_tfrecord.py --csv_input=directory\train_labels.csv --image_dir=image_directory --output_path=train.record```

```python generate_tfrecord.py --csv_input=directory\test_labels.csv --image_dir=image_directory --output_path=test.record```


4. make sure that `"object-detection.pbtxt"` in training_config

 looks like this

```
item {
  id: 1
  name: 'rumex'
}
```

5. Now we need to create a training configuration file. , `ssd_mobilenet_v1_pets.config` , which can be found in the "`training_config`" folder.

6. Changes to be made in config file:

 fine_tune_checkpoint: `directory/base_model/model.ckpt`

 `input_path: "directory/train.record" line 123`

 label_map_path: "directory/training_config/object-detection.pbtxt"

 input_path: "directory/test.record" line 135

 label_map_path: `"directory/training_config/object-detection.pbtxt"`


7. Training model

`python train.py --logtostderr --model_dir=training_output/ --pipeline_config_path=training_config/ssd_mobilenet_v1_pets.config`

8. Export model

````python export_inference_graph.py --input_type image_tensor --pipeline_config_path raining_config/ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix training_output/model.ckpt-XXXX --output_directory final_model````

9. Running iference `python inference.py`


