## API Reference

#### Obtain API Key

```http
  POST /api-token/
```

| Parameter  | Type     | Description                             |
|:-----------|:---------|:----------------------------------------|
| `username` | `string` | **Required**. Username of existing user |
| `password` | `string` | **Required**. Password of existing user |

#### Refresh access token

```http
  POST /api-token/refresh/
```

| Parameter | Type  | Description                 |
|:----------|:------|:----------------------------|
| `refresh` | `str` | **Required**. Refresh Token |

#### Verify Token

```http
  POST /api-token/verify/
```

| Parameter | Type  | Description                |
|:----------|:------|:---------------------------|
| `token`   | `str` | **Required**. Access Token |

#### Get all currencies

```http
  GET /currencies
```

#### Get item

```http
  GET /currencies/<int:pk>
```

| Parameter | Type  | Description                           |
|:----------|:------|:--------------------------------------|
| `pk`      | `int` | **Required**. Id of currency to fetch |

#### Register user

```http
  POST /register/
```

| Parameter          | Type     | Description                                  |
|:-------------------|:---------|:---------------------------------------------|
| `username`         | `string` | **Required**. Username of new user           |
| `password`         | `string` | **Required**. Password of new user           |
| `confirm_password` | `string` | **Required**. Repeat of password of new user |

