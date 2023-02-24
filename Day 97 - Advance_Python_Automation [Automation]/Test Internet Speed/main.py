from speedtest import Speedtest

network = Speedtest()

print("Running Speed Test ===>🚀")

down = network.download()
up = network.upload()

print(f"🔼 Upload Speed: {round(up/(1024*1024), 2)} Mbps \n⏬ Download Speed: {round(down/(1024*1024), 2)} Mbps")

