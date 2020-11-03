# Import the os module, for the os.walk function
import os

# Custom Vision modules
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials

from cv_00_credentials import ENDPOINT
from cv_00_credentials import training_key


publish_iteration_name = "classifyModel"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Create a new project
print ("Creating project...")
project = trainer.create_project("Garden Birds")


# Make tags in the new project
# Set the directory you want to start from
image_folder = os.getenv("HOME") + '/birds'
os.chdir(image_folder)
# Tag = Directory name
tags = [name for name in os.listdir('.') if os.path.isdir(name)]
print(tags)

def createTag(tag):
    result = trainer.create_tag(project.id, tag)
    print('{tag} create with id: {result}')
    return result.id

def createImageList(tag, tag_id):
    # Set directory to current tag
    base_image_url = image_folder + "/" + tag + "/"
    photo_name_list = os.listdir(base_image_url)
    image_list = []
    for file_name in photo_name_list[0:49]:
        with open(base_image_url+file_name, "rb") as image_contents:
            image_list.append(ImageFileCreateEntry(name=base_image_url+file_name, contents=image_contents.read(), tag_ids=[tag_id]))
    return image_list

def uploadImageList(image_list):
    upload_result = trainer.create_images_from_files(project.id, images=image_list)
    if not upload_result.is_batch_successful:
        print("Image batch upload failed.")
        for image in upload_result.images:
            print("Image status: ", image.status)
        exit(-1)

for tag in tags:
    tag_id = createTag(tag)
    print("tag creation done with tag id {tag_id}")

    # Set directory to current tag
    base_image_url = image_folder + "/" + tag + "/"
    photo_name_list = os.listdir(base_image_url)
    
    for file_name in photo_name_list[0:21]:
        print(file_name)
        with open(base_image_url+file_name, "rb") as image_contents:
            trainer.create_images_from_data(project.id, image_contents.read(), tag_ids=[tag_id])
        
print('Project ID: ' + project.id)