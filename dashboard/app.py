import streamlit as st
import time
import threading
from collections import deque
import pytz
import datetime

def ist_localtime(secs=None):
    if secs is None:
        dt = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    else:
        dt = datetime.datetime.fromtimestamp(secs, pytz.timezone('Asia/Kolkata'))
    return dt.timetuple()

time.localtime = ist_localtime

# Thread-safe queue to hold anomalies
anomaly_queue = deque(maxlen=100)

def add_anomaly(anomaly):
    anomaly_queue.appendleft(anomaly)

def anomaly_generator():
    """
    Dummy generator to simulate incoming anomalies.
    Replace this with real integration to streaming pipeline.
    """
    import random
    while True:
        time.sleep(random.randint(5, 15))
        anomaly = f"Anomaly detected at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"
        add_anomaly(anomaly)

def main():
    st.title("Real-time Anomaly Detection Dashboard")

    # Start anomaly generator thread
    threading.Thread(target=anomaly_generator, daemon=True).start()

    st.subheader("Recent Anomalies")
    anomaly_placeholder = st.empty()

    while True:
        anomalies = list(anomaly_queue)
        if anomalies:
            # Display each anomaly on a separate line
            anomaly_placeholder.markdown("\n".join(anomalies), unsafe_allow_html=True)
        else:
            anomaly_placeholder.write("No anomalies detected yet.")
        time.sleep(2)

if __name__ == "__main__":
    main()
