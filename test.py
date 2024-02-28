import requests

def f1():
    url = "http://127.0.0.1:8000/ok"
    response = requests.get(url)
    return(response.json())

def f2():
    url = "http://127.0.0.1:8000/hello"
    response = requests.get(url, params={"name": "Giorgos"})
    return(response.json())

def f3():
    url = "http://127.0.0.1:8000/chat"
    data =  {
    "model": "gpt-4",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello"},
    ]
}
    response = requests.post(url, json=data)
    return(response.json())

suggested_titles= "Swish Symphony - A Journey Through Hoops Harmony and Slam Dunk Serenade"+ "Court Chronicles: The Game Beyond the Game - Dribble Dreams Unveiled"+"Fast Break Fantasia: Bounce Back Ballet of Triple Threat Tango"+"The Jumpshot Jamboree - Alley-Oop Allegro in Dunk Dynasty Fugue"+"Rebound Rhapsody: Basketball Ballet Beyond the Buzzer's Hoops Hues"+"The Spin Move Sonata - Backboard Ballerina's Net Notes Elegance"

def f4(suggested_titles):
    url = "http://127.0.0.1:8000/prompt"
    data =  {
    "prompt": f"Hi, i want to create a movie title very similar to{suggested_titles}. Give me just the titles"
}
    response = requests.post(url, json=data)
    return(response.json())


gwords="Greece, George, Maria, Valor, Computers, Cat, Seafood, Steak, Python"
def f5(gwords):
    url = "http://127.0.0.1:8000/chat"
    data =  {
    "model": "gpt-4",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"create a phrase using all the {gwords}."}
    ]
}
    response = requests.post(url, json=data)
    return(response.json())



print(f1()['message'],end='\n')
print(f2()['message'],end='\n')
print(f3()['response']['content'],end='\n')
print(f4(suggested_titles)['response']['content'],end='\n')
print(f5(gwords)['response']['content'])



