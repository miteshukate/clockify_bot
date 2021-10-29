# clockify_bot
The bot to read entries from text file and create clockify entries

Download Dependency 

pip install -r requirements.txt

#### Pre-requisite
This bot requires a valid clockify API.
- Get it from https://clockify.me/user/settings
and update CLOCKIFY_SECRETE in .env file (create if does not exist)
- Required PROJECT_ID to identify your project (It will give you all project, and their id if does not update)
- Require passing staring date eg. python main 2021-10-01 (yyyy-MM-dd) 

#### Run application
1. Create entries in `entries.txt` everytime  you run this application
2. Run command in root folder python main.py {yyyy-MM-dd format date}