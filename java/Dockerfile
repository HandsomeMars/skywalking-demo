FROM openjdk:8-jdk-alpine
ENV LANG=C.UTF-8
RUN set -eux && mkdir -p /opt/skywalking/agent/
ADD agent/ /opt/skywalking/agent/
VOLUME /tmp
ARG JAR_FILE
COPY ${JAR_FILE} app.jar
ENTRYPOINT java -javaagent:/opt/skywalking/agent/skywalking-agent.jar \
-Dskywalking.agent.service_name=$APP_ID \
-Dskywalking.collector.backend_service=$SKYWALKING_ADDR -jar app.jar