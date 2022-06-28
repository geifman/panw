Build image
-----------
docker build -t alexg -f Dockerfile .

Create container
---------------
1. docker run -d --rm --name geifman alexg
2. docker exec -it geifman /bin/bash

Run tests
---------
python3 -m pytest .
