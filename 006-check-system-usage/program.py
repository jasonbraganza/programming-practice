import psutil


def main():
    print("Please wait. Checking CPU & Memory utilisation …")
    cpu_usage = psutil.cpu_percent(interval=5)
    mem_usage = psutil.virtual_memory()
    print(
        f" You are using {cpu_usage}% of your total CPU capacity and {mem_usage[2]}% of total memory, actual - {round((mem_usage[3]/(1024**3)), 2)} GB"
    )


if __name__ == "__main__":
    main()
