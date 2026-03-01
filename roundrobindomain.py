import re
import random

domains = ['d1turjz14jo.chinam.eu.org', 'dwpdt1sclbmq.chinat.indevs.in', 'tydwzcch.chinam.eu.org', 'cyuxj212pnq.chinat.indevs.in', 'm834s7cv.chinam.eu.org', 'o9ep7jzg1ljs.chinav.indevs.in', 'bt5hpm5jf6.chinam.eu.org', 'r8e51vobnu.chinav.indevs.in', 'l4dhf6elv.chinav.indevs.in', 'y4fk5ppa.chinam.indevs.in', 'za56b8yqfhr.chinam.eu.org', 'xei0vyob6y0o.chinat.indevs.in', 'e2roh174px.chinat.indevs.in', 'gd1ya93ge.chinam.indevs.in', 'got2d2ktp4r.chinam.indevs.in', 'sd1lznov9.chinam.indevs.in', 'wqdo76ww8ndc.chinat.indevs.in', 'k2a5gmqp.chinat.indevs.in', 'aaksh0gsk.chinat.indevs.in', 'zg2nh5lf.chinam.eu.org', 'l6yzat4d.chinav.eu.org', 'etgpkda0.chinav.eu.org', 'kfaq8uz96.chinav.eu.org', 's1kkpuf5c3.chinat.indevs.in', 'k7ryegiaeu.chinam.eu.org', 'x5dpudyj1.chinav.indevs.in', 'lirpeuijr.chinav.indevs.in', 'fqrf5tlc.chinav.eu.org', 'f5383e07d.chinam.indevs.in', 'msffvgvfo.fgfw.indevs.in', 'parn632q2.chinav.indevs.in', 'gjhapsegj69y.fgfw.indevs.in', 'ducqbvsi.chinav.eu.org', 'ki3ndg49ph.chinat.indevs.in', 'zsk15jrad.chinat.indevs.in', 'le899e0uw.chinav.indevs.in', 'mfzsm7evl.chinam.indevs.in', 's8edgebu.chinat.indevs.in', 'kdlugmt0hbhl.chinav.eu.org', 'hs1wklxjk.fgfw.indevs.in', 'luxat5m6.chinam.eu.org', 'co9d204kmcb.fgfw.indevs.in', 'f99arspqnt.chinav.indevs.in', 'wmy3i5vynlg5.fgfw.indevs.in', 'ms1avuqntx02.chinav.eu.org', 'm3rfvlfdnd.chinam.indevs.in']
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
