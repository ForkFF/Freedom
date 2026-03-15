import re
import random

domains = ['vrd3rg9qr.chinam.indevs.in', 'uwjl3c7q.fgfw.indevs.in', 'sigxrqy7uv8c.chinam.eu.org', 'o2m0zjhz0slm.chinav.indevs.in', 'yxxcbinu.chinam.eu.org', 'w3na9usy5l8.fgfw.indevs.in', 'pujd1crfzx5.chinam.indevs.in', 'q6x65zp4w.gfw.hidns.co', 'kocr9fo60pmo.chinam.eu.org', 'dzxvn7a7r.chinam.indevs.in', 'kubpq0pxj.fgfw.indevs.in', 'qt2cte0z61.gfw.hidns.co', 'ek86dmdczz.fgfw.indevs.in', 'llhgje3in89z.chinav.indevs.in', 'op6tju2a.gfw.hidns.co', 'sls1ggsd.chinam.eu.org', 'pnat6unnnp.gfw.hidns.co', 'zu7rz41bbfz4.chinav.indevs.in', 'rxju6p8m.danfeng.gv.uy', 'oxwxtrvm3.danfeng.gv.uy', 'j0enf81pmt.gfw.hidns.co', 'd2wiyfbwnyf.danfeng.gv.uy', 'hbm0bvbw3bc7.chinam.eu.org', 'okbhq9o4867.gfw.hidns.co', 'g321s416vut.chinav.indevs.in', 'n4slq25g4kg.chinam.eu.org', 'mzees9mh.danfeng.gv.uy', 'ddrhjb7tl4r0.chinam.eu.org', 'jnookzvefe0.danfeng.gv.uy', 'j07ih3wxowr5.gfw.hidns.co']
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
