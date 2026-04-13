import re
import random

domains = ['l1tfe1d07ogu.chinam.indevs.in', 'e3ty9hv5p.chinam.indevs.in', 'gavorbhj.chinam.indevs.in', 'l2c0xvu6zx.chinam.indevs.in', 'be3noxe89ev.sh21.eu.org', 'o7xl8f3efc.danfeng.qzz.io', 'cdio8zo9axk.danfeng.qzz.io', 'emp1twys5ym.danfeng.qzz.io', 'dbb4m1mn.chinam.indevs.in', 'dq43jdupnv1.danfeng.qzz.io', 'zyyhmxfdcck3.fgfw.qzz.io', 'codu3tyk0.chinam.indevs.in', 'gb6pworso8.danfeng.qzz.io', 'jkl3gix3qz.danfeng.qzz.io', 'sil55n91ophm.chinam.indevs.in', 'q40ivxuck.danfeng.qzz.io', 'uji.media-cdn-01.fgfw.indevs.in', 'p2tqt.files.danfeng.qzz.io', 'lnapfqu.data-node-us.danfeng.qzz.io', 'p7j257h.node-cache.sh21.eu.org', 'yclxf.stream-01.chinam.indevs.in', 'p57gl.core.fgfw.indevs.in', 'g8wkkaz.media-cache-01.sh21.eu.org', 'taxerggd.auth-api-01.sh21.eu.org', 'x3opu61.dev-node.gfw.hidns.co', 'afjevhp6.api-proxy.sh21.eu.org', 'txqd4kyx.node-relay.gfw.hidns.co', 'j402y5.auth-edge.fgfw.indevs.in', 'e5z.node-03.danfeng.qzz.io', 'ooamn.media-relay.chinam.indevs.in', 'okiz5l4.node-relay-01.danfeng.qzz.io', 'pyzm7bil.stream-node-us.sh21.eu.org', 'pchlzn.cdn-a.gfw.hidns.co', 'jdv7sh.data-node-01.chinam.indevs.in', 'lsoe9.cdn-edge-02.fgfw.qzz.io', 'vukf7g2.media-cdn-01.chinav.indevs.in', 'ru9y.api-gateway-02.sh21.eu.org', 'x1d.edge-01.fgfw.indevs.in', 'ut92bv.data.chinam.indevs.in', 'i9uw353.proxy-01.danfeng.qzz.io', 'u6rh.node-a.chinav.indevs.in', 'k8egev.api-node-a1.gfw.hidns.co', 'o47rlz0.api-node-01.sh21.eu.org', 's3vz.user-service.chinav.indevs.in', 'yp20xb9t.user-service.fgfw.indevs.in', 'il5dip.status-api.sh21.eu.org', 'qgljeuqx.stream-node-us.sh21.eu.org', 'l1ibp8ly.backend-node.gfw.hidns.co', 'twnn1j15.node-cache-01.fgfw.indevs.in', 'mtlu.media-cdn-jp.chinam.indevs.in', 'zbe.auth-node-01.gfw.hidns.co', 'ts7or.cache.chinam.indevs.in', 'pejwvw.api-worker.chinam.indevs.in', 'aqona0.node-cache-a1.chinav.indevs.in', 's4gaf2l.relay-01.sh21.eu.org']
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
