
from _uxy_core._components import router
from _uxy_core._components import spiel
from _uxy_core._components import convo_data
import json
global VIEW_DIR
VIEW_DIR = 'src/components/res/'

def exe(userID, data, response, altResponse, choice, optionMatched, valid, maxRetry):
  
  if( not valid ):
    if( maxRetry ):
      return [], valid

  with open(VIEW_DIR+'pokedex.json') as p:
    dex=json.load(p)
    index=data['data']['text'].lower()
    if index in dex:
      pokemon=(dex[index]['id'])
      new=pokemon[1:]
      display='https://galardex.s3-ap-southeast-1.amazonaws.com/pkimage/'+new+'.png'
      
      
  
  print(data)
  
  response = spiel.display_attachment(display,'image')
 # response += router.route(userID,"new state")
  return response, True






