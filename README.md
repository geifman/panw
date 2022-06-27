Image build instructions
------------------------
1. Copy Model and Tests folder to /tmp

docker build -t alexg -f Dockerfile .
docker run --name geifman -it --rm alexg &
docker exec -it geifman /bin/bash
cd Tests
python3 -m pytest .
