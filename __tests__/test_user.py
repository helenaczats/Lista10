import json
import pytest        
import requests 
from utils.utils import ler_csv      

user_id = 145768701      
user_username = "Lola"        
user_firstName = "Lorena"        
user_lastName = "Albuquerque"  
user_email = "lola.albuquerque@icloud.com"             
user_password = "verde" 
user_phone = "996976547"
user_userStatus = 1


url = "https://petstore.swagger.io/v2/user"            
headers = { "Content-Type": "application/json" }       


def test_post_user():
    
    user = open("./fixtures/json/user1.json")  
    data = json.loads(user.read())             
    
    response = requests.post(           
        url = url,                     
        headers = headers,              
        data = json.dumps(data),        
        timeout = 5                    
    )

    response_body = response.json()     
    
    assert response.status_code == 200
    assert response_body["code"] == 200  
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(user_id)
    
    
def test_get_user():
    
    response = requests.get(
        url = f"{url}/{user_username}",  
        headers = headers
    )
    
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body["id"] == user_id 
    assert response_body["username"] == user_username
    assert response_body["firstName"] == user_firstName
    assert response_body["lastName"] == user_lastName
    assert response_body["email"] == user_email 
    assert response_body["password"] == user_password
    assert response_body["phone"] == user_phone
    assert response_body["userStatus"] == user_userStatus
    
    
def test_put_user():
    
    user = open("./fixtures/json/user2.json")
    data = json.loads(user.read())    
   
    response = requests.put(
        url = f"{url}/{user_username}",
        headers = headers,
        data = json.dumps(data),
        timeout = 5
    )
   
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body["code"] == 200
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(user_id)
    
def test_delete_user():
    
    response = requests.delete(
        url = f"{url}/{user_username}",
        headers = headers
    )
    
    response_body = response.json()
    
    assert response.status_code == 200   
    assert response_body["code"] == 200  
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(user_username)
    
  
@pytest.mark.parametrize("user_id,user_username,user_firstName,user_lastName,user_email,user_password,user_phone,user_userStatus",ler_csv("./fixtures/csv/user.csv"))

def test_post_user_dinamico(user_id,user_username,user_firstName,user_lastName,user_email,user_password,user_phone,user_userStatus):
   
    user = {}     
    user["id"] = int(user_id)
    user["username"] = user_username
    user["firstName"] = user_firstName
    user["lastName"] = user_lastName
    user["email"] = user_email
    user["password"] = user_password
    user["phone"] = user_phone
    user["userStatus"] = int(user_userStatus)
            
        
    user = json.dumps(obj=user, indent=4)
    print("\n" + user) 
        
    response = requests.post(
        url = url,
        headers = headers,
        data = user,
        timeout = 5
    )
            
    response_body = response.json()
        
    assert response.status_code == 200
    assert response_body["code"] == 200  
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(user_id)
       
        
@pytest.mark.parametrize("user_id,user_username,user_firstName,user_lastName,user_email,user_password,user_phone,user_userStatus",ler_csv("./fixtures/csv/user.csv"))        

def test_delete_user_dinamico(user_id,user_username,user_firstName,user_lastName,user_email,user_password,user_phone,user_userStatus):
   
    user = {}     
    user["id"] = int(user_id)
    user["username"] = user_username
    user["firstName"] = user_firstName
    user["lastName"] = user_lastName
    user["email"] = user_email
    user["password"] = user_password
    user["phone"] = user_phone
    user["userStatus"] = int(user_userStatus)
            
        
    user = json.dumps(obj=user, indent=4)
    print("\n" + user) 
        
    response = requests.delete(
        url = f"{url}/{user_username}",
        headers = headers,
        data = user,
        timeout = 5
    )
            
    response_body = response.json()
        
    assert response.status_code == 200
    assert response_body["code"] == 200  
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(user_username)     