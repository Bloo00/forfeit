# Django forfeit

- [ ] fork and clone
- [ ] Add a `.env` file with `SECRET_KEY=whatever-key-you-want`
- [ ] Install `python-dotenv` -> `pip3 install python-dotenv`
- [ ] Create database in SQL called `catsoncats` ( reference the `settings.py` file )
  - [ ] `createdb catsoncats`
- [ ] Migrate the database `python3 manage.py migrate`
- [ ] Start server `python3 manage.py runserver`

# Authentication

To get an idea of how `Django Authentication` work, view the `models.py` and `views.py` file.

### `User` Model

| Column Name | Data Type | Notes |
| --------------- | ------------- | ------------------------------ |
| _id | Integer | Serial Primary Key, Auto-generated |
| name | String | Must be provided |
| email | String | Must be unique / used for login |
| password | String | Stored as a hash |
| timesLoggedIn | Number | used to track the amount of times a user logs in |
| date | Date | new Date() |
| __v | Number | Auto-generated |

### `Summoner` Model

| Column Name | Data Type | Notes |
| --------------- | ------------- | ------------------------------ |
| _id | Integer | Serial Primary Key, Auto-generated |
| Summoner name | String | Must be provided |
| Solo Rank | String | get icon pic |
| Flex Rank | String | get icon pic |
| Win rate | Number | show a cute graph |
| Riot id | int | used for api stoof |
| Puuid | int | ditto |
| Account id | int | still dont know why there are so many |
| Profile id | int | used to get profile icon from data dragon |
| profile Icon | image | picture they can choose |
| Kills | int | pew pew |
| deaths | int | pew pew |
| assists | int | pew pew |
| Items | String | links to icons? |
| Level | Int | max lvl that game |
| Rank | String | Show lvl when not found |
| Creep Score | Int | creeps killed |
| __v | Number | Auto-generated |

### `Match` Model

| Column Name | Data Type | Notes |
| --------------- | ------------- | ------------------------------ |
| _id | Integer | Serial Primary Key, Auto-generated |
| Summoner name | String | Must be provided |
| Game Type | String | of 3 maybe 4 |
| Win or Loss | String | color maybe? |
| Duration | Int | game length |
| Players | Array | list of all the characters that game |
| Blue Barons | Int | number of wiggley worms killed |
| Blue Dragon | Int | ditto |
| Blue Towers | Int | ditto |
| Blue Gold total | Int | ditto |
| Red Barons | Int | number of wiggley worms killed |
| Red Dragon | Int | ditto |
| Red Towers | Int | ditto |
| Red Gold total | Int | ditto |
| __v | Number | Auto-generated |

### `Rank` Model

| Column Name | Data Type | Notes |
| --------------- | ------------- | ------------------------------ |
| _id | Integer | Serial Primary Key, Auto-generated |
| Summoner name | String | Must be provided |
| Game Type | String | Solo or 5v5 |
| Wins | Int |  |
| Loss | Int |  |
| LP | Int |  |
| Icon | Image | of all ranks |
| __v | Number | Auto-generated |