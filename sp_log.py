#!/usr/bin/env python3

# -*- coding: utf-8 -*-


class SpLog:
    def __init__(self, path):
        self.f = open(path, 'w')

    def info(self, msg):
        self.f.write(msg)
        print(msg)

    @staticmethod
    def get_ins(path: str):
        """
        单例模式
        :param path:
        :return:
        """

        # TODO 完成单例模式代码
        log = SpLog(path)

        return log
