import re
import random

domains = ['_acme-challenge.443888.xyz', 'd1turjz14jo.chinam.eu.org', 'dwpdt1sclbmq.chinat.indevs.in', 'tydwzcch.chinam.eu.org', 'cyuxj212pnq.chinat.indevs.in', 'm834s7cv.chinam.eu.org', 'o9ep7jzg1ljs.chinav.indevs.in', 'bt5hpm5jf6.chinam.eu.org', 'r8e51vobnu.chinav.indevs.in']
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
