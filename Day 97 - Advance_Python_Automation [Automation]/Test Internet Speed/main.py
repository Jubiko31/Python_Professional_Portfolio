from speedtest import Speedtest

network = Speedtest()

print("Running Speed Test ===>š")

down = network.download()
up = network.upload()

print(f"š¼ Upload Speed: {round(up/(1024*1024), 2)} Mbps \nā¬ Download Speed: {round(down/(1024*1024), 2)} Mbps")

