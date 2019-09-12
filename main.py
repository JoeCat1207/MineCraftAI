import minerl
import gym
import logging

env = None 
def main():
    print("Started Logging")
    logging.basicConfig(level=logging.DEBUG)
    print("Environment Starting")
    env = gym.make('MineRLNavigateDense-v0')
    obs = env.reset
    doAction(False)

def doAction(bool):
    done = bool
    while not done:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)

if __name__ == "__main__" :
    main()
    

