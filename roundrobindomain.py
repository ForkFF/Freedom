import re
import random

domains = ['xw0d9r.cdn-edge-sg.chinam.indevs.in', 'n63n17.mail.sh21.eu.org', 'iuh1.auth-proxy.chinat.indevs.in', 'yvl5fy.data-cache.chinam.indevs.in', 'e9x.mirror-node.chinav.indevs.in', 'xjv.node-proxy.chinam.indevs.in', 'akrip7.beta-edge.fgfw.indevs.in', 'm16itazc.api-core.chinat.indevs.in', 'py7k82mu.api-node-02.gfw.hidns.co', 'mcbeaamn.relay-api.fgfw.qzz.io', 'ynwta9.api-edge.fgfw.qzz.io', 'pl4oj.mirror.fgfw.indevs.in', 'cv6v.cdn-relay.chinat.indevs.in', 'nt3c.edge-stream.chinat.indevs.in', 'mug.support.gfw.hidns.co', 'bwy8qm.data-node-us.chinav.indevs.in', 'ikw6x4.stream-node-us.chinav.indevs.in', 'z8vauu.edge-b.fgfw.qzz.io', 'u0d1.proxy-relay.sh21.eu.org', 'v6u.cdn-a.chinam.indevs.in', 'kpvn42j.login-service.chinam.indevs.in', 'onxww2k.node-cache-01.chinam.indevs.in', 'fn2bkp6.data-relay.chinat.indevs.in', 'qwx1cfe.worker-api.chinam.indevs.in', 'juvfhox.auth-node-01.sh21.eu.org', 'baq.mail.chinam.indevs.in', 'xfxl35a.node-edge.gfw.hidns.co', 'ltaeqp.cdn-assets.fgfw.indevs.in', 'h4ipx.stream.fgfw.qzz.io', 'ykhog58r.data-api-01.chinat.indevs.in', 'm165kavw.cdn-01.chinam.indevs.in', 'cplr2.backend.chinam.indevs.in', 'zto7d05.api-relay.sh21.eu.org', 'jaj2zz.relay-node-01.sh21.eu.org', 'keehn1fi.auth-service.gfw.hidns.co', 's3cqz.user-service.fgfw.indevs.in', 'szuwn.status-node-01.sh21.eu.org', 'jpkbw.storage-api.chinam.indevs.in', 'mloi960.edge-stream.chinav.indevs.in', 'n8cfsev.node-c.chinav.indevs.in', 'oai.cdn-node-02.fgfw.qzz.io', 'vd4wl.cdn-img.sh21.eu.org', 'lx43o5.worker-node-01.sh21.eu.org', 'n21x2.files-api.chinav.indevs.in', 'svb13.cdn-edge-jp.fgfw.indevs.in', 'qtz.auth-node-01.gfw.hidns.co', 'ggj.core-node-01.gfw.hidns.co', 'n5bc.panel.chinat.indevs.in', 'r6tv.cdn-img.chinat.indevs.in', 'anuguce.img.chinam.indevs.in', 'th0.api-core.gfw.hidns.co', 'fmn2.assets-node.sh21.eu.org', 'qbsk1e9.auth-api-01.fgfw.qzz.io', 'nxoqi02.proxy.chinat.indevs.in', 'jsid3w77.node-proxy.chinav.indevs.in', 'ifak.api-worker.chinat.indevs.in', 'e5vuenz.media-node.sh21.eu.org', 's82.edge-stream.fgfw.indevs.in', 'avnk.panel-node.chinam.indevs.in', 'ykq.core-api.chinat.indevs.in']
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
