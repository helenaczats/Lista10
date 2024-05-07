import json
import pytest        
import requests  

     
store_id = 9       
store_petId = 450        
store_quantity = 1
store_shipDate= "2024-06-07T14:01:53.199+0000"             
store_status = "placed" 
store_complete = True    


url = "https://petstore.swagger.io/v2/store"            
headers = { "Content-Type": "application/json" }       


def test_post_store():
    
    store = open("./fixtures/json/store.json")  
    data = json.loads(store.read())             
    
    response = requests.post(           
        url = f"{url}/order",                      
        headers = headers,              
        data = json.dumps(data),        
        timeout = 5                    
    )

    response_body = response.json()    
    
    assert response.status_code == 200
    assert response_body["id"] == store_id
    assert response_body["petId"] == store_petId
    assert response_body["quantity"] == store_quantity
    assert response_body["shipDate"] == store_shipDate
    assert response_body["status"] == store_status
    assert response_body["complete"] == store_complete 
    
    
def test_get_store():
    
    response = requests.get(
        url = f"{url}/order/{store_id}", 
        headers = headers
      
    )
    
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body["id"] == store_id
    assert response_body["petId"] == store_petId
    assert response_body["quantity"] == store_quantity
    assert response_body["shipDate"] == store_shipDate
    assert response_body["status"] == store_status
    assert response_body["complete"] == store_complete 
    
    
def test_delete_store():
    
    response = requests.delete(
        url = f"{url}/order/{store_id}",   
        headers = headers
    )
    
    response_body = response.json()
    
    assert response.status_code == 200   
    assert response_body["code"] == 200  
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(store_id)