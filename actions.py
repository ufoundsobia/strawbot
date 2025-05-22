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

from rasa_sdk import Action
from rasa_sdk.types import Text
import random

class ActionEmotionalResponse(Action):
    def name(self) -> Text:
        return "action_emotional_response"

    def run(self, dispatcher, tracker, domain):
        # Get the latest message sentiment
        last_message = tracker.latest_message.get('text', '')
        
        # Simple sentiment analysis
        negative_words = ['sad', 'hurt', 'pain', 'crying', 'depressed', 'anxious']
        positive_words = ['happy', 'excited', 'amazing', 'wonderful', 'great']
        
        # Check message content and respond appropriately
        if any(word in last_message.lower() for word in negative_words):
            responses = [
                "my strawberry heart is literally breaking rn 💔🍓 but remember - even the sourest strawberries become sweet with time! want to talk it out? i'm here with virtual hugs and strawberry wisdom! ✨",
                "stop everything because my pookie is hurting?? 😭🍓 letting you know that you're the sweetest berry in my patch and this feeling is temporary! need me to spam you with serotonin boosting strawberry content?",
                "naurr why am i crying in the strawberry fields?? 🥺🍓 you're stronger than you think ! like a strawberry growing through concrete fr fr! here for you always! 💕"
            ]
        elif any(word in last_message.lower() for word in positive_words):
            responses = [
                "PERIOD ! 👑🍓 you're literally glowing like a sun-ripened strawberry rn! this energy is everything! keep serving !",
                "the way you're absolutely eating this up?? 😌🍓 strawberry queen behavior detected! so proud of you !",
                "NOT YOU BEING THE MOMENT?? 💅🍓 this is the strawberry success i love to see! you really said 'watch me slay' and did exactly that!"
            ]
        else:
            responses = [
                "girl your energy is giving strawberry main character rn and i'm here for it! 🍓✨",
                "the way you just made my strawberry senses tingle! tell me more! 👀🍓",
                "okay but why is everything you say so iconic?? giving strawberry wisdom fr fr! 💭🍓"
            ]
            
        dispatcher.utter_message(text=random.choice(responses))
        return []

class ActionContextualStrawberryThought(Action):
    def name(self) -> Text:
        return "action_contextual_strawberry_thought"

    def run(self, dispatcher, tracker, domain):
        # Get the latest intent
        latest_intent = tracker.latest_message['intent'].get('name')
        
        if latest_intent == 'express_confusion':
            message = "fun fact: strawberries are the only fruit with seeds on the outside - sometimes the best things don't make conventional sense! 🍓✨"
        elif latest_intent in ['affirm_positive', 'mood_great']:
            message = "just like strawberries growing towards the sun, we're thriving! 🍓☀️"
        elif latest_intent in ['affirm_negative', 'mood_sad']:
            message = "remember: even wild strawberries start tiny before they bloom! you got this! 🌱🍓"
        else:
            message = "random strawberry thought: did you know strawberries are actually part of the rose family? we love an unexpected queen! 👑🍓"
            
        dispatcher.utter_message(text=message)
        return []