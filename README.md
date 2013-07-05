geopost
=======

Functions
---------

### `GET /posts`

Either:
- Returns and list of all posts.
- Returns a list of all posts within a `distance` of [`curr_latitude`,
  `curr_longitude`].

### `POST /posts`

Creates a new post. *Must* give it a `message`, `longitude`, and `latitude`
otherwise it will return HTTP code `500 Internal Server Error`. Returns HTTP
code `200 OK` on success.

### `GET /posts/<id>`

Returns the specified post if it exists, otherwise returns HTTP code `404 Not
Found`.
