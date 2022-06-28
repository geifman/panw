Build image
-----------
docker build -t alexg -f Dockerfile .

Create container
---------------
docker run -d --rm --name geifman alexg

Connect to container
--------------------
docker exec -it geifman /bin/bash

Run tests
---------
python3 -m pytest .
