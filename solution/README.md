# POC level app to show images for each frames and Point of interests

### Instructions

- To run the application, install the requirments:

    `pip install ../requirements.txt`

- Run the app.py file:

    `python3 app.py`

### Results

The results are saved in the `spreadsheets` directory:

1. `asset_poi.csv`
        
    Contains all the images 50m near to a particular point of interests.
    
2. `video_srt_image_data.csv`
        
    Images within 35m of each frames, coordinates received from `DJI_0301.SRT`.

The KML path of the drone is saved in `kml_paths` directory by the filename `drone_path.kml`.