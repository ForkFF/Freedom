import re
import random

domains = ['_acme-challenge.443888.xyz', 'd1turjz14jo.chinam.eu.org', 'dwpdt1sclbmq.chinat.indevs.in', 'tydwzcch.chinam.eu.org', 'cyuxj212pnq.chinat.indevs.in', 'm834s7cv.chinam.eu.org', 'o9ep7jzg1ljs.chinav.indevs.in', 'bt5hpm5jf6.chinam.eu.org', 'r8e51vobnu.chinav.indevs.in', 'l4dhf6elv.chinav.indevs.in', 'y4fk5ppa.chinam.indevs.in', 'za56b8yqfhr.chinam.eu.org', 'xei0vyob6y0o.chinat.indevs.in', 'e2roh174px.chinat.indevs.in', 'gd1ya93ge.chinam.indevs.in', 'got2d2ktp4r.chinam.indevs.in', 'sd1lznov9.chinam.indevs.in', 'wqdo76ww8ndc.chinat.indevs.in', 'k2a5gmqp.chinat.indevs.in', 'aaksh0gsk.chinat.indevs.in', 'zg2nh5lf.chinam.eu.org', 'l6yzat4d.chinav.eu.org', 'etgpkda0.chinav.eu.org', 'kfaq8uz96.chinav.eu.org', 's1kkpuf5c3.chinat.indevs.in', 'k7ryegiaeu.chinam.eu.org', 'x5dpudyj1.chinav.indevs.in']
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
