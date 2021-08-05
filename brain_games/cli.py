#!/usr/bin/python3.9
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name, end='')
    print('!')
