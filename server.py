"""Snake Environment Server"""

from openreward.environments import Server

from env import SnakeEnvironment

if __name__ == "__main__":
    server = Server([SnakeEnvironment])
    server.run()
