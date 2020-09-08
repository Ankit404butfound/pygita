from requests import get, post
import os


#Messages for different error response
message = {400:"Bad Request: The request was unacceptable due to wrong parameter(s).",401:"Unauthorized: Invalid access_token used.",402:"Request Failed.",404:"Not Found: The chapter/verse number you are looking for could not be found.",500:"Server Error: Something went wrong on our end."}



#Authentication from access_token
def auth_token(token):
  os.environ["gita_access_token"] = token



#Authentication from client_id and client_secret
def auth(client_id,client_secret):
  try:
    request = post("https://bhagavadgita.io/auth/oauth/token",data={"client_id":client_id,"client_secret":client_secret,"grant_type":"client_credentials","scope":"verse chapter"})
  except:
    print("Unable to send post request")
    return
  token = request.json()["access_token"]
  os.environ["gita_access_token"] = token
  return "You are authenticated by the generated token "+token



#function to get chapter(s) to get a single chapter pass the chapter number, to get all chapter don't pass anything
def get_chapter(chapter_number=None):
  if chapter_number == None:
    return Chapter.all()
  else:
    token = os.environ.get("gita_access_token")
    url = "https://bhagavadgita.io/api/v1/chapters/{chapter_number}?access_token={token}".format(chapter_number=chapter_number,token=token)
    try:
      request = get(url)
    except:
      print("unable to send get request")
      return 
    if request.status_code == 200:
      response = request.json()
    else:
      print(message[request.status_code])
      return
    return Chapter(response)
    
    
###Chapter class#####

class Chapter:
  def __init__(self,json_data):
    self.json = json_data
    self.chapter_number = json_data["chapter_number"]
    self.chapter_summary = json_data["chapter_summary"]
    self.name = json_data["name"]
    self.verses_count = json_data["verses_count"]
    self.name_meaning = json_data["name_meaning"]
    self.name_translation = json_data["name_translation"]
    self.name_transliterated = json_data["name_transliterated"]
  def next(self):
    chapter_number = self.chapter_number
    if chapter_number>=18:
      return "No chapter"
    return get_chapter(int(chapter_number)+1)
  
  def previous(self):
    chapter_number = self.chapter_number
    if chapter_number<=1:
      return "No chapter"
    return get_chapter(int(chapter_number)-1)
  def json(self):
    return self.__json
  
  def verse(self,verse_number=None):
    if verse_number==None:
      return Verse.all(self.chapter_number)
    else:
      return Verse(self.chapter_number,verse_number)
  @classmethod
  def all(cls):
    url = "https://bhagavadgita.io/api/v1/chapters?access_token={token}".format(token=os.environ.get("gita_access_token"))
    try:
      request = get(url)
    except:
      print("unable to send get request")
      return 
    if request.status_code == 200:
      response = request.json()
    else:
      print(message[request.status_code])
      return
    return [Chapter(json_data) for json_data in response]
   
      
#function to get verse(s). To get a specific verse pass chapter number and verse number ,to get list of all verses from a specific chapter pass only chapter number, to get list of all verses from all chaters pass nothing.
def get_verse(chapter_number=None,verse_number=None,language="en"):
  token = os.environ.get("gita_access_token")
  if token is None:
    print("Authentication not done")
    return
  if verse_number==None and chapter_number==None:
    return Verse.all()
  elif verse_number==None:
    return Verse.all(chapter_number)
  
  elif chapter_number == None:
    print("Please pass enough arguments")
  else:
    if language=="hi":
      url = "https://bhagavadgita.io/api/v1/chapters/{chapter_number}/verses/{verse_number}?access_token={token}&language={language}".format(chapter_number=chapter_number,verse_number=verse_number,language=language,token=token)
    else:
      url = "https://bhagavadgita.io/api/v1/chapters/{chapter_number}/verses/{verse_number}?access_token={token}".format(chapter_number=chapter_number,verse_number=verse_number,token=token)
    try:
      request = get(url)
    except:
      print("unable to send get request")
      return 
    if request.status_code == 200:
      response = request.json()
    else:
      print(message[request.status_code])
      return
    return Verse(response)
    
    
  
  
class Verse:
  def __init__(self,json_data):
    self.__json = json_data
    self.text = json_data["text"]
    self.meaning = json_data["meaning"]
    self.transliteration = json_data ["transliteration"]
    self.chapter_number = json_data["chapter_number"]
    self.verse_number = json_data["verse_number"]
    self.word_meanings = json_data["word_meanings"]
  def next(self):
    chapter_number = self.chapter_number
    verse_number = self.verse_number
    return get_verse(int(verse_number)+1,chapter_number)
    
  def previous(self):
    chapter_number = self.chapter_number
    verse_number = self.verse_number
    return get_verse(int(verse_number)-1,chapter_number)
  def json(self):
    return self.__json
  def chapter(self):
    return Chapter(self.chapter_number)
  @classmethod
  def all(cls,chapter_number=None):
    token = os.environ.get("gita_access_token")
    if chapter_number == None:
      url = "https://bhagavadgita.io/api/v1/verses?access_token={token}".format(token=token)
    else:
     url = "https://bhagavadgita.io/api/v1/chapters/{chapter_number}/verses?access_token={token}".format(chapter_number=chapter_number,token=token)
    if token is None:
      print("Authentication not done")
      return
    try:
      request = get(url)
    except:
      print("unable to send get request")
      return 
    if request.status_code == 200:
      response = request.json()
    else:
      print(message[request.status_code])
      return

    return [Verse(json_data) for json_data in response]
  
    
    