FROM openjdk@sha256:ec2ac33dcbd1f392a6594765f55f64272a8c7353b2748872c933d56ae5f66ed6
COPY target/aline-gateway-*.jar app.jar
ENTRYPOINT [ "java", "-jar", "app.jar" ]