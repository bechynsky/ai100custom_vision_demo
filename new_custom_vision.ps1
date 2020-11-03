$location = "westeurope"
$rg_name = "CustomVisionDemo" + (Get-Random -Minimum 10000 -Maximum 99999)

$cv_name_training = "CustomVisionTraining" + (Get-Random -Minimum 10000 -Maximum 99999)
$cv_name_prediction = "CustomVisionPrediction" + (Get-Random -Minimum 10000 -Maximum 99999)

$rg = New-AzResourceGroup -Name $rg_name -Location $location
$rg

# https://docs.microsoft.com/en-us/powershell/module/az.cognitiveservices/new-azcognitiveservicesaccount?view=azps-4.8.0
$cv_training = New-AzCognitiveServicesAccount -Name $cv_name_training -ResourceGroupName $rg.ResourceGroupName -Location $location -SkuName S0 -Type CustomVision.Training -Force
$cv_prediction = New-AzCognitiveServicesAccount -Name $cv_name_prediction -ResourceGroupName $rg.ResourceGroupName -Location $location -SkuName S0 -Type CustomVision.Prediction -Force

$cv_training
$cv_prediction


$keys_training = Get-AzCognitiveServicesAccountKey -Name $cv_name_training -ResourceGroupName $rg.ResourceGroupName
$keys_prediction = Get-AzCognitiveServicesAccountKey -Name $cv_name_prediction -ResourceGroupName $rg.ResourceGroupName

$keys_training
$keys_prediction

# Put inforamation to temporary environment variable
# This information is lost after session is closed
$Env:CV_RESOURCE_GROUP = $rg_name
$Env:CV_ENDPOINT = $cv_training.Endpoint
$Env:CV_TRAINING_KEY = $keys_training.Key1
$Env:CV_PREDICTION_KEY = $keys_prediction.Key1
$Env:CV_PREDICTION_RESOURCE_ID = $cv_prediction.Id

Get-ChildItem env:* | Where-Object {$_.Name -like 'CV_*'} | Select-Object -Property Name, Value | Format-Table