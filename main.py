from data_stream import data_stream_simulation
from anomaly_detector import EWMAAnomalyDetector

def main():
    detector = EWMAAnomalyDetector(alpha=0.3, threshold=0.1)
    stream_generator = data_stream_simulation()

    for value in stream_generator:
        is_anomaly, ewma = detector.detect(value)
        if is_anomaly:
            print(f"Anomaly detected: {value} (EWMA: {ewma})")
        else:
            print(f"Value: {value} (EWMA: {ewma})")

if __name__ == "__main__":
    main()
    
import matplotlib.pyplot as plt

def real_time_visualization(stream_generator, detector):
    data_points = []
    ewma_points = []
    anomalies = []

    plt.ion()  # Interactive mode on

    fig, ax = plt.subplots()
    for i, value in enumerate(stream_generator):
        is_anomaly, ewma = detector.detect(value)
        data_points.append(value)
        ewma_points.append(ewma)

        ax.clear()  # Clear the plot
        ax.plot(data_points, label="Data Stream")
        ax.plot(ewma_points, label="EWMA", linestyle="--")

        if is_anomaly:
            ax.scatter(i, value, color='red', label="Anomaly")

        ax.legend()
        plt.pause(0.1)  # Pause to update the plot in real-time

    plt.ioff()  # Turn off interactive mode
    plt.show()

if __name__ == "__main__":
    detector = EWMAAnomalyDetector(alpha=0.3, threshold=0.1)
    stream_generator = data_stream_simulation()
    real_time_visualization(stream_generator, detector)
    


