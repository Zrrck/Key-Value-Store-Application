## Start App (default port 3000)
```
./app
```
### API
```
-GET /keys 
   - Returns 200 if empty returns empty {} with 200
-DELETE /keys 
   - Returns 200 if empty returns 204
-PUT /keys 
   - Returns 201
-GET /keys/{id} 
   - Returns 200 else 404
-HEAD /keys/{id}
   - Returns 200 else 404
-DELETE /keys/{id}
   - Returns 200 else 500
```
### Usage
```
# put "value" in key "key"
- PUT /keys
   - curl -X PUT -d "key:value" http://localhost:3000/keys

# get all keys and value (should return json {"key":"value"})
- GET /keys
   - curl -X GET  http://localhost:3000/keys

# delete all keys
- DELETE /keys
   - curl -X DELETE  http://localhost:3000/keys

# get key "key" (should return "value")
- GET /keys/{id}
   - curl -X GET  http://localhost:3000/keys/

# check key exist
- HEAD /keys/{id}
   - curl -X HEAD  http://localhost:3000/keys/key

# delete key "key"
- DELETE /keys/{id}
   - curl -X DELETE  http://localhost:3000/keys/key
```
