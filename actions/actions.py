from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class Action_Data(Action):
    def name(self) -> Text:
        return "action_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity_value = next(tracker.get_latest_entity_values("data"), None)
        print("action data")
        print(entity_value)

        
        if entity_value == "name":
            dispatcher.utter_message(text="Prashanth",image="hi2")
        elif entity_value in ["mail", "email", "gmail"]:
            dispatcher.utter_message(text="prashanthpathigari@gmail.com",image="hi2")
        else:
            dispatcher.utter_message(text="Sorry, I didn't understand. Please ask clearly.",image="confuse")

        return []


class ActionData_education(Action):
    def name(self) -> Text:
        return "actions_education"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity_value = next(tracker.get_latest_entity_values("education"), None)
        entity_passed = next(tracker.get_latest_entity_values("complete"), None)
        print("education action",entity_value," ",entity_passed)
        ans=""

        
        if entity_value == "school" or entity_value=="education" or entity_value==None:
            p1="I have done my scooling in St anthoy's high school Sangareddy \n"
            if entity_value == "school":
                print(entity_passed)
                dispatcher.utter_message(text= p1 if entity_passed==None else "2020",image="cool1")
            else:
                ans=ans+p1
        if entity_value == "inter" or entity_value=="education" or entity_value==None:
            p1="I done my intermediate in Sir chainthanya junior kalashala miyapur,\nit's useless to know about this(my inter) collage\n"
            if entity_value == "inter":
                dispatcher.utter_message(text=ans+p1 if not entity_passed else "2022",image="cool1")
            else:
                ans=ans+p1
        if entity_value == "college" or entity_value=="education" or entity_value==None:
            p1="I am doing me btech with ECE major in cvr college of engineering ibrahimpatnam \n"

            if entity_value == "college" or entity_value==None:
                
                dispatcher.utter_message(text=ans+p1 if entity_passed==None else "ongoing till 2026",image="cool1")
            else:
                ans=ans+p1
        if entity_value!=None and entity_value not in ["college","inter","school","education"] :
            dispatcher.utter_message(text="Sorry, I didn't understand. Please ask clearly.",image="confuse")
        dispatcher.utter_message(text=ans,image="cool1")
        

        return []


class ActionData_expriences(Action):
    def name(self) -> Text:
        return "actions_experience"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity_value = next(tracker.get_latest_entity_values("data"), None)
        print("action exprience")
        print(entity_value)
        ans=""

        if entity_value == "intership":
            dispatcher.utter_message(text="No unforunately i did't go any I am still trying for it",image="low1")
        elif entity_value == "experience" or entity_value == "work":
            
            dispatcher.utter_message(text="I am still sreach imporving my skills , don't have eny exprecis",image="cool1")
        elif entity_value == None or len(entity_value)==0:
            
            dispatcher.utter_message(text="I am a student looking for opurniies",image="coodontknow")
        else:
            dispatcher.utter_message(text="Sorry, I didn't understand. Please ask clearly.",image="confuse")
        dispatcher.utter_message(text=ans)
        return []


class ActionData_family(Action):
    def name(self) -> Text:
        return "actions_family"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity_member = next(tracker.get_latest_entity_values("family_member"), None)
        entity_type = next(tracker.get_latest_entity_values("info_type"), None)
        print("action family")
        print(entity_member," ",entity_type)
        
        ans="sorry!.., I don't like to share any too personal information"
        if entity_member=="girl friend" or entity_type=="about":
            dispatcher.utter_message(text=ans,image="prayer")
            return []
        #  
        if entity_type=="name":
            print("father is got")
            if entity_member=="father":
                ans="pochaiah"
            elif entity_member=="mother":
                ans="sunitha"
            elif entity_member=="brother" or entity_member=="siblings":
                ans="praveen"
            elif entity_member=="sister" or entity_member=="siblings":
                ans="I don't have any"
            else:
                ans=" cant able to understand please check spelling or ask peoperrly , thank you"

        elif entity_type=="have":
            print("father is got")
            if entity_member=="father":
                ans="yes, his hame is pochaiah"
            elif entity_member=="mother":
                ans="yes , her name is sunitha"
            elif entity_member=="brother" or entity_member=="siblings":
                ans="yes his hame is praveen"
            elif entity_member=="sister":
                ans="I don't have any"
            else:
                ans=" cant able to understand please check spelling or ask peoperrly , thank you"

        elif entity_type=="work":
            ans="sorry i dont like to share personal information"
            dispatcher.utter_message(text=ans,image="prayer") 
        else:

            ans="sorry can't able to understand can you ask properly/model not yet trined for this , thank you"
            dispatcher.utter_message(text=ans,image="confuse") 
        
        dispatcher.utter_message(text=ans,image="love3") 

        return []


