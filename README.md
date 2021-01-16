# IncTrend
This project is an extension from the project [stocktwits-svm-nlp](https://github.com/AMOOOMA/stocktwits-svm-nlp), which is a state-of-the-art nlp model aims to classicify the posts' sentiment from stocktwits. More detailed report and explanation is available in that repo.

IncTrend on the other hand attempts to make that model more accessible by setuping a open api endpoint that will fetch posts data and process through the pretrained model to gain predictions for a specific company using its stock identifier. For example: "/predictions/AAPL" for apple and "/predictions/GOOGL" for google.

## Usage
Send a GET request to the remote endpoint: TODO

## Project structure
In the directory, predict.py will handle the generation of all of the predictions by loading the pretrained model and etc. Whereas for the endpoint, models.py and serializers.py for storing the messages and predictions; views.py for bringing all of that together and send out the requested json data.
