FROM python
RUN pip install pytest requests
WORKDIR /usr/src/homework
COPY homework .
COPY twtask .
RUN chmod +x twtask
ENTRYPOINT ["/bin/bash", "-c", "./twtask"]