class ActionData_learn(Action):
    def name(self) -> Text:
        return "action_learn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entity_time = next(tracker.get_latest_entity_values("time"), None)
        if entity_time!=None:
            dispatcher.utter_message(text="It took 1 year to learn DSA,Full stack , and i spend almost 3 moths on ml",image="cool1")

        entity_value = next(tracker.get_latest_entity_values("courses"), None)
        print("action_learn")
        print("entity value",entity_value)
        ans=""

        if entity_value == "full stack":
            dispatcher.utter_message(text=(
        "I learned most of this from YouTube. If you want to learn, I’d recommend:\n"
        "1. React: Chai aur Code\n"
        "2. Backend: CodeWithHarry, Chai aur Code\n"
        "3. Projects: Codesistency (highly recommended)"
                    )
)
        elif entity_value == "dsa":
            dispatcher.utter_message(text="I directly jumped to leet code with first year basic",image="cool2")

        elif entity_value==None:
            dispatcher.utter_message(text="I have learn most my things from youtube",image="cool2")

        elif entity_value in ["paid","programs","courses","course"]:
            
            dispatcher.utter_message(text="no i learn all my things from you tube, and from projects",image="cool1")

        elif entity_value == "future":
            dispatcher.utter_message(text="I am learing nextjs, chat bots , machine learning",image="cool2")
        elif entity_value == "workshops":
            dispatcher.utter_message(text="I have attended arduino works shop, iot workshop",image="cool1")
        elif entity_value == "hackthons":
            dispatcher.utter_message(text="I have participated but did not won any",image="low2")
        else:
            dispatcher.utter_message(text="Sorry, I didn't understand. Please ask clearly.",image="confuse")
        dispatcher.utter_message(text=ans,image="cool1")
        return []


class ActionData_personalInfo(Action):
    def name(self) -> Text:
        return "actions_personal_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity_value = next(tracker.get_latest_entity_values("data"), None)
        print("action personal info")
        print(entity_value," ")
        ans=""
        
        if entity_value == "mail":
            dispatcher.utter_message(text= "Sure prashanthpathigari@gmail.com \n",image="cool1")

        elif entity_value == "linkedin":
            dispatcher.utter_message(text= "Sure https://www.linkedin.com/in/prashanth-kumar-pathigari-a303112b7/ \n",image="cool1")

        elif entity_value in ["live demos","demo"]:
            dispatcher.utter_message(text= "If you want to see demos of my project visit my linked in \n https://www.linkedin.com/in/prashanth-kumar-pathigari-a303112b7/ \n",image="cool1")

        elif entity_value == "git":
            dispatcher.utter_message(text= "Sure https://github.com/I-am-prashanth \n",image="cool1")

        elif entity_value  in ["facebook","insta","twitter","X","telegram","phone","contact"]:
            p1="i dont use much "+entity_value+" much but happy to share my linkedin \n https://www.linkedin.com/in/prashanth-kumar-pathigari-a303112b7/ "
            dispatcher.utter_message(text= p1,image="cool1")

        else :
            dispatcher.utter_message(text="Sorry, I didn't understand. Please ask clearly.",image="confuse")
        dispatcher.utter_message(text=ans)
        
        return []
    

class ActionData_Projects(Action):
    def name(self) -> Text:
        return "action_projects"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity_value = next(tracker.get_latest_entity_values("projects"), None)
        print("action projects")
        print(entity_value)
        ans=""
        if(entity_value=="best" or entity_value=="cantten"):
            entity_value="canteen"

        if entity_value == "mini" or entity_value==None :
            p1 = (
                  "• This is my first full-stack project.\n"
                   "In this project, I built a web application that shows all semester results on a single page.\n"
                   "GitHub: https://github.com/I-am-prashanth/my-mini-project.git\n"
                   "visit to project section for more details \n \n"
                )
            if entity_value == "mini":
                dispatcher.utter_message(text=p1)
            else:
                ans=ans+p1
        if entity_value == "canteen" or entity_value==None:
            p1 = (
    "• This is one of my most challenging full-stack projects.\n"
    "I developed a web application for my college canteen that allows online payments,\n"
    "which helps reduce crowd and waiting time in the canteen.\n"
    "GitHub: https://github.com/I-am-prashanth/CVR-Canteen-Project--2.git\n"
    "visit to project section for more details \n \n"
)
            if entity_value == "canteen":
                
                dispatcher.utter_message(text=p1,image="cool1")
            else:
                ans=ans+p1
        if entity_value in ["bank","chatbot","finalyear","major project",None]:
            p1 = (
    "• This is my first ML and NLP project.\n"
    "I built a banking assistant chatbot that can answer various queries related to banking services.\n"
    "GitHub: https://github.com/I-am-prashanth/CVR-Canteen-Project--2.git\n"
    "Visit the Projects section for more details."
)

            if entity_value !=None :
                
                dispatcher.utter_message(text=p1,image="cool1")
            else:
                ans=ans+p1
        if entity_value not in ["bank","chatbot",None,"canteen","mini"]:
            print("not cae",entity_value)
            dispatcher.utter_message(text="Sorry, I didn't understand. Please ask clearly.",image="confuse")
        dispatcher.utter_message(text=ans,image="cool1")
        return []


class ActionData_what_i_learned(Action):
    def name(self) -> Text:
        return "actions_what_i_have_learned"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity_value = next(tracker.get_latest_entity_values("data"), None)
        print("action:what i have learned")
        print(entity_value," ")
        ans="I have learned a lot "
        
        if entity_value == "projects":
            dispatcher.utter_message(text=ans+"\n1. Learned sloving real time problems \n2. improved ploblem sloving skills etc..,\n",image="cool1")

        elif entity_value == "college":
            dispatcher.utter_message(text=ans+"in my betch life\n1. taking rspsibilities \n2. dsa,full stack \n3.understanding value of money etc..,",image="cool1")

        elif entity_value in ["school","inter"]:
            dispatcher.utter_message(text= "I didn't learn much i just enjoyed my life and had fun \n",image="cool1")

        elif entity_value == "life":
            dispatcher.utter_message(text= "many thing and i am still learning \n1.happiness , love,friendship \n2.resposibilities, money management, time management etc..,  \n",image="cool1")

        else :
            dispatcher.utter_message(text="Sorry, I didn't understand. Please ask clearly.",image="confuse")
        # dispatcher.utter_message(text=ans)
        
        return []
