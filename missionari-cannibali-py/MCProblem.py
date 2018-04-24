
import core.search as search


class MCProblem(search.Problem):

    POSSIBLE_ACTIONS = ['MC', 'MM', 'CC', 'M', 'C']
    POSSIBLE_MOVES = {
        POSSIBLE_ACTIONS[0]: (1, 1),
        POSSIBLE_ACTIONS[1]: (2, 0),
        POSSIBLE_ACTIONS[2]: (0, 2),
        POSSIBLE_ACTIONS[3]: (1, 0),
        POSSIBLE_ACTIONS[4]: (0, 1)
    }

    def __init__(self,
                 goal=(0, 0, 0),
                 max_missionars=3,
                 max_cannibals=3,
                 missionars=None,
                 cannibals=None,
                 side_ship=1):
        self.max_missionars = max_missionars
        self.max_cannibals = max_cannibals
        if missionars is None and cannibals is None:
            self.initial = (max_missionars, max_cannibals, side_ship)
        else:
            self.initial = (missionars, cannibals, side_ship)

        self.current_state = self.initial

        search.Problem.__init__(self, self.initial, goal)

    def actions(self, state):
        possible_actions = list(MCProblem.POSSIBLE_ACTIONS)

        if self.can_move_mc(state) is False:
            possible_actions.remove('MC')
        if self.can_move_mm(state) is False:
            possible_actions.remove('MM')
        if self.can_move_cc(state) is False:
            possible_actions.remove('CC')
        if self.can_move_m(state) is False:
            possible_actions.remove('M')
        if self.can_move_c(state) is False:
            possible_actions.remove('C')

        return possible_actions

    def result(self, state, action):
        new_state = (self.max_missionars, self.max_cannibals, 1)
        for single_action in self.POSSIBLE_ACTIONS:
            if single_action == action:
                new_state = self.set_new_state(state, self.POSSIBLE_MOVES[action][0], self.POSSIBLE_MOVES[action][1], state[2])

        return new_state

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return 1

    def h(self, node):
        hval = node.state[0] + node.state[1] - (node.state[2])
        return hval

    def set_current_state(self, state):
        if state[2]:
            self.current_state = (state[0], state[1], 0)
        else:
            self.current_state = (self.max_missionars - state[0], self.max_cannibals - state[1], 1)

    def set_new_state(self, current_state, missionars, cannibals, ship_side):
        if ship_side:
            new_state = (current_state[0] - missionars, current_state[1] - cannibals, 0)
            return new_state
        else:
            new_state = (current_state[0] + missionars, current_state[1] + cannibals, 1)
            return new_state

    def __str__(self):
        return str(self.initial)

    # POSSIBLE ACTION CHECKS

    def can_move_mc(self, state):
        self.set_current_state(state)
        num_missionars = self.current_state[0]
        num_cannibals = self.current_state[1]
        if ((num_missionars >= 1 and num_cannibals >= 1)
                and (num_missionars >= num_cannibals)
                and (self.max_missionars - num_missionars + 1 >= self.max_cannibals - num_cannibals + 1)):
            return True
        else:
            return False

    def can_move_mm(self, state):
        self.set_current_state(state)
        num_missionars = self.current_state[0]
        num_cannibals = self.current_state[1]
        if ((num_missionars >= 2)
                and (num_missionars == 2 or num_missionars - 2 >= num_cannibals)
                and (self.max_missionars - num_missionars + 2 >= self.max_cannibals - num_cannibals)):
            return True
        else:
            return False

    def can_move_cc(self, state):
        self.set_current_state(state)
        num_missionars = self.current_state[0]
        num_cannibals = self.current_state[1]
        if ((num_cannibals >= 2)
                and (self.max_missionars - num_missionars == 0
                     or self.max_missionars - num_missionars >= (self.max_cannibals - num_cannibals + 2))):
            return True
        else:
            return False

    def can_move_m(self, state):
        self.set_current_state(state)
        num_missionars = self.current_state[0]
        num_cannibals = self.current_state[1]
        if (num_missionars >= 1
                and (num_missionars == 1 or num_missionars-1 >= num_cannibals)
                and (self.max_missionars - num_missionars + 1 >= self.max_cannibals - num_cannibals)):
            return True
        else:
            return False

    def can_move_c(self, state):
        self.set_current_state(state)
        num_missionars = self.current_state[0]
        num_cannibals = self.current_state[1]
        if (num_cannibals >= 1
                and (self.max_missionars - num_missionars == 0
                     or self.max_missionars - num_missionars >= self.max_cannibals - num_cannibals + 1)):
            return True
        else:
            return False
