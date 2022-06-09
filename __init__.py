import datetime
import logging
import azure.functions as func
import requests
import ast

def main(mytimer: func.TimerRequest) -> None:
  utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
  
  if mytime.past_due:
    logging.info("Timer is past due!")
    
  # 0 */1 * * * * -> every min
  # */10 * * * * * -> every 10s
  # 0 */1 * * * * -> every min
  # 0 0 10 * * * -> every 10am UTC time (houston time is 5am)
  
  # These are the azure keyvaults variables
  CLIENT_ID = ""
  CLIENT_SECRET = ""
  RESOURCE = "" # this is the resource id on your azure app
  URL = "www.sample.com/api/email"
  
  post_url = "https://login.microsoftonline.com/********/oauth2/token"
  post_body={
   'grant_type' : 'client_credentials',
   'client_id' : CLIENT_ID,
   'client_secret' : CLIENT_SECRET,
   'resource': RESOURCE
  }
  response = requests.post(post_url, data = post_body).content
  dict_token = response.decode("UTF-8")
  access_token = ast.literal_eval(dict_token)["access_token"]
  
  # GET to call api
  get_email_url = URL
  get_headers = {'Authorization' : 'Bearer {}'.format(access_token)}
  get_result = requests.get(get_email_url, headers = get_headers, verify=False).content
  print(f'---- result: {get_result}')
  
  
  
