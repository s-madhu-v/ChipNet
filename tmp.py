import psutil

cpu_freq = psutil.cpu_freq()

print("Current CPU frequency: {} GHz".format(cpu_freq.current / 1000))

