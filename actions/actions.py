# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

Class ActionCovidTracker(Action):
     def name(self):
          return "action_covid_cases"
     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #entities=[e for e in tracker.latest_message['entities']]
        entities=tracker.latest_message['entities']

        for e in entities:
                #print(e['entity'])
                if e['entity']=='location_covid':
                        name=e['value']
                        #print(name)

        response = requests.get('https://api.covid19india.org/data.json').json()
        #print(response['statewise'][-1])
        for data in response['statewise']:
                #when response matches entity
                if data['state']==name.title: 
                        #print(data)
                        message="Active: "+data['active']+" Confirmed: "+data['confirmed']+" Deaths: "+data['deaths']+" Recovered: "+data['recovered']
                        dispatcher.utter_message(message)
                        break
                #even at the end of iteration if dresponse doesn't macth entity
                elif data['state']==response['statewise'][-1]['state']: 
                        message="Please enter a valid State or for Total counts type Total.."
                        dispatcher.utter_message(message)
                else:
                        continue
        
        return []