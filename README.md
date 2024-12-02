
# IoT Weather Application

This project demonstrates an IoT application that fetches weather data, processes it, and visualizes it in real-time. It involves using APIs, MQTT, Kafka, Apache Spark, and MongoDB to build a complete data pipeline for weather data analysis.

## Features
- Fetch weather data from OpenWeatherMap API.
- Publish weather data to an MQTT broker.
- Consume MQTT messages using Apache Kafka.
- Process real-time data with Apache Spark Structured Streaming.
- Store processed data in MongoDB.
- Visualize data on a live dashboard (e.g., Grafana).

## Project Structure
- `fetch_weather.py`: Fetches weather data using the OpenWeatherMap API.
- `mqtt_publisher.py`: Publishes weather data to an MQTT topic.
- `kafka_consumer.py`: Consumes data from a Kafka topic.
- `spark_streaming.py`: Processes real-time data with Apache Spark.

## Prerequisites
1. Python 3.6+ installed on your system.
2. Install required libraries:
   ```bash
   pip install requests paho-mqtt kafka-python pyspark
   ```
3. Services to set up:
   - MQTT broker (e.g., Mosquitto or a cloud-based broker).
   - Kafka and Zookeeper.
   - MongoDB.

## Setup Instructions
1. **Weather API Configuration**:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/) and get an API key.
   - Replace `your_api_key_here` in the code with your API key.

2. **Run the Scripts**:
   - Start by fetching and publishing weather data:
     ```bash
     python fetch_weather.py
     python mqtt_publisher.py
     ```
   - Set up and run Kafka services.
   - Consume Kafka messages:
     ```bash
     python kafka_consumer.py
     ```
   - Process the data with Spark:
     ```bash
     python spark_streaming.py
     ```

3. **Visualize the Data**:
   - Use tools like Grafana or a custom web app to display real-time data.

## Future Enhancements
- Integrate advanced analytics using machine learning models.
- Add notifications for extreme weather conditions.
- Scale the application with distributed systems like Kubernetes.

---

For questions or contributions, feel free to raise an issue or submit a pull request.
