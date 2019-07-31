# Mod4 - Take Home Challenge - Django

 [Django application](https://mod4-final-project.herokuapp.com/) hosted on Heroku that is able to serve up data about olympians from the 2016 olympics.

**Application Highlights:**
* 48 hour take-home challenge
* Django REST framework integration
* Robust PR documentation as seen [here](https://github.com/blake-enyart/take_home_challenge_django/pull/1)

## How to Use
The following endpoints are in production:
```
Request:
GET api/v1/olympians

Response:
{
  "olympians":
    [
      {
        "name": "Maha Abdalsalam",
        "team": "Egypt",
        "age": 18,
        "sport": "Diving"
        "total_medals_won": 0
      },
      {
        "name": "Ahmad Abughaush",
        "team": "Jordan",
        "age": 20,
        "sport": "Taekwondo"
        "total_medals_won": 1
      },
      {...}
    ]
}
```

```
Request:
GET api/v1/olympians?age=youngest

Response:
{
  "olympians": [
    {
      "name": "Ana Iulia Dascl",
      "team": "Romania",
      "age": 13,
      "sport": "Swimming"
      "total_medals_won": 0
    }
  ]
}
```

```
Request:
GET api/v1/olympians?age=oldest

Response:
{
  "olympians": [
    {
      "name": "Julie Brougham",
      "team": "New Zealand",
      "age": 62,
      "sport": "Equestrianism"
      "total_medals_won": 0
    }
  ]
}
```

## Contributing
* [Blake Enyart](https://github.com/blake-enyart) - Application design and development

### Location of Apps in Production
* [Django application](https://mod4-final-project.herokuapp.com/) - Django based backend with DRF

## Tech Stack
* Django - 2.2
* Django REST Framework - 3.9.2
* PostgreSQL - 11.3
* Django Heroku - 0.4.5
