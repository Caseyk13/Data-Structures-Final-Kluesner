import heapq
import unittest
import finalLodgic
import heapq



class TestListElements(unittest.TestCase):
    def setUp(self):
        self.jobs = [[1], [3], [5]]
        self.expectedJobs = [[1], [3], [5]]
        united = heapq
        united.heapify(self.jobs)

    def tearDown(self):
        self.jobs = []
        self.expectedJobs = []

    def test_count_eq(self):
        """Will succeed"""
        self.assertCountEqual(self.jobs, self.expectedJobs)

    def test_list_eq(self):
        """Will fail"""
        self.assertListEqual(self.jobs, self.expectedJobs)




if __name__ == '__main__':
    unittest.main()
