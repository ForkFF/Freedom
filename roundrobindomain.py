import re
import random

domains = ['ekfi6evi0p.chinav.eu.org', 'gfllmphve.danfeng.gv.uy', 'jrr8jjznm.chinam.indevs.in', 'j5a0dvrw52u.chinam.indevs.in', 'ikkgljv5.chinam.indevs.in', 'xco8dx9j5252.danfeng.gv.uy', 'ypsg7e0wvt.chinam.indevs.in', 'abxxswoudcjz.chinav.eu.org', 'paueq260.danfeng.gv.uy', 'm37o9alw51.danfeng.gv.uy', 'urfbqo42.danfeng.gv.uy', 'ac1pbn392qql.fgfw.qzz.io', 'vt44afrmqyb.danfeng.gv.uy', 'z9pdfo3fm.danfeng.qzz.io', 'lnov64nh.fgfw.qzz.io', 'i276dawc.danfeng.qzz.io', 'qeccnw7svyo.chinav.eu.org', 'eublwdu71la.danfeng.qzz.io', 'jxqwp4nzm6o.chinav.eu.org', 'bh0070x2.danfeng.gv.uy', 'w0cqvpddf.danfeng.gv.uy', 'rsytsihz.danfeng.gv.uy', 'ei6kvrlr9kr.danfeng.qzz.io', 'ysmvd6zvzgqj.chinav.eu.org', 'e4goah11g.fgfw.qzz.io', 'glp2ul6ss5g0.fgfw.qzz.io', 'oisxrdygimyg.chinam.indevs.in', 'c674xj5uu.chinam.indevs.in', 'r62w8zwzus.chinam.indevs.in', 'bpskajeql6n8.chinam.indevs.in', 'tpi2opy9bk.chinav.eu.org', 'ui4waovxqh.chinav.eu.org', 'vbxkgv81x.danfeng.qzz.io', 'lfli43jd1.danfeng.gv.uy', 'esyjjh2xwgr.chinav.eu.org', 'kod4t259zf.fgfw.qzz.io', 'p3lydb507umi.chinav.eu.org', 'ud3fywa7.chinav.eu.org', 'l1tfe1d07ogu.chinam.indevs.in', 'jjvh8940sq4.danfeng.gv.uy', 'k9e5frount.chinav.eu.org', 'e3ty9hv5p.chinam.indevs.in', 'gavorbhj.chinam.indevs.in']
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
