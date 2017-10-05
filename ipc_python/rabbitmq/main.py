# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import

from ipc_python import logger, rabbitmq, p_title

if __name__ == '__main__':
    p_title('RabbitMQ')
    logger.info('add(2, 2) =')
    logger.info('{}'.format(rabbitmq.tasks.add(2, 2)))
    logger.info('add_slow_and_lazy(2, 2) =')
    logger.info('{}'.format(rabbitmq.tasks.add_slow_and_lazy(2, 2)))
    async_result = rabbitmq.tasks.add.delay(2, 2)
    logger.info('add.delay(2, 2) =')
    logger.info('{}'.format(async_result))
    logger.info('async_result =')
    logger.info(async_result.get())

