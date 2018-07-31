package com.weimob.{{module}}.{{project}}.adapter;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.boot.autoconfigure.jdbc.DataSourceTransactionManagerAutoConfiguration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.web.bind.annotation.*;


@SpringBootApplication
@EnableAspectJAutoProxy(proxyTargetClass = true)
@EnableAutoConfiguration(exclude = {DataSourceAutoConfiguration.class
		, DataSourceTransactionManagerAutoConfiguration.class})
@RestController
public class {{ModuleProject}}AdapterApplication {

	@GetMapping("test")
	public String test(){
		return "hello";
	}

	public static void main(String[] args) {
		SpringApplication.run({{ModuleProject}}AdapterApplication.class, args);
	}
}
