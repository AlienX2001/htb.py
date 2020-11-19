# Documentation for using this module

## Callable Funcion, their parameters and their returned objects

### 1. id_by_name(api_token,user_name) :-
Get a user's hackthebox ID by his/her name
#### api_token and user_name both in string format
  - If user exists then returns a dict object having ID and name
  ![success](https://raw.githubusercontent.com/AlienX2001/htb.py/main/images/success_id_by_name.jpg)
  - If user doesnt exist then returns a string "Not Found"
  ![fail](https://raw.githubusercontent.com/AlienX2001/htb.py/main/images/fail_id_by_name.jpg)
### 2. user_by_identifier(user_identifier) :-
Get's user's full information from his identifier
#### user_identifier in string format
  - If user exists then returns a dict object having full information
  ![success](https://raw.githubusercontent.com/AlienX2001/htb.py/main/images/success_user_by_identifier.jpg)
  - If user doesnt exist then returns a string "User not Found"
  ![fail](https://raw.githubusercontent.com/AlienX2001/htb.py/main/images/fail_user_by_identifier.jpg)
### 3. get_matrix(api_token,box_name) :-
Gets the matrix of a box by its name
#### api_token and box_name both in string format
  - If box exists then returns dict object having the matrix data
  ![success](https://raw.githubusercontent.com/AlienX2001/htb.py/main/images/success_get_matrix.jpg)
  - If box doesnt exist then returns a string "Box not Found"
  ![fail](https://raw.githubusercontent.com/AlienX2001/htb.py/main/images/fail_get_matrix.jpg)
### 4. box_info(api_token,box_name) :-
Gets general information of the box
#### api_token and box_name both in string format
  - If box exists returns dict object having information
  ![success](https://raw.githubusercontent.com/AlienX2001/htb.py/main/images/success_box_info.jpg)
  - If box doesnt exist returns a string "Box not Found"
  ![fail](https://raw.githubusercontent.com/AlienX2001/htb.py/main/images/fail_box_info.jpg)
### 5. walkthrough(box_name) :-
searches ippsec.rocks for any walkthrough for the specified box name
#### box_name in string format
  - If a box is retired and is present in ippsec's list then returns a string having it's youtube URL
  ![success](https://raw.githubusercontent.com/AlienX2001/htb.py/main/images/success_walkthrough.jpg)
  - If a box is active or is invalid or is not in ippsec's list then returns a string "Not Found"
  ![fail](https://raw.githubusercontent.com/AlienX2001/htb.py/main/images/fail_walkthrough.jpg)
