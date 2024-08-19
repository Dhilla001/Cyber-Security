#This is a very basic simple firewall simulation
import random

#Generating own random ip addresses
#If the generated ip is in the rule set of the firewall, then the firewall blocks the ip
#In a real world scenario, the generated ip is replaced with the ip requesting to access the system
def gen_ip():
    return f'198.162.1.{random.randint(0,20)}'

def check_rules(ip,rules):
    for rule_ip, action in rules.items():
        if ip==rule_ip:
            return action
    return 'Allow'

rules = {
    '198.162.1.1':'Block',
    '198.162.1.4':'Block',
    '198.162.1.9':'Block',
    '198.162.1.13':'Block',
    '198.162.1.16':'Block',
    '198.162.1.19':'Block'
}

def main():
    for _ in range(15):
        ip = gen_ip()
        action = check_rules(ip,rules)
        pid = random.randint(0,9999)
        print(f'PID No.: {pid}    ip:{ip}    {action}')

if __name__ == "__main__":
    main()

