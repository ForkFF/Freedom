import re
import random

domains = ['rom.media-cdn-01.chinav.eu.org', 'xox.cdn-cache-01.chinat.indevs.in', 'pimelef.cdn-edge.fgfw.qzz.io', 'd8euiih.monitor.sh21.eu.org', 'q0rwc0f.edge.fgfw.qzz.io', 'uq5l.stage-node.chinav.indevs.in', 'nfhv9rz.relay-api.chinat.indevs.in', 'qccs.beta-api.sh21.eu.org', 'iqjs.login-service.chinam.indevs.in', 'rlm68.relay-node.fgfw.indevs.in', 'gyi7hi.app-node.fgfw.indevs.in', 'hms7df.monitor.fgfw.qzz.io', 'zdy.cdn-edge-b2.sh21.eu.org']
def update_yaml_with_single_domain(file_path):
    selected_domain = random.choice(domains)
    print(f"Random domain: {selected_domain}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    def replace_func(match):
        key = match.group(1)
        return f"{key} {selected_domain}"

    pattern = r'(servername:|Host:)\s+([a-zA-Z0-9\-\.]+)'
    new_content = re.sub(pattern, replace_func, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("YAML updated!")

if __name__ == "__main__":
    update_yaml_with_single_domain('sayuri.yaml')
