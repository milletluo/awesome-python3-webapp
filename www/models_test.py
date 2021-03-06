#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'milletluo'

import orm, asyncio, sys
from models import User, Blog, Comment

async def test():
    await orm.create_pool(loop = loop, user='www-data', password='www-data', db='awesome')
    #往User数据表中插入数据，注意：已插入的输出重复插入会报错
    #u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    #await u.save()
    uu = User(name='milletluotest', email='milletluo@example.com', passwd='1234', image='about:blank')
    await uu.save()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
    loop.close()
    if loop.is_closed():
        sys.exit(0)
