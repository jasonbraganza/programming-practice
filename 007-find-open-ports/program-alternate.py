"""
Program to show ports that are listening or have established connections
Trying a simpler, less verbose way
"""

import psutil


def main():

    connections = psutil.net_connections()
    for proc in psutil.process_iter(["pid", "name", "username"]):
        for each_key, each_key_value in proc.info.items():
            if each_key == "pid":
                for each_connection in connections:
                    if proc.info["pid"] == each_connection[6]:
                        print(
                            f"Process {proc.info['name']} with PID {proc.info['pid']} is on port {each_connection.laddr.port}"
                        )


if __name__ == "__main__":
    main()
