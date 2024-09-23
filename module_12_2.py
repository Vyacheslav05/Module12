class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    # def start(self):
    #     finishers = {}
    #     place = 1
    #     while self.participants:
    #         for participant in self.participants:
    #             participant.run()
    #             if participant.distance >= self.full_distance:
    #                 finishers[place] = participant
    #                 place += 1
    #                 self.participants.remove(participant)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        result = tournament.start()
        self.all_results[self._testMethodName] = {place: runner.name for place, runner in result.items()}
        last_place = max(result.keys())
        self.assertTrue(result[last_place].name == "Ник")

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        result = tournament.start()
        self.all_results[self._testMethodName] = {place: runner.name for place, runner in result.items()}
        last_place = max(result.keys())
        self.assertTrue(result[last_place].name == "Ник")

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        result = tournament.start()
        self.all_results[self._testMethodName] = {place: runner.name for place, runner in result.items()}
        last_place = max(result.keys())
        self.assertTrue(result[last_place].name == "Ник")

if __name__ == "__main__":
    unittest.main()