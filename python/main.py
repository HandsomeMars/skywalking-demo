# -*- coding:utf-8 -*-
from time import sleep

from skywalking import Component
from skywalking.decorators import trace, runnable
from skywalking.trace.context import SpanContext, get_context
from skywalking.trace.ipc.process import SwProcess
config.init(collector='127.0.0.1|11801', service='py_demo')
config.flask_collect_http_params = True
agent.start()
from flask import Flask
app = Flask(__name__)

from skywalking import Component
from skywalking.trace.context import SpanContext, get_context
from skywalking.trace.tags import Tag

context: SpanContext = get_context()  # get a tracing context

@trace()  # the operation name is the method name('some_other_method') by default
def some_other_method():
    sleep(1)


@trace(op='awesome')  # customize the operation name to 'awesome'
def some_method():
    some_other_method()


@trace(op='async_functions_are_also_supported')
async def async_func():
    return 'asynchronous'


@trace()
async def async_func2():
    return await async_func()


@runnable() # cross thread propagation
def some_method():
    some_other_method()

from threading import Thread
t = Thread(target=some_method)
t.start()

# When another process is started, agents will also be started in other processes,
# supporting only the process mode of spawn.
p1 = SwProcess(target=some_method)
p1.start()
p1.join()


context: SpanContext = get_context()
with context.new_entry_span(op=str('https://github.com/apache/skywalking')) as span:
    span.component = Component.Flask
    some_method()


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8091)

