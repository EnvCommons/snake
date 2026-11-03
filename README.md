# Snake

[![OpenReward Environment](https://img.shields.io/badge/%E2%AD%90%20OpenReward-Environment-f7e6cc)](https://openreward.ai/GeneralReasoning/Snake)

## Description

**Snake** is an environment for evaluating agents on the classic multiplayer snake game. The agent plays a two-player game against an LLM opponent (gpt-5-mini). This environment wraps the Snake implementation from [TextArena](https://github.com/LeonGuertler/TextArena), a framework for text-based game environments.

## Capabilities

- Spatial navigation and path planning
- Collision avoidance with walls, trails, and opponents
- Turn-based strategic decision making
- Evaluation across multiple grid size variants

## Compute Requirements

Snake does not require a sandbox. It has minimal compute requirements.

## License

[MIT](https://opensource.org/licenses/MIT). TextArena itself is also released under MIT.

## Tasks

There are 450 tasks in the `train` split and 450 in `test`. Each split contains 50 tasks for each of 9 TextArena variants:

- **Snake-v0**
- **Snake-v0-large**
- **Snake-v0-large-raw**
- **Snake-v0-large-train**
- **Snake-v0-raw**
- **Snake-v0-standard**
- **Snake-v0-standard-raw**
- **Snake-v0-standard-train**
- **Snake-v0-train**

Each task is seeded for reproducibility: train uses seeds 0 to 49 and test uses seeds 10000 to 10049. The opponent is an LLM, so games are not fully deterministic.

## Reward Structure

This is a sparse reward environment with a single reward when the game ends (1.0 for a win, 0.5 for a draw, 0.0 for a loss). Rewards are mapped from TextArena's native range of {-1, 0, 1} to {0.0, 0.5, 1.0} via `(raw + 1) / 2`.

We do not use LLM graders for this environment; reward is determined programmatically by the game. The opponent snake is played by gpt-5-mini.

## Data

Game state is generated procedurally by the TextArena engine using seeded randomness. No external data files are required.

## Tools

Agents are given a single tool:

- `move(direction)`: Move your snake in the specified direction (up/down/left/right).

## Time Horizon

Snake is a multi-turn environment: one `move` call per turn until the game ends.

## Other Environment Requirements

This environment requires an OpenAI API key, passed as the `openai_api_key` secret, to power the LLM opponent.

## Safety

Agents in Snake interact only with a multiplayer game and have no access to external systems, the internet, or sensitive data. The environment does not present safety risks.

## Citations

```bibtex
@misc{guertler2025textarena,
    title={TextArena},
    author={Leon Guertler and Bobby Cheng and Simon Yu and Bo Liu and Leshem Choshen and Cheston Tan},
    year={2025},
    eprint={2504.11442},
    archivePrefix={arXiv},
    primaryClass={cs.CL},
    url={https://arxiv.org/abs/2504.11442},
}
```
