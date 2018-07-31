spring:
  redis:
      host: localhost
      port: 6379
      password:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/table?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true
    username: root
    password: 123456
    type: com.alibaba.druid.pool.DruidDataSource
  application:
    name: {{module}}-soa-service
