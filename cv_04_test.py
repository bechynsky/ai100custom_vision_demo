from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from cv_00_credentials import ENDPOINT
from cv_00_credentials import prediction_key
from cv_00_credentials import prediction_resource_id
from cv_00_credentials import project_id


# Example of default iteration name would be "Iteration1"
publish_iteration_name = "Iteration 1"


credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, credentials)

base_image_url = 'C:/Users/stbechyn/Pictures/Birds/'
with open(base_image_url + "Turdus_merula_Male/Blackbird_%2827967533735%29.jpg", "rb") as image_contents:
    results = predictor.classify_image(
        project_id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))