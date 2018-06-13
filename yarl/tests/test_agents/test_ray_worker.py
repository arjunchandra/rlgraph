# Copyright 2018 The YARL-Project, All Rights Reserved.
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
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

from yarl import set_distributed_backend


class TestRayWorker(unittest.TestCase):

    env_spec = dict(
      type="openai",
      gym_env="CartPole-v0"
    )
    agent_config = dict(
        type="random"
    )

    def test_get_timesteps(self):
        """
        Simply tests if time-step execution loop works and returns the samples.
        """
        # Ensure Ray is set.
        set_distributed_backend(_distributed_backend="ray")
        from yarl.execution.ray import RayWorker

        worker = RayWorker(
            env_spec=self.env_spec,
            agent_config=self.agent_config,
        )

        # Test when breaking on terminal.
        result = worker.execute_and_get_timesteps(100, break_on_terminal=True)
        print(result)