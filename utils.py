import csv
import requests
import os

def _download_image(url, save_path):
    """ Download one image from URL and save it to a file 
    parameters:
    - url: str, URL of the image
    - save_path: str, path to save the image file
    """
    try:
        response = requests.get(url)
        # check if the request was successful
        response.raise_for_status()
        
        # write the image content to a file
        with open(save_path, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")

def download_images_from_csv(csv_file_path, folder='images', max_images=200):
    """ Download images from URLs in a CSV file 
    parameters:
    - csv_file_path: str, path to the CSV file containing image URLs
    - folder: str, path to the folder where images will be saved
    - max_images: int, maximum number of images to download
    """

    # create folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    with open(csv_file_path, newline='') as csvfile:
        # read the csv file with each row as a dictionary
        reader = csv.DictReader(csvfile)
        count = 0

        for row in reader:
            if count >= max_images:
                break

            url = row['image_url'] 
            image_name = url.split('/')[-1]
            save_path = os.path.join(folder, image_name)

            # download the image from URL
            _download_image(url, save_path)
            print(f"Downloaded {image_name} from {url}")

            count += 1

# replace the path with the actual path to the CSV file
csv_file_path = '/Users/gongjingyi/Desktop/Later/clip-model-codes/data/NewDataset.csv'  
download_images_from_csv(csv_file_path, max_images=200)