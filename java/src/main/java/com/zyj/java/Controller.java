package com.zyj.java;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;


@RestController
public class Controller {

    final Logger logger = LoggerFactory.getLogger(Controller.class);

    @GetMapping
    public void hello(HttpServletResponse response, HttpServletRequest request) throws IOException, ServletException {
        logger.info("hello");
        RequestDispatcher requestDispatcher =request.getRequestDispatcher("http://127.0.0.1:8089");
        requestDispatcher.forward(request,response);
    }

}
