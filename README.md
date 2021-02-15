# Rasa-Weather-Bot
Chatbot built using Rasa framework that let users know the weather conditions over 200,000 cities globally in real time.
- Api Used - Open Weather Map 
- Rasa - 2.27 version

### To set up your working environment 

1. Clone the repository -  `https://github.com/meghaggarwal/Rasa-Weather-Bot.git` inside your working directory.

2. Create a conda virtual environment. 
   `conda create --name env python==x.x.x`
   Make ensure that the version of conda environment and base python environment is same.
   You can check it using `python --version`
   
3. Activate the conda environment - `conda activate env`

4. Use your own api key and save it in your environment variables as VARIABLE = WEATHER_API_KEY and Value = `Your API key`

5. Make sure you open your favourite terminal (cmd/windows terminal) as Administrative privileges if you are using Windows OS to perform following operations-

- Install the necessary packages inside your conda env.
 `pip install -r requirements.txt`
 
 #### This will install necessary dependencies including Spacy. We have used conda environment here to install spacy models using requirements.txt file in Windows OS.
 
 - Now Link the spacy model of medium size md and of English language en using -
  `python -m spacy link en_core_web_md en`
 #### Linking model requires administrative privileges in Windows OS.
 
 ### To run Rasa Bot-
 
 #### Make Sure you are using your conda env environment.
 1. Navigate to project directory `cd Rasa-Weather-Bot`
 2. Train your Rasa Nlu and core using `rasa train`
 3. Run your custom actions using Rasa SDK server. `rasa run actions`
 4. In a seperate shell or terminal, run your rasa server. (Make sure you are within your conda env here as well.)
    `rasa run`
   
 Your default rasa server will start on http://localhost:5005, and rasa action server on http://localhost:5055.
 
 #### How to give user input to bot?
 
 For testing purpose you can run the chatbot on terminal. Replace step 4 with `rasa shell`
 This will run your rasa server as well as accept user input shell.
 
 For Reference - 
 
 ![Sample Image](https://github.com/meghaggarwal/Rasa-Weather-Bot/blob/main/Weather%20Chat%20Sample.png)
