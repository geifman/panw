FROM python
RUN pip install pytest requests
WORKDIR /usr/src/homework
COPY Homework .
COPY twtask .
ENTRYPOINT ["/bin/bash", "-c", "./twtask"]
