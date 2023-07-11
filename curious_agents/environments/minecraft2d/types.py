# Copyright 2022 InstaDeep Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:  # https://github.com/python/mypy/issues/6239
    from dataclasses import dataclass
else:
    from chex import dataclass

import chex
import jax.numpy as jnp


class Position(NamedTuple):
    row: jnp.int32
    col: jnp.int32

    def __eq__(self, other: object) -> chex.Array:
        if not isinstance(other, Position):
            return NotImplemented
        return (self.row == other.row) & (self.col == other.col)


@dataclass
class State:
    """
    agent_position: current 2D Position of agent.
    agent_level: current level of agent.
    map: array (bool) whose values are `True` where map are and `False` for empty cells.
    action_mask: array specifying which directions the agent can move in from its current position.
    level_step_count: (int32) step number of the episode.
    key: random key used for auto-reset.
    """

    agent_position: Position  # Position(row, col) each of shape ()
    agent_level: jnp.int32  # ()
    map: chex.Array  # (num_rows, num_cols)
    action_mask: chex.Array  # (4,)
    level_step_count: jnp.int32  # ()
    key: chex.PRNGKey  # (2,)


class Observation(NamedTuple):
    """The Minecraft2D observation that the agent sees.

    map: array (bool) whose values are `True` where map are and `False` for empty cells.
    action_mask: array specifying which directions the agent can move in from its current position.
    level_step_count: (int32) step number of the episode.
    agent_level: current level of agent.
    """
    map: chex.Array  # (num_rows, num_cols)
    action_mask: chex.Array  # (4,)
    level_step_count: jnp.int32  # ()
    agent_level: jnp.int32  # ()

