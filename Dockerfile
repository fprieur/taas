FROM ubuntu:14.04


# Install Python Setuptools
RUN apt-get update && apt-get upgrade -y
RUN apt-get install build-essential python-setuptools python-dev build-essential chrpath wget libssl-dev libxft-dev unzip python git -y
RUN easy_install pip

RUN apt-get install libfreetype6 libfreetype6-dev -y
RUN apt-get install libfontconfig1 libfontconfig1-dev -y

# Install phantomjs
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2 -P /home

RUN tar xvjf /home/phantomjs-1.9.7-linux-x86_64.tar.bz2
RUN mv phantomjs-1.9.7-linux-x86_64 /usr/local/share/
          
RUN ln -sf /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs
RUN ln -sf /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs
RUN ln -sf /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/bin/phantomjs

# Bundle app source
ADD . /home

# Expose
WORKDIR /home

# Install casperjs
RUN git clone https://github.com/n1k0/casperjs.git

RUN mv /home/casperjs /usr/local/share/casperjs-latest
         
RUN ln -sf /usr/local/share/casperjs-latest/bin/casperjs /usr/local/share/casperjs
RUN ln -sf /usr/local/share/casperjs-latest/bin/casperjs /usr/local/bin/casperjs
RUN ln -sf /usr/local/share/casperjs-latest/bin/casperjs /usr/bin/casperjs

RUN pip install -r requirements.txt

EXPOSE 5000

# Run
CMD python taas.py 
