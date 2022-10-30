# Usage

### Endpoints

> <https://october-hackathon-edualt.up.railway.app/advocates/>
>
> <https://october-hackathon-edualt.up.railway.app/companies/>
>
> <https://october-hackathon-edualt.up.railway.app/links/>
>
## /advocates/

### GET

You can provide an username through the url to get an object

```url
../advocates/edualt
```

Also you can provide url params, filtering by username

```url
../advocates/?query=edualt
```

### POST

Send the next values to create an advocate,
`companies` field is required, so send it as a `null list` or send an id or multiple id's as a list.

```json
{
    "profile_pic": null,
    "username": "edualt",
    "name": "Eduardo Altuzar",
    "short_bio": "hi, im edualt",
    "long_bio": "Backend developer",
    "companies": [],
}
```

## /companies/

### GET

You can provide an id through the url to get an object

```url
../companies/1
```

### POST
Send the next values to create a company,
`advocates` field is required, so send it as a `null list` or send an id or multiple id's as a list.

```json
{
    "name":"MongoDB",
    "logo": null,
    "summary":"Some text...",
    "advocates":[]
}
```
## /links/

### GET

You can provide an id through the url to get an object

```url
../links/1
```

### POST
Send the next values to create a link, advocate cannot be null.
```json
{
    "name":"github",
    "url":"https://github.com/edualt",
    "advocate": 1
}
```


