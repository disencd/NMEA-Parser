import matplotlib.pyplot as plt

def plot_satellites_vs_time(data):
    """Plot the number of satellites tracked vs. time."""
    plt.figure(figsize=(12, 6))
    plt.plot(data['Timestamp'], data['Satellites Tracked'], marker='o', linestyle='-')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Satellites Tracked')
    plt.title('Number of Satellites Tracked vs. Time')
    plt.grid(True)
    plt.show()