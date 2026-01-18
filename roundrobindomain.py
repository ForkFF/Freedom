import re
import random

domains = ['snippet.gfw.nn.kg',
    'snippet.fgfw.indevs.in',
    'snippet.chinam.indevs.in',
    'snippet.sheilabelinda.ndjp.net',
    'snippet.danfeng21.ndjp.net',
    'snippet.fgfw.ye.gs',
    'snippet.fgfw.cc.cd',
    'snippet.fgfw.ccwu.cc',
    'snippet.fgfw.de5.net',
    'snippet.fgfw.us.ci',
    'snippet.fgfw.eu.org',
    'snippet.sh21.eu.org',
    'snippet.fgfw.ndjp.net',
    'snippet.danfeng.theworkpc.com',
    'snippet.danfeng.ccwu.cc',
    'snippet.danfeng.cc.cd',
    'snippet.danfeng.eu.org',
    'snippet.danfeng.site',
    'snippet.danfeng.dedyn.io',
    'snippet.danfeng.us.ci',
    'snippet.danfeng.de5.net',
    'snippet.danfeng.gleeze.com',
    'snippet.danfeng.gv.uy',
    'snippet.danfeng.nn.kg',
    'snippet.danfeng.indevs.in',
    'snippet.danfeng.kozow.com',
    'snippet.danfeng.let.gs',
    'snippet.gfw.hidns.co',
    'danfeng.sylu.cc',
    'danfeng.sylu.net',
    'snippet.443888.xyz'
  ]

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
