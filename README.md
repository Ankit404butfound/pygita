
# gita
gita is a wrapper of [bhagavadgita.io](https://bhagavadgita.io) api for Python 3
# Installation
Install it from pypi using pip

`pip install gita`
# Authentication
*  Register on [bhagavadgita.io](https://bhagavadgita.io)
*  Create App
* Copy  Client Id and Client Secret 
* ```geeta.auth(client_id,secret_id)```

# Usage
  ## 1. Authentication using client_id and secret_id
  This function generate a new access_token
  `geeta.authUsage(client_id, client_secret)
  `
  -----------------------------------
  ## 2. Authentication using access_token
  If you have access_token, you don't need to generate a new one.
  `geeta.auth_token(access_token)
  `
  -----------------------------------
  ## 3. Get all chapters 
  
  ` chapter_list = get_chapter()
  `
  -----------------------------------
  
  
  ## 4. Get a specific chapter
  `chapter = get_chapter(chapter_number)
  `
  -----------------------------------
  
  ## 5. Get all Verses from all chapters
  
  `list_of_all_verses = get_verse()
  `
  -----------------------------------
  
  ## 6. Get all Verses from a specific chapter
  `verses = get_verse(chapter_number=chapter_number)
  `
  -----------------------------------
  ## 7. Get a specific verse from a specific chapter
  `verse = get_verse(chapter_number=chapter_number,verse_number=verse_number)
  `
 -----------------------------------
# Classes
 Above functions from point 3 to 4 returns a object of the `Chapter` class and from point 5 to 7 returns a object of the `Verse` class
# Objects
  ## Attributes of **Chapter** objects
    1. chapter_number
    2. chapter_summary
    3. name
    4. verses_count
    5. name_meaning
    6. name_translation
    7. name_transliterated
  ## Methods of **Chapter** objects
    1. next() : returns object of next chapter
    2. previous() : returns object of previous chapter
    3. verse() : returns object of verse in that chapter if verse_number is passed . Otherwise it returns the list of all verses in that chapter.
    4. json() : returns above attributes in dictionary or json format
   
-----------------------------------
  ## Attributes of **Verse** objects
    1. chapter_number
    2. verse_number
    3. text
    4. meaning
    5. transliteration
    6. word_meanings
  ## Methods of **Verse** objects
    1. next() : returns object of next verse
    2. previous() : returns object of previous verse
    3. verse() : returns the object of it's chapter
    4. json() : returns above attributes in dictionary or json format
   
   