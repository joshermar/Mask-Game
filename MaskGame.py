#!/usr/bin/env python3

import os
import random

want_to_play = True
m_possibilities = []
p_possibilities = []


# This will turn a numeric prefix into a nicely formatted dotted decimal mask.
def mask_maker(prefix):
    mask = [0, 0, 0, 0]
    for i in range(4):
        if prefix > 8:
            mask[i] = 255
            prefix -= 8
        else:
            mask[i] = 256 - 2 ** (8 - prefix)
            break
    return '{}.{}.{}.{}'.format(mask[0], mask[1], mask[2], mask[3])


while want_to_play:
    # I guess you could consider this the "menu screen". Should show up at
    # the very beginning and again once there are no "possibilities" left
    # (once the game is over).
    while not m_possibilities and not p_possibilities:
        os.system('clear')
        print('Please select one of the following options:\n'
              '\n'
              'm - Mask (you will be prompted for a prefix)\n'
              'p - Prefix (you will be prompted for a mask)\n'
              'r - Random\n'
              '\n'
              'You can enter \'q\' at any time to quit\n')
        modeAnswer = input('')
        if modeAnswer == 'q' or modeAnswer == 'Q':
            want_to_play = False
            break
        elif modeAnswer == 'm' or modeAnswer == 'M':
            m_possibilities = list(range(0, 33))
        elif modeAnswer == 'p' or modeAnswer == 'P':
            p_possibilities = list(range(0, 33))
        elif modeAnswer == 'r' or modeAnswer == 'R':
            m_possibilities = list(range(0, 33))
            p_possibilities = list(range(0, 33))

    # This is for keeping score
    max_score = len(m_possibilities) + len(p_possibilities)
    score = 0

    # This is the main game loop.
    while m_possibilities or p_possibilities:

        # We wanna select the right mode bassed on the pressence of one or
        # both of those lists up there, and if the mode is 'r' (meaning both
        # lists are not empty) we want to only use one at a time.
        if m_possibilities and p_possibilities:
            mode_mask = bool(random.choice([True, False]))
        elif m_possibilities:
            mode_mask = True
        else:
            mode_mask = False

        # This will determine the right question and answer based on the
        # current game mode
        if mode_mask:
            print('Mask mode!')
            round_prefix = random.choice(m_possibilities)
            m_possibilities.remove(round_prefix)

            question = mask_maker(round_prefix)
            questionPrompt = 'CIDR prefix: '
            answer = str(round_prefix)
        else:
            print('Prefix mode!')
            round_prefix = random.choice(p_possibilities)
            p_possibilities.remove(round_prefix)
            question = '/' + str(round_prefix)
            questionPrompt = 'Subnet mask: '
            answer = mask_maker(round_prefix)

        # Just make some room and print out the question.
        os.system('clear')
        print('')
        print(str(len(m_possibilities) + len(p_possibilities)) +
              ' questions remaining')
        print('')
        print(question)
        print('')

        # The following input and control flow is pretty much the heart
        # of the game.
        response = input(questionPrompt)

        # Check for 'q' to see if the player no longer wants to play.
        if response == 'q' or response == 'Q':
            want_to_play = False
            break

        # You're either right or you're wrong. Or are you!? No time for
        # philosophy...
        if response == answer:
            score += 1
            print('')
            response = input('That is correct!')
        else:
            print('')
            response = input('Sorry! Try again')

        # Check for 'q' one more time before the next round.
        if response == 'q' or response == 'Q':
            want_to_play = False
            break

    # Tell player final score before starting new game or quiting.
    if want_to_play:
        os.system('clear')
        print('Score: {}/{}'.format(score, max_score))
        print('')
        input('Hit \'Enter\' to continue (or just press it gently)')
