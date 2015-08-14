import random
import math


class Attributes:

    @staticmethod
    def choose_attribute_order(number_of_attributes):

        attributes_random = []
        for i in range(int(number_of_attributes)):
            number = random.randint(1, number_of_attributes)
            while number in attributes_random:
                number = random.randint(1, number_of_attributes)
            attributes_random.append(number)

        return attributes_random

    @staticmethod
    def generate_attribute_values(level, number_of_attributes, attributes_modifier):

        stat_lower = math.floor(attributes_modifier * level)
        if stat_lower < 1:
            stat_lower = 1
        stat_upper = math.floor(attributes_modifier * number_of_attributes * level)
        if stat_upper < 1:
            stat_upper = 1

        attributes_random_values = []

        rest_value = 0
        attribute_value_total = 0

        for i in range(1, int(number_of_attributes)):
            value = random.randint(rest_value, stat_upper)

            rest_value = stat_upper - value

            value += stat_lower
            if i == 1:
                value += stat_lower

            attribute_value_total += value
            attributes_random_values.append(value)

        last_attribute_value = int(stat_upper * (number_of_attributes + 1)) - attribute_value_total

        if number_of_attributes == 1:
            last_attribute_value = math.floor(attributes_modifier * level) * 2

        attributes_random_values.append(last_attribute_value)

        return attributes_random_values
