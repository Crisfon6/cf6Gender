# cf6Gender

This is an artificial intelligence model to predict gender by name, if you know a way to improve the model send me a message

  ### Example: 
  ```
    "cristhian" -> male
    "maria claudia" -> female
   ```
# How use
### clone repo
```shell
  git clone https://github.com/Crisfon6/cf6Gender.git
```
### create virtual enviroment
```shell
  virtualenv env  
```
### activate your virtual enviroment
#### Mac/linux:
```shell
  source env/bin/activate
 ```
 #### Windows:
 ```shell
  .\test\Scripts\activate
```
### install requirements
```
pip3 install -r requirements.txt
```
### create \__init__.py
this for import Cf6Gender
```
touch __init__.py
```
# OK let's try it
```python
from Cf6Gender import get_gender

print (get_gender ('cristhian'))
```
#### output:
```shell
>>> male
```
# References:
 <https://github.com/ksdkamesh99/Ling-Gender>
