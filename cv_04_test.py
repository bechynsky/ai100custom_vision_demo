from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient

from msrest.authentication import ApiKeyCredentials
from cv_00_credentials import ENDPOINT
from cv_00_credentials import training_key
from cv_00_credentials import prediction_key
from cv_00_credentials import prediction_resource_id

credentials_training = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials_training)

# It is just demo, we use first project in Custom Vison resource
project = trainer.get_projects()[0]
print('Project: ' + project.name)

# It is just demo, we use first iteration in Custom Vison resource
iteration = trainer.get_iterations(project.id)[0]
print('Iteration: ' + iteration.name)


credentials_prediction = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, credentials_prediction)

image_urls = ['https://upload.wikimedia.org/wikipedia/commons/5/57/WoodPecker_Pivert_in_59650_%282%29.JPG', \
'https://upload.wikimedia.org/wikipedia/commons/0/01/Un_passerotto_su_un_olivo_nella_primavera_2020_Uccellino.jpg', \
'https://upload.wikimedia.org/wikipedia/commons/b/b2/Pica_1450098_Nevit.jpg', \
'https://upload.wikimedia.org/wikipedia/commons/4/43/Kohlmeise_%2823%29_%2834632808830%29.jpg', \
'https://upload.wikimedia.org/wikipedia/commons/4/42/Merel_%28Turdus_merula%29.jpg']

for image_url in image_urls:
    results = predictor.classify_image_url(project.id, iteration.name, url=image_url)
    print(image_url)
    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))
    
    print()

