from sensors.sensor_reader import SensorReader
from data.data_processor import DataProcessor
from storage.data_storage import DataStorage

def main():
    sensor_reader = SensorReader()
    data_processor = DataProcessor()
    data_storage = DataStorage()

    sensor_data = sensor_reader.read_sensor_data()
    processed_data = data_processor.process_data(sensor_data)
    data_storage.store_data(processed_data)

if __name__ == "__main__":
    main()
