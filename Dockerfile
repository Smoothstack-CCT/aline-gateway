FROM openjdk@sha256:77a5473ddb0c020e1ed7613a3454bb7106ca546e4eac3fab3dab411e288ba8d3
COPY target/aline-gateway-*.jar app.jar
ENTRYPOINT [ "java", "-jar", "app.jar" ]