Image build instructions
------------------------
1. Copy Model and Tests folder to /tmp

3. docker build -t alexg -f Dockerfile .
4. docker run --name geifman -it --rm alexg &
5. docker exec -it geifman /bin/bash
6. cd Tests
7. python3 -m pytest .
