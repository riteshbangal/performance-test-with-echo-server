FROM openjdk:11-jre-slim

# Set the working directory in the container
WORKDIR /opt/gatling

# Copy Gatling script and resources
COPY EchoServerSimulation.scala /opt/gatling/user-files/simulations/

# Download Gatling bundle
RUN apt-get update
RUN apt-get install -y unzip
RUN apt-get install -y curl
RUN curl -L -o gatling.zip https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-highcharts-bundle/3.5.1/gatling-charts-highcharts-bundle-3.5.1-bundle.zip
RUN unzip gatling.zip && \
    rm gatling.zip && \
    mv gatling-charts-highcharts-bundle-3.5.1 gatling

# Add Gatling to the PATH
ENV PATH="/opt/gatling/gatling/bin:${PATH}"

# Execute Gatling when the container starts
CMD ["gatling.sh", "-s", "EchoServerSimulation"]
