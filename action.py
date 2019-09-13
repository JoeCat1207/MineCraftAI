import minerl
import gym
import logging

obs = None
env = None


def doAction(name):
    if name == "walk":
        logging.info("Started: ")
    if name == "mine":
        logging.info("Started: ")
    if name == "jump":
        logging.info("Started: ")
    if name == "hit":
        logging.info("Started: ")
    if name == "shoot":
        logging.info("Started: ")
    if name == "find":
        logging.info("Started: ")

def baseStart():
    env = gym.make('MineRLTesting-v0')
    
    obs = env.reset()
    done = False

    while not done:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)

def mine():
    logging.info("Finished Mining")

def walk():
    logging.info("Finished Walking")

def jump():
    logging.info("Finished Jumping")

def hit():
    logging.info("Finished Hitting")

def shoot():
    logging.info("Finished Shooting")

def find():
    logging.info("Finished Search")