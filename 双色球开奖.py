#!/user/bin/env python3
# -*-coding: utf-8-*-

# @Time: 7/19/21 4:44 PM
# @Author: lifelong learner
# @Email:  19554102@qq.com
# @File: 双色球开奖.py

"""
编写一个小程序，模拟实现双色球开奖，摇出6个红色球号码和1个蓝色球号码，每个号码都是双数，例如9记为09，范围如下
红球：从1号到33号共33个数字
篮球：从1号到16号共16个数字
"""
import random


class Lottery(object):
    def __init__(self, reds_pool, blues_pool, draw_result=None):
        self.reds_pool = reds_pool
        self.blues_pool = blues_pool
        if draw_result is None:
            draw_result = []
        self.draw_result = draw_result

    def gen_balls(self):
        self.draw_result.clear()
        red_balls = sorted(random.sample(self.reds_pool, 6))
        for ball in red_balls:
            if len(str(ball)) == 1:
                ball = '0' + str(ball)
            else:
                ball = str(ball)
            self.draw_result.append(ball)
        blue_ball = random.choice(self.blues_pool)
        if len(str(blue_ball)) == 1:
            blue_ball = '0' + str(blue_ball)
        else:
            blue_ball = str(blue_ball)
        # self.draw_result.append(blue_ball)
        return ' '.join(self.draw_result), blue_ball

    def show_result(self):
        red, blue = self.gen_balls()
        print(f'本期双色球中奖号码: \n{red}  {blue}')


if __name__ == '__main__':
    red_pool = list(range(1, 34))
    blue_pool = list(range(1, 17))
    lottery = Lottery(red_pool, blue_pool)
    lottery.show_result()
