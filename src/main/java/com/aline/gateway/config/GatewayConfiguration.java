package com.aline.gateway.config;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.GatewayFilterSpec;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.cloud.gateway.route.builder.UriSpec;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.function.Function;
import java.util.stream.Collectors;

@Configuration
@Slf4j
@RequiredArgsConstructor
public class GatewayConfiguration {

    private final GatewayConfigurationProperties gatewayProperties;

    @Bean
    public RouteLocator routeLocator(RouteLocatorBuilder builder) {
        RouteLocatorBuilder.Builder routes = builder.routes();

        final String pathPrefix = gatewayProperties.getPathPrefix();
        final String serviceHost = gatewayProperties.getServiceHost();

        final Function<GatewayFilterSpec, UriSpec> rewritePath = r -> r.rewritePath(pathPrefix + "/(?<segment>.*)", "/${segment}");

        gatewayProperties.getRoutes().forEach(route -> routes.route(route.getId(),
                r -> r.path(route.getPaths().stream().map(path -> path.replace("@", pathPrefix))
                                    .collect(Collectors.toList())
                                    .toArray(new String[0]))
                        .filters(rewritePath)
                        .uri(serviceHost + ":" + route.getPort())
                )
        );

        return routes.build();
    }

}
