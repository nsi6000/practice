FROM alpine:latest
#docker image build -t nsi6000:latest .
#docker run --rm -it nsi6000 bash

WORKDIR /github

COPY . /local

#Tools
RUN apk update
RUN apk add bash
RUN apk add vim
RUN apk add git
RUN apk add wget

#Clone git repos
RUN git clone https://github.com/nsi6000/practice.git
RUN git clone https://github.com/nsi6000/stacks.git

#C
RUN apk add gcc #compile linux kernel.
RUN apk add libc-dev #required to compile with GCC.
RUN apk add binutils #compile linux kernel.
RUN apk add make #compile linux kernel.
RUN apk add gdb
RUN apk add cppcheck #cppcheck <file>|<path>
RUN apk add indent #indent -kr|-linux <file>

#Python
RUN apk add python3
RUN apk add py3-pip #pip
RUN pip3 install Faker #faker
RUN pip3 install pylint #Linter
RUN pip3 install pytest
RUN pip3 install flake8 #Linter

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
#CMD ["python", "app.py"]
