#!/usr/bin/env python3

import os
import random

want_to_play = True

# Keeps track of remaining questions. Also determines whether the game has ended.
m_list = []
p_list = []

# Returns a nicely formatted dotted decimal mask
def mask_maker(prefix):
    mask = []
    for i in range(4):
        mask.append(256 - (2 ** (8 - prefix)) if prefix < 8 else 255)
        prefix -= prefix if prefix < 8 else 8
    return '{}.{}.{}.{}'.format(*mask)


while want_to_play:
    try:
        # Mnu screen that appears once the game is started
        # and/or once the lists are empty (game is over).
        while not m_list and not p_list and want_to_play:
            os.system('clear')
            print(
                'Select one of the following options:\n'
                '\n'
                'm - Mask (you will be prompted for a prefix)\n'
                'p - Prefix (you will be prompted for a mask)\n'
                'r - Random\n'
                '\n'
                'You can enter \'q\' at any time to quit\n'
            )
            modeAnswer = input('Game mode: ')
            if modeAnswer in ('q', 'Q'):
                want_to_play = False
            elif modeAnswer in ('m', 'M'):
                m_list = list(range(0, 33))
            elif modeAnswer in ('p', 'P'):
                p_list = list(range(0, 33))
            elif modeAnswer in ('r', 'R'):
                m_list = list(range(0, 33))
                p_list = list(range(0, 33))

        # Max score is determined by game mode. Check if m_list AND p_list
        # are both NOT empty.
        #
        # TODO: Replace magic numbers
        if p_list and m_list:
            max_score = 66
        else:
            max_score = 33
        # Initial score
        score = 0

        # Game round loop
        while m_list or p_list:

            # The mode must be determined on a per-round basis to provide
            # the functionality of 'r' mode (random).
            if m_list and p_list:
                mode_mask = random.choice((True, False))
            else:
                mode_mask = bool(m_list)

            # Based on the mode, select a prefix for the round and then
            # remove it from the list.
            if mode_mask:
                round_prefix = random.choice(m_list)
                m_list.remove(round_prefix)
                # The question and answer must be formatted accordingly
                question = mask_maker(round_prefix)
                prompt = 'CIDR prefix: '
                correct_answer = str(round_prefix)
            else:
                round_prefix = random.choice(p_list)
                p_list.remove(round_prefix)
                # The mode is prefix for this round
                question = f'/{round_prefix}'
                prompt = 'Subnet mask: '
                correct_answer = mask_maker(round_prefix)

            # Clear the screen and prompt with question.
            os.system('clear')
            print(
                '\n'
                f'{len(m_list) + len(p_list)} questions remaining\n'
                '\n'
                f'{question}\n'
            )

            response = input(prompt)

            # Check to see if the player no longer wants to play.
            if response in ('q', 'Q'):
                want_to_play = False
                break

            if response == correct_answer:
                score += 1
                response = input('\nThat is correct!')
            else:
                response = input('\nSorry! Try again')

            # Check for 'q'/'Q' one more time before the next round.
            if response in ('q', 'Q'):
                want_to_play = False
                break

        # Tell player the final score (unless 'q'/'Q' was pressed).
        if want_to_play:
            os.system('clear')
            print(f'Score: {score}/{max_score}\n')
            input("Hit 'Enter' to continue (or just press it gently)")

    except KeyboardInterrupt:
        want_to_play = False

    finally:
        os.system('clear')
