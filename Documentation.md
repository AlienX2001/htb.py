# Documentation for using this module

### Callable Funcion, their parameters and their returned objects

1. id_by_name(api_token,name) :- Get a user's hackthebox ID by his/her name
  api_token and name both in string format
  - If user exists then output will be returned as a dict object having ID and name
  ![success](https://imgur.com/yeL6JwN)
  - If user doesnt exist then output will be a string "Not Found"
  ![fail](https://imgur.com/081W8gy)
2. user_by_identifier(identifier) :- Get's user's full information from his identifier
  identifier in string format
  - 
