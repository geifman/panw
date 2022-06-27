Build image
-----------
1. Copy/dowload project
2. docker build -t alexg -f Dockerfile .

Create container
---------------
1. docker run --name geifman -it --rm alexg &
2. docker exec -it geifman /bin/bash

Run tests
---------
1. cd homework
2. python3 -m pytest .
