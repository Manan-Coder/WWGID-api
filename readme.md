# What was good in your day!

## Overview

This is a simple Flask-based API that allows users to add and retrieve entries. It also provides random motivational messages. The API supports CORS and has multiple endpoints to interact with stored data.

## Features

- Add an entry
- Get all entries
- Get a random entry
- Receive motivational messages
- Simple HTML homepage

## Installation

### Clone the repository:

```sh
git clone https://github.com/your-repo.git
cd your-repo
```

### Install dependencies:

```sh
pip install flask flask-cors
```

### Run the application:

```sh
python app.py
```

## API Endpoints

### `GET /home`

Returns an HTML homepage.

### `POST /api/add`

Adds a new entry.

#### Request Body (JSON):

```json
{
  "entry": "Your entry text here"
}
```

#### Response:

```json
{
  "message": "Entry added successfully",
  "id": 1
}
```

### `GET /api/get-all`

Gets all stored entries.

#### Response (Example):

```json
[
  {
    "id": 1,
    "entry": "First entry",
    "date": "2025-03-07"
  }
]
```

### `GET /api/get-random`

Gets a random entry.

#### Response:

```json
{
  "id": 1,
  "entry": "A random entry",
  "date": "2025-03-07"
}
```

### `GET /api/get-motivation`

Returns a random motivational message.

#### Response:

```json
"You are amazing"
```

## License

MIT License

