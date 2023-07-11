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

import jax.numpy as jnp

# Actions
MOVES = jnp.array([[-1, 0], [0, 1], [1, 0], [0, -1]])  # Up, Right, Down, Left

# Minecraft blocks
AIR = 0
STEVE = 1
WOODEN_LOG = 2
COBBLESTONE = 3
IRON_ORE = 4
DIAMOND_ORE = 5
