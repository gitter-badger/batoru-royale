class Experience:

    @staticmethod
    def calculate_experience_need(level):

        calculate_experience_need = 0

        for i in range(int(level)):
            calculate_experience_need += ((level + 1000) * (level * level))

        return calculate_experience_need

    @staticmethod
    def calculate_experience_gain(level, opponent_level):
        experience_gain = opponent_level * opponent_level + opponent_level * opponent_level - level * level

        if experience_gain < 0:
            experience_gain = 0

        return experience_gain
