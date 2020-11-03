import time

# Custom Vision modules
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials


from cv_00_credentials import ENDPOINT
from cv_00_credentials import training_key
from cv_00_credentials import prediction_resource_id

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

project = trainer.get_projects()[0]

print('Project ' + project.name + ' loaded.')

iteration = trainer.get_iterations(project.id)[0]

print(iteration)

trainer.publish_iteration(project.id, iteration.id, iteration.name, prediction_resource_id)

