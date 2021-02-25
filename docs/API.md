# Server Api and request available
|URL|METHOD|ARGS EXAMPLE(json)|DESCRIPTION|
|---|---|---|---
|`/api/in/scanner`|GET|NA|Get all ip waiting for scan
|`/api/in/scanned`|GET|NA|Get all ip scanned with result
|`/api/ip`|POST|{"ip": "192.168.1.1/24"}|Add ip or ip range to scanner queues
|`/api/ip/get`|GET|NA|*for client* get ip to scan and remove from waiting
> more option in future