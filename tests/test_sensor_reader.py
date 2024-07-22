import unittest
from sensors.sensor_reader import SensorReader

class TestSensorReader(unittest.TestCase):
    def test_read_sensor_data(self):
        reader = SensorReader()
        data = reader.read_sensor_data()
        self.assertIn("temperature", data)
        self.assertIn("humidity", data)

if __name__ == '__main__':
    unittest.main()
