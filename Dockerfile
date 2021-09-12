FROM openjdk:8-jdk-alpine
ENV APP_PORT=8080
EXPOSE $APP_PORT
COPY target/aline-gateway-0.0.1-SNAPSHOT.jar app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]
