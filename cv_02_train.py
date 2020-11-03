import time

# Custom Vision modules
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials

from cv_00_credentials import ENDPOINT
from cv_00_credentials import training_key

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# It is just demo, we use first project in Custom Vison resource
project = trainer.get_projects()[0]

print('Project ' + project.name + ' loaded.')

# Start trsining, it can tace few minutes
print("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status == "Training"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print("Training status: " + iteration.status)
    time.sleep(15)

