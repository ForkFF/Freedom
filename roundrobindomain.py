import re
import random

domains = ['vtxpxgne.mirror-node.sh21.eu.org', 'wsm52.gateway-api-01.chinav.indevs.in', 'ar2m.api-backend.sh21.eu.org', 'qrqt.backend-edge.sh21.eu.org', 'jbp7i.data-edge.chinav.indevs.in', 'sguj46k.static-node-01.chinav.eu.org', 't39sed.gateway-api.sh21.eu.org', 'omn15.files-cdn.chinat.indevs.in', 'mz0tgmxz.user-api.chinav.eu.org', 'tq0iwf.user-service.chinav.eu.org', 'v3wdc.app-node.chinam.indevs.in', 'y4z.cdn-a.chinav.indevs.in', 'nai3.api-gateway-01.chinat.indevs.in', 'ii5.static-node-01.chinav.indevs.in', 'la463cv6.static-cache.chinam.indevs.in', 'y0wkd.app-edge.chinav.indevs.in', 'nxahk.media-cdn.sh21.eu.org', 'n76.api-node-sg.chinav.indevs.in', 'sg156m.cdn-edge-eu.sh21.eu.org', 'jek.media-cdn.chinav.eu.org', 'srd0l.monitor-edge.chinav.indevs.in', 'pkw.download.fgfw.qzz.io', 'klng2.stream-cdn.sh21.eu.org', 'le8535x4.data-stream.sh21.eu.org', 'vfa9.cdn-stream.fgfw.indevs.in', 'eedu7.mail.danfeng.qzz.io', 'nlrkld.files-api.danfeng.cyou', 'fo5xj.monitor-edge.chinat.indevs.in', 'c1mxc.api-gateway.fgfw.qzz.io', 'zllj95qn.api-node-sg.chinat.indevs.in', 'v8mbk9s.node-stream.danfeng.qzz.io', 'w9rw8g1k.node-c.danfeng.gv.uy', 'urg0.edge-node-us.danfeng.bond', 'z8c.node-01.fgfw.qzz.io']
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
