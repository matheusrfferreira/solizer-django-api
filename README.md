# Solizer-API

### Register

`POST https://solizer-api.herokuapp.com/api/register/`

```json
    {
	    "first_name": "John",
	    "last_name": "Jobs",
	    "email": "john@email.com",
	    "cell_phone_number": "1212341234",
	    "address": "House 123",
	    "cpf": "12312312312",
	    "username": "john",
	    "password": "123",
	    "user_type": 2
    }
```

### Response

    201 Created
```json
    {
	    "id": 1,
	    "username": "john",
	    "first_name": "John",
	    "last_name": "Jobs",
	    "email": "john@email.com",
	    "cell_phone_number": "1212341234",
	    "address": "House 123",
	    "cpf": "12312312312",
	    "cnpj": "",
	    "user_type": 2
    }
```    
### Note

```json
    {
	    "user_type": 2 # Integrator
    }
```    
```json
    {
	    "user_type": 1 # Client
    }
```    
```json
    {
	    "cnpj": "" # Optional
    }
```
### Login

`POST https://solizer-api.herokuapp.com/api/login/`

```json
    {
	    "username": "john",
	    "password": "123",
    }
```

### Response

    200 Ok
```json
    {
	    "token": "4b12e9n04a993f4a00f8b63y4k34yf610cf743c6",
    }
```
### List Clients

`GET https://solizer-api.herokuapp.com/api/users/clients/` 

   
`HEADER:` 
```json
    {
	    "Authorization": "Token 4b12e9n04a993f4a00f8b63y4k34yf610cf743c6"
    }
```

### Response

    200 Ok
```json
    [
	    {
            "username": "john",
            "first_name": "John",
            "last_name": "Rock",
            "email": "john@email.com",
            "cell_phone_number": "12312312312312",
            "address": "House 123"
	    }
    ]
``` 
### List Integrators

`GET https://solizer-api.herokuapp.com/api/users/integrators/` 

   
`HEADER:` 
```json
    {
	    "Authorization": "Token 4b12e9n04a993f4a00f8b63y4k34yf610cf743c6"
    }
```

### Response

    200 Ok
```json
    [
	    {
            "username": "john2",
            "first_name": "John",
            "last_name": "Sanji",
            "email": "john2@email.com",
            "cell_phone_number": "2143211234",
            "address": "House 321"
	    }
    ]
```                     
