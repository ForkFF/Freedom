import re
import random

domains = ['o2m0zjhz0slm.chinav.indevs.in', 'pujd1crfzx5.chinam.indevs.in', 'q6x65zp4w.gfw.hidns.co', 'dzxvn7a7r.chinam.indevs.in', 'qt2cte0z61.gfw.hidns.co', 'llhgje3in89z.chinav.indevs.in', 'op6tju2a.gfw.hidns.co', 'pnat6unnnp.gfw.hidns.co', 'zu7rz41bbfz4.chinav.indevs.in', 'rxju6p8m.danfeng.gv.uy', 'oxwxtrvm3.danfeng.gv.uy', 'j0enf81pmt.gfw.hidns.co', 'd2wiyfbwnyf.danfeng.gv.uy', 'okbhq9o4867.gfw.hidns.co', 'g321s416vut.chinav.indevs.in', 'mzees9mh.danfeng.gv.uy', 'jnookzvefe0.danfeng.gv.uy', 'j07ih3wxowr5.gfw.hidns.co', 'wbsnthrtc.chinav.indevs.in', 'knuskvposa83.chinav.indevs.in', 'n44i0ani.gfw.hidns.co', 'ekfi6evi0p.chinav.eu.org', 'gfllmphve.danfeng.gv.uy', 'bxqb9udsy1c7.gfw.hidns.co', 'jrr8jjznm.chinam.indevs.in', 'itz4m3m5v7.chinav.indevs.in', 'j5a0dvrw52u.chinam.indevs.in', 'u0eammn4e30v.gfw.hidns.co', 'g5lauoe4pq.chinav.indevs.in', 'd5ixkx2w.gfw.hidns.co', 'ikkgljv5.chinam.indevs.in', 'nw11p3ql0jm.chinav.indevs.in', 'xco8dx9j5252.danfeng.gv.uy', 'ypsg7e0wvt.chinam.indevs.in', 'abxxswoudcjz.chinav.eu.org', 'paueq260.danfeng.gv.uy', 'mt2rn7mla.chinav.indevs.in', 'ksgyus8a.chinav.indevs.in', 'm37o9alw51.danfeng.gv.uy', 'lot7e7u9.chinav.indevs.in', 'sp18nyrj9.chinav.indevs.in', 'urfbqo42.danfeng.gv.uy', 'rk13hiap.gfw.hidns.co', 'stt3nt3w2e.gfw.hidns.co', 'ac1pbn392qql.fgfw.qzz.io']
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
