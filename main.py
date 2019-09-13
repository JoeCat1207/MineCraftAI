import minerl
import gym
import logging
import threading
import action
import os

env = None 

def main():
    print("Started Logging")
    logging.basicConfig(level=logging.DEBUG)
    print("Environment Starting")
    trd = threading.Thread(target=action.baseStart())
    print("DONE")

if __name__ == "__main__":
    main()
    

