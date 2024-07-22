class DataProcessor:
    def process_data(self, data):
        # Código para processar os dados
        processed_data = {
            "temperature": data["temperature"] * 1.8 + 32,  # Convertendo para Fahrenheit
            "humidity": data["humidity"]
        }
        return processed_data
