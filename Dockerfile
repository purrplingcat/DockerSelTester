FROM ubuntu:trusty

MAINTAINER "Ellen Fawkes <fawkes@ttc.cz>"

ENV TEST_DIR="/tests"
ENV REPORT_DIR="/report"
ENV SCREEN_DIR="/report/screenshots"
ENV DEBUG=0

RUN echo "deb http://ppa.launchpad.net/mozillateam/firefox-next/ubuntu trusty main" > /etc/apt/sources.list.d//mozillateam-firefox-next-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CE49EC21
RUN apt-get update
RUN apt-get install -y firefox xvfb python-pip wget zip unzip libnss3 libnspr4 libgconf-2-4

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && apt-get update && apt-get install -y google-chrome-stable

# Install Gecko (firefox) driver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz -O - | tar zxf - -C /usr/bin
# Install Chrome driver
RUN wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip -O /tmp/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver_linux64.zip -d /usr/bin

RUN pip install selenium
RUN pip install custom_text_test_runner
RUN mkdir -p ${TEST_DIR}
RUN mkdir -p ${REPORT_DIR} && mkdir -p ${SCREEN_DIR}

# COPY ./tests ${TEST_DIR}
ADD ./src/etc/xvfb.init /etc/init.d/xvfb

ADD ./src/init.sh /
COPY ./src/bin /usr/local/bin
COPY ./src/lib /usr/lib/python2.7

RUN chmod +x /etc/init.d/xvfb
RUN chmod +x /usr/local/bin/*
RUN chmod +x /init.sh
RUN update-rc.d xvfb defaults

VOLUME ${TEST_DIR}
VOLUME ${REPORT_DIR}

WORKDIR /

ENTRYPOINT [ "./init.sh" ]
CMD [ "do_all_tests", "--report" ]
