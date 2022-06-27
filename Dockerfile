FROM python
RUN pip install pytest requests
WORKDIR /tmp
COPY PycharmProjects/pythonProject .
COPY twtask .
ENTRYPOINT ["/bin/bash", "-c", "./twtask"]