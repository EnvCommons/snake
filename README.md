# Snake

[![OpenReward Environment](https://img.shields.io/badge/%E2%AD%90%20OpenReward-Environment-f7e6cc)](https://openreward.ai/GeneralReasoning/Snake)

## Description

**Snake** is an environment for evaluating agents on the classic multiplayer snake game. This environment wraps the Snake implementation from [TextArena](https://github.com/LeonGuertler/TextArena), a framework for text-based game environments.

## Capabilities

- Spatial navigation and path planning
- Collision avoidance with walls, trails, and opponents
- Real-time strategic decision making
- Evaluation across multiple grid size variants

## Compute Requirements

Snake does not require a sandbox. It has minimal compute requirements.

## License

[MIT](https://github.com/LeonGuertler/TextArena/blob/main/LICENSE).

## Tasks

There are two splits: train (450 tasks) and test (450 tasks). Each split contains 50 tasks across each of 9 variants:

- **Snake-v0**
- **Snake-v0-large**
- **Snake-v0-large-raw**
- **Snake-v0-large-train**
- **Snake-v0-raw**
- **Snake-v0-standard**
- **Snake-v0-standard-raw**
- **Snake-v0-standard-train**
- **Snake-v0-train**

Each task is seeded for reproducibility.

## Reward Structure

This is a sparse reward environment. Rewards are mapped from TextArena's native range of {-1, 0, 1} to {0.0, 0.5, 1.0} via `(raw + 1) / 2`.

We do not use LLM graders for this environment; reward is determined programmatically.

## Data

Game state is generated procedurally by the TextArena engine using seeded randomness. No external data files are required.

## Tools

Agents are given a single tool:

- `move(direction)`: Move your snake in the specified direction (up/down/left/right).

## Time Horizon

Snake is a multi-turn environment.

## Environment Difficulty

Medium - requires spatial awareness and planning ahead.

## Other Environment Requirements

This environment requires an OpenAI API key (passed via secrets) to power the LLM opponent.

## Safety

Agents in Snake interact only with a multiplayer game and have no access to external systems, the internet, or sensitive data. The environment does not present safety risks.

## Citations

```bibtex
@software{textarena2024,
  author    = {Guertler, Leon and Banting, Wilfried and Pignatelli, Eduardo},
  title     = {TextArena},
  year      = {2024},
  publisher = {GitHub},
  url       = {https://github.com/LeonGuertler/TextArena}
}
```
