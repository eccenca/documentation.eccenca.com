# Application logging with Logback

Logging for eccenca DataManager can also be configured with [Logback](https://logback.qos.ch/), which, for example, allows a more granular control of file rolling strategies. For further information on configuration options refer to the [Logback's Configuration](https://logback.qos.ch/manual/configuration.html) manual section and the Spring Boot's Configure Logback for logging manual section.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| logging.configuration | none | no | none | string (file path) |

Use this property to specify where the Logback configuration is located.

## Configuration example

``` yaml
logging:
  configuration: "${ELDS_HOME}/etc/datamanager/logback.xml"
```

The following example `logback.xml` file defines a rolling file strategy where files are rotated on a time base (1 day) with a limit of 7 files, which means that the logging files contain a log history of a maximum of 1 week.

``` yaml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <appender name="TIME_BASED_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>/opt/elds/var/log/datamanager.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
      <!-- daily rollover, history for 1 week -->
      <fileNamePattern>/opt/elds/var/log/datamanger.%d{yyyy-MM-dd}.log</fileNamePattern>
      <maxHistory>7</maxHistory>
    </rollingPolicy>
    <encoder>
      <pattern>%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n</pattern>
    </encoder>
  </appender>
  <logger name="com.eccenca" level="INFO">
    <appender-ref ref="TIME_BASED_FILE" />
  </logger>
</configuration>
```
