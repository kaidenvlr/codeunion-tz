# Test Task Code Union

Цель задания: Разработка сервиса для отслеживания курса валют через XML

Необходимо создать сервис на Django, который предоставляет информацию о текущих курсах валют в отношении к тенге (KZT).

## Getting started

Используйте `make`, чтобы упростить запуск проекта

```bash
make help
```

Получим такой ответ:

```bash
help                 Show this help
start                Start server
test                 Start tests
```

Для запуска проекта с помощью `docker-compose` используйте

```bash
make start
```

Для запуска тестов используйте

```bash
make test
```

## API Reference

#### Obtain API Key

```http
  POST /api-token-auth/
```

| Parameter  | Type     | Description                             |
|:-----------|:---------|:----------------------------------------|
| `username` | `string` | **Required**. Username of existing user |
| `password` | `string` | **Required**. Password of existing user |

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

## Usage/Examples

To create superuser with default username and password, provided from environment file:

```bash
python3 manage.py create_superuser
```

To get currencies or currency:

```bash
python3 manage.py get_currency [--name NAME]
```

To update currency:

```bash
python3 manage.py update_currency id ID rate RATE
```