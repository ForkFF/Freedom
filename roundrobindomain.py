import re
import random

domains = ['l1ibp8ly.backend-node.gfw.hidns.co', 'twnn1j15.node-cache-01.fgfw.indevs.in', 'mtlu.media-cdn-jp.chinam.indevs.in', 'zbe.auth-node-01.gfw.hidns.co', 'ts7or.cache.chinam.indevs.in', 'pejwvw.api-worker.chinam.indevs.in', 'aqona0.node-cache-a1.chinav.indevs.in', 's4gaf2l.relay-01.sh21.eu.org', 'gh422.node-02.chinam.indevs.in', 'hp22o1.node-b.chinav.indevs.in', 'e43zyc.cdn-edge-jp.fgfw.qzz.io', 'r4lx.core.gfw.hidns.co', 'k598psis.auth.sh21.eu.org', 'cnn.storage-api.sh21.eu.org', 'mqw4.api-edge.fgfw.qzz.io', 'xuaxsde.img-node.fgfw.indevs.in', 'y0hph3c4.console-node.chinav.indevs.in', 'gso9r.gateway-edge.chinav.indevs.in', 'f0w8uhw.static-cdn-01.fgfw.qzz.io', 'ssfe.cdn-static.fgfw.indevs.in', 'i4b.stream-node.chinav.indevs.in', 'g0bd3nd9.media-edge-01.gfw.hidns.co', 'znjzbc.node-core.chinav.indevs.in', 'iip26mmf.cdn-edge-jp.chinav.indevs.in', 'h0payuw.uploads.sh21.eu.org', 'snzeys.edge-node-a1.fgfw.qzz.io', 'ewur4k.api-edge-02.chinat.indevs.in', 'ajo9j4w.img-cdn.chinav.indevs.in', 'yniz.img-cache.fgfw.indevs.in', 'yqv.cdn-node-02.chinat.indevs.in', 'uiz9vbq.mirror-edge.sh21.eu.org', 'n6j.cdn-edge-jp.chinat.indevs.in', 'wzvh.panel-api.gfw.hidns.co', 'cgcbbo.media-cache-01.chinav.indevs.in', 'a50u951.stream.chinav.indevs.in', 'acyq7kj.api-node-eu.chinat.indevs.in', 'xw0d9r.cdn-edge-sg.chinam.indevs.in', 'n63n17.mail.sh21.eu.org', 'iuh1.auth-proxy.chinat.indevs.in', 'yvl5fy.data-cache.chinam.indevs.in', 'e9x.mirror-node.chinav.indevs.in', 'xjv.node-proxy.chinam.indevs.in', 'akrip7.beta-edge.fgfw.indevs.in', 'm16itazc.api-core.chinat.indevs.in', 'py7k82mu.api-node-02.gfw.hidns.co', 'mcbeaamn.relay-api.fgfw.qzz.io', 'ynwta9.api-edge.fgfw.qzz.io', 'pl4oj.mirror.fgfw.indevs.in', 'cv6v.cdn-relay.chinat.indevs.in', 'nt3c.edge-stream.chinat.indevs.in', 'mug.support.gfw.hidns.co', 'bwy8qm.data-node-us.chinav.indevs.in', 'ikw6x4.stream-node-us.chinav.indevs.in', 'z8vauu.edge-b.fgfw.qzz.io', 'u0d1.proxy-relay.sh21.eu.org', 'v6u.cdn-a.chinam.indevs.in', 'kpvn42j.login-service.chinam.indevs.in', 'onxww2k.node-cache-01.chinam.indevs.in', 'fn2bkp6.data-relay.chinat.indevs.in', 'qwx1cfe.worker-api.chinam.indevs.in', 'juvfhox.auth-node-01.sh21.eu.org', 'baq.mail.chinam.indevs.in']
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
