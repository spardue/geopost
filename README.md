geopost
=======

Functions
---------

### `GET /posts/`

Either:
- Returns and list of all posts.
- Returns a list of all posts within a `distance` of `curr_latitude` and `curr_longitude`.

### `POST /posts/`

Creates a new post. *Must* give it a `message`, `longitude`, and `latitude` otherwise it will return HTTP code `500 Internal Server Error`. Returns HTTP code `200 OK` on success.

### `GET /posts/<id>`

Returns the specified post if it exists, otherwise returns HTTP code `404 Not Found`.

### `PUT /posts/<id>`

Updates the specified post if it exists, otherwise returns HTTP code `404 Not Found`. Can give it a `message`, `latitude`, and `longitude`. You only need to give it the values you are updating. Returns HTTP code `200 OK`.

### `DELETE /posts/<id>`

Deletes the specified post if it exists, otherwise returns HTTP code `404 Not Found`. Returns HTTP code `200 OK` on success.
