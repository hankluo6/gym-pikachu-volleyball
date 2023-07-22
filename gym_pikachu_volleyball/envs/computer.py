import random

from gym_pikachu_volleyball.envs.constants import *

def expected_landing_point_x_when_power_hit(self, userInputXDirection: int, userInputYDirection: int, ball) -> int:
    copy_ball = {
        'x': ball.x,
        'y': ball.y,
        'velocity_x': ball.x_velocity,
        'velocity_y': ball.y_velocity,
    }
    if copy_ball['x'] < GROUND_HALF_WIDTH:
        copy_ball['velocity_x'] = (abs(userInputXDirection) + 1) * 10
    else:
        copy_ball['velocity_x'] = -(abs(userInputXDirection) + 1) * 10

    copy_ball['velocity_y'] = abs(copy_ball['velocity_y']) * userInputYDirection * 2
    loopCounter: int = 0
    while True:
        loopCounter += 1

        futurecopy_ballX = copy_ball['x'] + copy_ball['velocity_x']
        if futurecopy_ballX < BALL_RADIUS or futurecopy_ballX > GROUND_WIDTH:
            copy_ball['velocity_x'] = -copy_ball['velocity_x']

        if copy_ball['y'] + copy_ball['velocity_y'] < 0:
            copy_ball['velocity_y'] = 1

        if abs(copy_ball['x'] - GROUND_HALF_WIDTH) < NET_PILLAR_HALF_WIDTH and copy_ball['y'] > NET_PILLAR_TOP_TOP_Y_COORD:
            if copy_ball['y'] <= NET_PILLAR_TOP_BOTTOM_Y_COORD:
                if copy_ball['velocity_y'] > 0:
                    copy_ball['velocity_y'] = -copy_ball['velocity_y']
            else:
                if copy_ball['x'] < GROUND_HALF_WIDTH:
                    copy_ball['velocity_x'] = -abs(copy_ball['velocity_x'])
                else:
                    copy_ball['velocity_x'] = abs(copy_ball['velocity_x'])

        copy_ball['y'] = copy_ball['y'] + copy_ball['velocity_y']

        if copy_ball['y'] > BALL_TOUCHING_GROUND_Y_COORD or loopCounter >= 1000:
            return copy_ball['x']

        copy_ball['x'] = copy_ball['x'] + copy_ball['velocity_x']
        copy_ball['velocity_y'] += 1

def decide_wheter_input_power_hit(self, player, ball, theOtherPlayer, userInput) -> bool:
    if random.randrange(0, 2) == 0:
        for xDirection in range(1, -1, -1):
            for yDirection in range(-1, 2):
                expectedLandingPointX = self.expected_landing_point_x_when_power_hit(xDirection, yDirection, ball)
                if (expectedLandingPointX <= int(player.is_player2) * GROUND_HALF_WIDTH or\
                    expectedLandingPointX >= int(player.is_player2) * GROUND_WIDTH + GROUND_HALF_WIDTH) and\
                    abs(expectedLandingPointX - theOtherPlayer.x) > PLAYER_LENGTH:
                        userInput.x_direction = xDirection
                        userInput.y_direction = yDirection
                        return True
    else:
        for xDirection in range(1, -1, -1):
            for yDirection in range(1, -2, -1):
                expectedLandingPointX = self.expected_landing_point_x_when_power_hit(xDirection, yDirection, ball)
                if (expectedLandingPointX <= int(player.is_player2) * GROUND_HALF_WIDTH or\
                    expectedLandingPointX >= int(player.is_player2) * GROUND_WIDTH + GROUND_HALF_WIDTH) and\
                    abs(expectedLandingPointX - theOtherPlayer.x) > PLAYER_LENGTH:
                        userInput.x_direction = xDirection
                        userInput.y_direction = yDirection
                        return True
    return False

def calculate_expected_landing_point_x_for(self, ball):
    copy_ball = {
        'x': ball.x,
        'y': ball.y,
        'velocity_x': ball.x_velocity,
        'velocity_y': ball.y_velocity,
    }
    loopCounter: int = 0
    while True:
        loopCounter += 1

        future_copy_ball_x: int = copy_ball['velocity_x'] + copy_ball['x']
        if future_copy_ball_x < BALL_RADIUS or future_copy_ball_x > GROUND_WIDTH:
            copy_ball['velocity_x'] = -copy_ball['velocity_x']
        if copy_ball['y'] + copy_ball['velocity_y'] < 0:
            copy_ball['velocity_y'] = 1

        if abs(copy_ball['x'] - GROUND_HALF_WIDTH) < NET_PILLAR_HALF_WIDTH and copy_ball['y'] > NET_PILLAR_TOP_TOP_Y_COORD:
            if copy_ball['y'] < NET_PILLAR_TOP_BOTTOM_Y_COORD:
                if copy_ball['velocity_y'] > 0:
                    copy_ball['velocity_y'] = -copy_ball['velocity_y']
            else:
                if copy_ball['x'] < GROUND_HALF_WIDTH:
                    copy_ball['velocity_x'] = -abs(copy_ball['velocity_x'])
                else:
                    copy_ball['velocity_x'] = abs(copy_ball['velocity_x'])
        
        copy_ball['y'] = copy_ball['y'] + copy_ball['velocity_y']

        if copy_ball['y'] > BALL_TOUCHING_GROUND_Y_COORD or loopCounter >= 1000:
            break

        copy_ball['x'] = copy_ball['x'] + copy_ball['velocity_x']
        copy_ball['velocity_y'] += 1

    ball.expected_landing_point_x = copy_ball['x']