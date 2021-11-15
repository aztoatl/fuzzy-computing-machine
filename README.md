# Dog facts API 

An API that will return random facts about dog.

This API is just a consumer of the [dog-facts-api](https://github.com/DukeNgn/Dog-facts-API), wrote with FastAPI for python 3.9

## Usage:
 This API is very simplistic and just have three functions. 
+ `http://localhost:8000/api/v1/` This will return a welcome message. Is used for testing purposes.
```JSON
{
    "msg":"Hello!! this is a small api which will give you dog facts."
}
```
The main functionallity is just ask for a amount of random facts: 
+ `http://localhost:8000/api/v1/dogs/1` This will return 1 fact.
```JSON
{
    "response":[{"fact":"President Theodore Roosevelt's Bull Terrier Pete ripped the pants off French Ambassador Jules Jusserand."}]
    
}
```
 if you give a bigger number you will get the anount of facts that match with the number given.

 + `http://localhost:8000/api/v1/dogs/all` will return all the facts stored in the original API database

## Build locally:

+ Installing dependiencies:
```BASH 
    python -m pip install ./app/requeriments.txt 
```
+ Start the API:
```BASH 
    uvicorn main:app --reload
```

## Test:

+ A small and simple test can be executed (after the requeriments are installed and while the api is running) just going to the app folder and execut:
```BASH
    pytest 
```

## Running the API in container

+ is as easy as build the Dockerfile located in the root level
```BASH
    docker  image build  -t dogapi:latest . 
```
+ but you can always pull it from dockerhub

```BASH 
   docker pull aztoatl/dogapi:tagname    
```
