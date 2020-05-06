"""
Program to show ports that are listening or have established connections
"""

import psutil


def main():
    """
    Gets a list of active connections, then gets all the pids on the system and then looks for established / listening connections, matches the pids to processes and then dumps them to the screen
    """
    conn_dump = []  # catch active connections
    get_conn_list(conn_dump)
    # output sample = sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_DGRAM: 2>, laddr=addr(ip='192.168.122.1', port=138), raddr=(), status='NONE', pid=None)
    # sconn(fd=129, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=56438), raddr=addr(ip='127.0.0.1', port=50227), status='ESTABLISHED', pid=2485)

    pid_dump = []  # catch active pids
    get_pid_list(pid_dump)
    # output sample {'name': 'python', 'pid': 28297, 'username': 'jess'}

    list_to_screen(conn_dump, pid_dump)  # list on screen


def get_pid_list(some_list):
    """
    Uses psutil to get a list of all running processes on the system

    :param some_list: a list to dump the pids into
    :type some_list: list
    :return: a list of pids
    :rtype: list (full of dicts)
    """
    # gather up processes and their names and dump them in a list
    for proc in psutil.process_iter(["pid", "name", "username"]):
        some_list.append(proc.info)
    return some_list


def get_conn_list(some_other_list):
    """
    Uses psutil to get a list of all the active connections on the system and dumps them to a list provided

    :param some_other_list: list to dump into
    :type some_other_list: list
    :return: a list of all active connections an the system
    :rtype: list
    """
    # gather up connections and dump them in a list
    for line in psutil.net_connections():
        some_other_list.append(line)
    return some_other_list


def list_to_screen(conn_dump, pid_dump):
    """
    takes both the lists and then runs through them to match pids and then prints out details of listening/established connections

    :param conn_dump: list of active connections
    :type conn_dump: list
    :param pid_dump: list of active pids
    :type pid_dump: list (full of dicts)
    """
    for line in conn_dump:
        if line[5] == "LISTEN" or line[5] == "ESTABLISHED":
            if line.pid == None:
                print(
                    f"""Process, Unknown running under user, Unknown, with PID: {line.pid}, on port {line.laddr.port}"""
                )
            else:
                for each_line in pid_dump:
                    if line.pid in each_line.values():
                        print(
                            f"""Process {each_line['name']}, running under user '{each_line['username']}' with PID: {each_line['pid']}, on port {line.laddr.port}"""
                        )


if __name__ == "__main__":
    main()
