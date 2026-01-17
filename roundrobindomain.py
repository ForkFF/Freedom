import re
import random

domains = [
    'snippet.gfw.nn.kg','snippet.fgfw.indevs.in','snippet.chinam.indevs.in',
    'snippet.sheilabelinda.ndjp.net','snippet.danfeng.ndjp.net','snippet.fgfw.ye.gs',
    'snippet.fgfw.cc.cd','snippet.fgfw.ccwu.cc','snippet.fgfw.de5.net',
    'snippet.fgfw.us.ci','snippet.fgfw.eu.org','snippet.sh21.eu.org',
    'snippet.fgfw.ndjp.net','snippet.danfeng.theworkpc.com','snippet.danfeng.ccwu.cc',
    'snippet.danfeng.cc.cd','snippet.danfeng.eu.org','snippet.danfeng.site',
    'snippet.danfeng.dedyn.io','snippet.danfeng.us.ci','snippet.danfeng.de5.net',
    'snippet.danfeng.gleeze.com','snippet.danfeng.gv.uy','snippet.danfeng.nn.kg',
    'snippet.danfeng.indevs.in','snippet.danfeng.kozow.com','snippet.danfeng.giize.com',
    'snippet.danfeng.let.gs','snippet.gfw.hidns.co','danfeng.sylu.cc',
    'danfeng.sylu.net','snippet.443888.xyz'
]

def update_yaml_domains(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_domain(match):
        key = match.group(1)
        new_domain = random.choice(domains)
        return f"{key} {new_domain}"

    pattern_servername = r'(servername:)\s+([a-zA-Z0-9\-\.]+)'
    content = re.sub(pattern_servername, replace_domain, content)

    pattern_host = r'(Host:)\s+([a-zA-Z0-9\-\.]+)'
    content = re.sub(pattern_host, replace_domain, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("YAML updated")

if __name__ == "__main__":
    update_yaml_domains('sayuri.yaml')
