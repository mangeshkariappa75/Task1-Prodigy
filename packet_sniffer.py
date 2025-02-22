from scapy.all import sniff
import sys

# Disclaimer and terms of use
def display_disclaimer():
    disclaimer_text = (
        "------------------------ Packet Sniffer Tool Disclaimer ---------------------------\n"
        "This packet sniffer tool is intended for educational and ethical purposes only.\n"
        "Unauthorized use, distribution, or modification of this tool is strictly prohibited.\n"
        "By using this tool, you agree to the following terms and conditions:\n"
        "\n1. You will only use this tool on networks and systems for which you have explicit permission.\n"
        "2. You will not use this tool to violate any laws, regulations, or terms of service.\n"
        "3. You will not use this tool to harm, disrupt, or exploit any networks or systems.\n"
        "4. You will not use this tool to intercept, collect, or store any sensitive or confidential information.\n"
        "5. You will not redistribute or sell this tool without the express permission of the author.\n"
        "6. The author is not responsible for any damages or losses incurred as a result of using this tool.\n"
        "7. You will respect the privacy and security of all networks and systems you interact with using this tool."
    )
    print(disclaimer_text)

def accept_terms():
    accept = input("\nDo you accept these terms and conditions? (y/n): ")
    if accept.lower() != 'y':
        print("You must accept the terms and conditions before using this tool.")
        sys.exit()

# Function to display and save the captured packets
def packet_sniff(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        src_port = packet["TCP"].sport
        dst_port = packet["TCP"].dport
        protocol = packet["IP"].proto
        payload = str(packet["TCP"].payload)

        output_string = (
            f"Source IP: {src_ip}\n"
            f"Destination IP: {dst_ip}\n"
            f"Source Port: {src_port}\n"
            f"Destination Port: {dst_port}\n"
            f"Protocol: {protocol}\n"
            f"Payload: {payload[:50]}...\n"
        )

        print(output_string, end='')
        with open('packet_sniffer_results.txt', 'a') as f:
            f.write(output_string)

def main():
    display_disclaimer()
    accept_terms()
    
    print("\n--------------- Packet Sniffing Tool ---------------")
    
    # Calls the sniff() function from the Scapy library to capture and analyze network packets
    sniff(filter="tcp", prn=packet_sniff, store=0, count=10)
    
    # Indicates where the results are saved
    print("\nResults saved to: packet_sniffer_results.txt")

if __name__ == "__main__":
    main()