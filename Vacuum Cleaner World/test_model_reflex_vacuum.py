# DO NOT MODIFY THE CODE WITHIN EACH TEST
# Run me via: python3 -m unittest test_model_reflex_vacuum

import unittest
from unittest.mock import MagicMock
import time
from location import Location
from state import State
from movement_model import MovementModel
from transition_model import TransitionModel
from sensor_model import SensorModel
from model_reflex_vacuum import ModelReflexVacuum


class TestModelReflexVacuum(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A ModelReflexVacuum exists.
        """
        try:
            ModelReflexVacuum(None, None, None)
        except NameError:
            self.fail("Could not instantiate ModelReflexVacuum")

    """
    Attributes
    """

    def test_state(self):
        """
        A ModelReflexVacuum has state.
        """
        vacuum = ModelReflexVacuum('Fake State', None, None)
        self.assertEqual('Fake State', vacuum.state)

    def test_transition_model(self):
        """
        A ModelReflexVacuum has a transition_model.
        """
        vacuum = ModelReflexVacuum(None, 'Fake Transition Model', None)
        self.assertEqual('Fake Transition Model', vacuum.transition_model)

    def test_sensor_model(self):
        """
        A ModelReflexVacuum has a sensor_model.
        """
        vacuum = ModelReflexVacuum(None, None, 'Fake Sensor Model')
        self.assertEqual('Fake Sensor Model', vacuum.sensor_model)

    def test_most_recent_action(self):
        """
        A ModelReflexVacuum has a most_recent_action.
        """
        vacuum = ModelReflexVacuum('Fake State', 'Fake Transition Model', 'Fake Sensor Model')
        self.assertEqual(None, vacuum.most_recent_action)

    """
    Actuators
    """

    def test_suck(self):
        """
        A ModelReflexVacuum can `suck`. But the `suck` action delegates to the
        transition model `apply_suction` method.
        """
        mock_transition_model = TransitionModel(None, None)
        mock_transition_model.apply_suction = MagicMock()
        vacuum = ModelReflexVacuum(None, mock_transition_model, None)
        vacuum.suck()
        mock_transition_model.apply_suction.assert_called()

    def test_suck_returns_nothing(self):
        """
        The `suck` method does not return a value.
        """
        mock_transition_model = TransitionModel(None, None)
        mock_transition_model.apply_suction = MagicMock()
        vacuum = ModelReflexVacuum(None, mock_transition_model, None)
        self.assertIsNone(vacuum.suck())

    def test_move_left(self):
        """
        A ModelReflexVacuum can `move_left`. But, the `move_left` action delegates
        to the transition model `movel_left` method.
        """
        mock_transition_model = TransitionModel(None, None)
        mock_transition_model.move_left = MagicMock()
        vacuum = ModelReflexVacuum(None, mock_transition_model, None)
        vacuum.move_left()
        mock_transition_model.move_left.assert_called()

    def test_move_left_returns_nothing(self):
        """
        The `move_left` method does not return a value.
        """
        mock_transition_model = TransitionModel(None, None)
        mock_transition_model.move_left = MagicMock()
        vacuum = ModelReflexVacuum(None, mock_transition_model, None)
        self.assertIsNone(vacuum.move_left())

    def test_move_right(self):
        """
        A ModelReflexVacuum can `move_right`. But, the `move_right` action delegates
        to the transition model `movel_right` method.
        """
        mock_transition_model = TransitionModel(None, None)
        mock_transition_model.move_right = MagicMock()
        vacuum = ModelReflexVacuum(None, mock_transition_model, None)
        vacuum.move_right()
        mock_transition_model.move_right.assert_called()

    def test_move_right_returns_nothing(self):
        """
        The `move_right` method does not return a value.
        """
        mock_transition_model = TransitionModel(None, None)
        mock_transition_model.move_right = MagicMock()
        vacuum = ModelReflexVacuum(None, mock_transition_model, None)
        self.assertIsNone(vacuum.move_right())

    """
    Update state
    """

    def test_update_state_without_recent_action(self):
        """
        Updating the state when there is no recent action to apply does not
        cause any actuator method to execute, nor invoke any transition model
        methods.
        """
        mock_transition_model = TransitionModel(None, None)
        mock_transition_model.apply_suction = MagicMock()
        mock_transition_model.move_left = MagicMock()
        mock_transition_model.move_right = MagicMock()
        vacuum = ModelReflexVacuum(None, mock_transition_model, None)
        vacuum.suck = MagicMock()
        vacuum.move_left = MagicMock()
        vacuum.move_right = MagicMock()
        self.assertIsNone(vacuum.most_recent_action)
        vacuum.update_state()
        vacuum.suck.assert_not_called()
        vacuum.move_left.assert_not_called()
        vacuum.move_right.assert_not_called()
        mock_transition_model.apply_suction.assert_not_called()
        mock_transition_model.move_left.assert_not_called()
        mock_transition_model.move_right.assert_not_called()

    def test_update_state_with_recent_action_suck(self):
        """
        Updating the state when the recent action is `suck` should invoke the
        `suck` actuator method.
        """
        vacuum = ModelReflexVacuum(None, None, None)
        vacuum.suck = MagicMock()
        vacuum.most_recent_action = vacuum.suck
        vacuum.update_state()
        vacuum.suck.assert_called()

    def test_update_state_with_recent_action_move_left(self):
        """
        Updating the state when the recent action is `move_left` should invoke the
        `move_left` actuator method.
        """
        vacuum = ModelReflexVacuum(None, None, None)
        vacuum.move_left = MagicMock()
        vacuum.most_recent_action = vacuum.move_left
        vacuum.update_state()
        vacuum.move_left.assert_called()

    def test_update_state_with_recent_action_move_right(self):
        """
        Updating the state when the recent action is `move_right` should invoke the
        `move_right` actuator method.
        """
        vacuum = ModelReflexVacuum(None, None, None)
        vacuum.move_right = MagicMock()
        vacuum.most_recent_action = vacuum.move_right
        vacuum.update_state()
        vacuum.move_right.assert_called()

    """
    Agent function
    """

    def test_action_should_invoke_update_state(self):
        """
        The agent function should update the world state via `update_state`.
        """
        mock_sensor_model = SensorModel(None)
        mock_sensor_model.sense_dirt = MagicMock()
        mock_sensor_model.sense_location_id = MagicMock()
        vacuum = ModelReflexVacuum(None, None, mock_sensor_model)
        vacuum.update_state = MagicMock()
        action = vacuum.action()
        vacuum.update_state.assert_called()

    def test_action_when_sensing_dirt_is_suck(self):
        """
        The agent function should return the `suck` action if it senses dirt.
        """
        mock_sensor_model = SensorModel(None)
        mock_sensor_model.sense_dirt = MagicMock(return_value=True)
        vacuum = ModelReflexVacuum(None, None, mock_sensor_model)
        self.assertIsNone(vacuum.most_recent_action)
        action = vacuum.action()
        self.assertEqual(vacuum.suck, action)

    def test_action_when_in_clean_location_a_is_move_right(self):
        """
        The agent function should return the `move_right` action if it does not
        sense dirt and senses that it is in location A.
        """
        mock_sensor_model = SensorModel(None)
        mock_sensor_model.sense_dirt = MagicMock(return_value=False)
        mock_sensor_model.sense_location_id = MagicMock(return_value='A')
        vacuum = ModelReflexVacuum(None, None, mock_sensor_model)
        self.assertIsNone(vacuum.most_recent_action)
        action = vacuum.action()
        self.assertEqual(vacuum.move_right, action)

    def test_action_when_in_clean_location_b_is_move_left(self):
        """
        The agent function should return the `move_left` action if it does not
        sense dirt and senses that it is in location B.
        """
        mock_sensor_model = SensorModel(None)
        mock_sensor_model.sense_dirt = MagicMock(return_value=False)
        mock_sensor_model.sense_location_id = MagicMock(return_value='B')
        vacuum = ModelReflexVacuum(None, None, mock_sensor_model)
        self.assertIsNone(vacuum.most_recent_action)
        action = vacuum.action()
        self.assertEqual(vacuum.move_left, action)

    """
    End-to-End Testing
    """

    def test_first_action_starting_at_dirty_a(self):
        """
        When A has dirt and the vacuum starts in location A, the action is suck.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'A')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        sensor_model = SensorModel(vacuum_world)
        vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)
        self.assertEqual(vacuum.suck, vacuum.action())

    def test_first_action_starting_at_clean_a(self):
        """
        When A has no dirt and the vacuum starts in location A, the action is move_right.
        """
        vacuum_world = State({'A': Location('A', None), 'B': Location('B', True)}, 'A')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        sensor_model = SensorModel(vacuum_world)
        vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)
        self.assertEqual(vacuum.move_right, vacuum.action())

    def test_first_action_starting_at_dirty_b(self):
        """
        When B has dirt and the vacuum starts in location B, the action is suck.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'B')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        sensor_model = SensorModel(vacuum_world)
        vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)
        self.assertEqual(vacuum.suck, vacuum.action())

    def test_first_action_starting_at_clean_b(self):
        """
        When A has no dirt and the vacuum starts in location A, the action is move_right.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', None)}, 'B')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        sensor_model = SensorModel(vacuum_world)
        vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)
        self.assertEqual(vacuum.move_left, vacuum.action())

    def test_five_actions_in_a_dirty_world_starting_at_a(self):
        """
        When A and B both have dirt and the vacuum starts in location A, the action
        sequence is suck, right, suck, left, right.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'A')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        sensor_model = SensorModel(vacuum_world)
        vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)
        self.assertEqual(vacuum.suck, vacuum.action())
        self.assertEqual(vacuum.move_right, vacuum.action())
        self.assertEqual(vacuum.suck, vacuum.action())
        self.assertEqual(vacuum.move_left, vacuum.action())
        self.assertEqual(vacuum.move_right, vacuum.action())

    def test_five_actions_in_a_dirty_world_starting_at_b(self):
        """
        When A and B both have dirt and the vacuum starts in location B, the action
        sequence is suck, left, suck, right, left.
        """
        vacuum_world = State({'A': Location('A', True), 'B': Location('B', True)}, 'B')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        sensor_model = SensorModel(vacuum_world)
        vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)
        self.assertEqual(vacuum.suck, vacuum.action())
        self.assertEqual(vacuum.move_left, vacuum.action())
        self.assertEqual(vacuum.suck, vacuum.action())
        self.assertEqual(vacuum.move_right, vacuum.action())
        self.assertEqual(vacuum.move_left, vacuum.action())

    def test_five_actions_in_a_clean_world_starting_at_a(self):
        """
        When neither A nor B have dirt and the vacuum starts in location A, the action
        sequence is right, left, right, left, right.
        """
        vacuum_world = State({'A': Location('A', None), 'B': Location('B', None)}, 'A')
        movements = {'A': MovementModel('A', 'B'), 'B': MovementModel('A', 'B')}
        transition_model = TransitionModel(vacuum_world, movements)
        sensor_model = SensorModel(vacuum_world)
        vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)
        self.assertEqual(vacuum.move_right, vacuum.action())
        self.assertEqual(vacuum.move_left, vacuum.action())
        self.assertEqual(vacuum.move_right, vacuum.action())
        self.assertEqual(vacuum.move_left, vacuum.action())
        self.assertEqual(vacuum.move_right, vacuum.action())


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
