from .motor_chain_robot import get_yam_robot

if __name__ == "__main__":
    import argparse
    import time

    args = argparse.ArgumentParser()
    args.add_argument("--channel", type=str, default="can0")
    args = args.parse_args()

    robot = get_yam_robot(args.channel)

    while True:
        robot.zero_torque_mode()
        obs = robot.get_observations() 
        print(obs)