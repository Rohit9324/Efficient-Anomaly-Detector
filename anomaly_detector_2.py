class EWMAAnomalyDetector:
    def __init__(self, alpha=0.3, threshold=0.1):
        """Initialize with a smoothing factor (alpha) and a threshold."""
        self.alpha = alpha
        self.threshold = threshold
        self.ewma = None  # Initial smoothed value

    def detect(self, value):
        """Detect anomalies based on the residual (difference from EWMA)."""
        if self.ewma is None:
            self.ewma = value
        else:
            # Update EWMA with the new value
            self.ewma = self.alpha * value + (1 - self.alpha) * self.ewma
        
        # Calculate residual (absolute difference between value and EWMA)
        residual = abs(value - self.ewma)
        
        # Check if residual is greater than the threshold (anomaly)
        if residual > self.threshold:
            return True, self.ewma  # Anomaly detected
        return False, self.ewma  # No anomaly
