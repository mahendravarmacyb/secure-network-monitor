import ipaddress
import nmap

from utils.logger import setup_logger
from utils.config import Config


class HostDiscovery:

    def __init__(self):
        self.logger = setup_logger()
        self.config = Config()
        self.scanner = nmap.PortScanner()

    def validate_network(self, network):
        try:
            ipaddress.ip_network(network)
            return True
        except ValueError:
            return False

    def discover_hosts(self, network):

        print("\nScanning network...")
        self.logger.info(f"Scanning network: {network}")

        self.scanner.scan(hosts=network, arguments="-sn")

        hosts = []

        for host in self.scanner.all_hosts():

            hostname = self.scanner[host].hostname()

            hosts.append({
                "ip": host,
                "hostname": hostname if hostname else "Unknown"
            })

        return hosts

    def display_hosts(self, hosts):

        print("\n==============================")
        print("Discovered Hosts")
        print("==============================")

        if not hosts:
            print("No hosts found.")
            return

        for host in hosts:
            print(f"{host['ip']}   {host['hostname']}")

        print(f"\nTotal Hosts: {len(hosts)}")

    def run(self):

        default_network = self.config.get("default_network")

        network = input(
            f"Enter Network [{default_network}]: "
        ).strip()

        if network == "":
            network = default_network

        if not self.validate_network(network):
            print("Invalid Network")
            self.logger.error("Invalid Network")
            return

        hosts = self.discover_hosts(network)

        self.display_hosts(hosts)
