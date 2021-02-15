# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import os, requests

class ActionWeather(Action):

  def name(self) -> Text:
    return "action_weather"

  def run(self, dispatcher,tracker,domain):
          
    loc = tracker.get_slot('GPE')
    print(loc)
    degree_sign= u'\N{DEGREE SIGN}'
    # print(dir(os.environ))

    payload = {'q': loc, 'units':'metric', 'appid': os.environ['WEATHER_API_KEY']}
    response = requests.get('http://api.openweathermap.org/data/2.5/find', params=payload)
    
    try:
      data = response.json()
      print(data)
      print(type(data))   
      x = data['list'][0]

      temp = x['main']['temp']
      desc = x['weather'][0]['description']
      city = x['name']
      humidity = x['main']['humidity']
      wind_speed = x['wind']['speed']
      clouds = x['clouds']['all']
    
      weather_data = """It is {}{}C in {}. The humidity is {}%, wind speed is {} meter/sec, cloudiness in the sky is {}%, and it is {} at the moment.""".format(temp, degree_sign,city, humidity, wind_speed, clouds, desc)
      dispatcher.utter_message(weather_data)

      return [SlotSet("GPE", None)]

    except requests.exceptions.HTTPError as e:
      dispatcher.utter_message(text="City not found!")

    except Exception as e:
      dispatcher.utter_message(text="Could not find the city!")


class ActionGreetName(Action):

  def name(self) -> Text:
    return "action_greet_name"

  def run(self, dispatcher,tracker,domain):

    name = tracker.get_slot('PERSON')
    if name is not None:  
      dispatcher.utter_message(text="Nice to meet you, {}!".format(name))
      return [SlotSet("PERSON", None)]

    else:
      dispatcher.utter_message(text="I see , carry on !")


class ActionFeedback(Action):
  def name(self) -> Text:
    return "action_feedback"

  def run(self, dispatcher, tracker, domain):
    
    intent = tracker.get_intent_of_latest_message()
  

    if intent == "affirm":
      return [SlotSet('feedback', True)]

    elif intent == "deny":
      return [SlotSet('feedback', False)]

    return []

    



