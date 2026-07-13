from astropy.io import fits
from PIL import Image
import numpy as np
from pathlib import Path

def create_thumbnail(file_path,thumbnail_folder='thumbnails',size=(200,200)):
    try:
        file_path=Path(file_path)
        thumbnail_dir=Path(thumbnail_folder)
        thumbnail_dir.mkdir(parents=True,exist_ok=True)
        with fits.open(file_path) as hdul:
            image_data=hdul[0].data
            image_data=np.squeeze(image_data) #np.squeeze() removes dimensions of size 1
            image_data=image_data-np.min(image_data)
            image_data=image_data/np.max(image_data)
            image_data=(image_data*255).astype(np.uint8)
            #Converts the NumPy array into a Pillow image object.
            image=Image.fromarray(image_data)
            #Resize
            image.thumbnail(size)
            #save thumbnail
            thumbnail_name=file_path.stem+'.jpg'
            thumbnail_path=thumbnail_dir/thumbnail_name
            image.save(thumbnail_path,'JPEG')
            return str(thumbnail_path)
    except Exception as e:
        print(f"An error occurred while creating thumbnail: {e}")
        return None 
