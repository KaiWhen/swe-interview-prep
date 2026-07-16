### What is a RESTful API?
An interface that two systems can exchange information securely over the internet.
It uses REST (Representational State Transfer) which is implemented with the HTTP protocol for data transfer.

### What are the HTTP methods?
GET, POST, PUT, DELETE, which are used to perform CRUD (create, read, update, delete) operations.

### What are the HTTP Status Codes?
- 1xx - represents informational responses
- 2xx - represents successful responses
- 3xx - represents redirects
- 4xx - represents client errors
- 5xx - represents server errors

Most commonly used status codes are:

- 200 - success/OK
- 201 - CREATED - used in POST or PUT methods.
- 304 - NOT MODIFIED - used in conditional GET requests to reduce the bandwidth use of the network. Here, the body of the response sent should be empty.
- 400 - BAD REQUEST - This can be due to validation errors or missing input data.
- 401- UNAUTHORIZED - This is returned when there is no valid authentication credentials sent along with the request.
- 403 - FORBIDDEN - sent when the user does not have access (or is forbidden) to the resource.
- 404 - NOT FOUND - Resource method is not available.
- 500 - INTERNAL SERVER ERROR - server threw some exceptions while running the method.
- 502 - BAD GATEWAY - Server was not able to get the response from another upstream server.

### What is statelessness in REST?
The server completes every client request independently of all previous requests. Basically, clients can request
resources in any order, and every request is stateless or isolated from other requests.
This helps remove load from the server.

### What is URI?
Uniform Resource Identifier is used for identifying each resource of the REST architecture.
For REST services, the server typically performs resource identification by using a Uniform Resource Locator (URL).

### CORS
Cross-Origin Resource Sharing is a browser security mechanism that blocks a webpage
from making requests to a different origin (different domain, protocol, or port)
unless that server explicitly allows it via response headers like Access-Control-Allow-Origin.
