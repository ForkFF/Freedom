import re
import urllib.parse
import urllib.request
import yaml


def fetch_subscription(url):
    """从订阅 URL 获取节点文本内容"""
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        )
        with urllib.request.urlopen(req) as response:
            content = response.read().decode("utf-8")
            return content
    except Exception as e:
        print(f"获取订阅数据失败: {e}")
        return None


def parse_vless_url(vless_url):
    """解析 VLESS URL，提取 uuid, sni, host, path 等信息"""
    if not vless_url.startswith("vless://"):
        return None

    try:
        # 去掉前缀
        url_body = vless_url[8:]

        # 解析 # 后的节点名/备注
        if "#" in url_body:
            url_body, remark = url_body.split("#", 1)

        # 解析 userinfo@server:port
        if "@" in url_body:
            uuid, rest = url_body.split("@", 1)
        else:
            return None

        # 解析 server:port?query
        if "?" in rest:
            server_port, query_str = rest.split("?", 1)
        else:
            server_port = rest
            query_str = ""

        # 解析查询参数
        params = urllib.parse.parse_qs(query_str)

        sni = params.get("sni", [""])[0]
        host = params.get("host", [""])[0]
        path = params.get("path", ["/"])[0]

        return {
            "uuid": uuid,
            "sni": sni or host,  # 如果没写 sni，默认用 host
            "host": host or sni,  # 如果没写 host，默认用 sni
            "path": urllib.parse.unquote(path),
        }
    except Exception as e:
        print(f"解析 URL 失败: {e}")
        return None


def update_yaml_file(yaml_path, parsed_info):
    """更新 YAML 配置文档中的 proxies 字段"""
    if not parsed_info:
        print("未获取到有效的节点参数，取消更新。")
        return

    new_uuid = parsed_info["uuid"]
    new_sni = parsed_info["sni"]
    new_host = parsed_info["host"]
    new_path = parsed_info["path"]

    print(f"提取的最新参数:")
    print(f" - UUID: {new_uuid}")
    print(f" - SNI / Servername: {new_sni}")
    print(f" - Host: {new_host}")
    print(f" - Path: {new_path}")

    # 读取原 YAML 文档
    try:
        with open(yaml_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        print(f"读取 {yaml_path} 失败: {e}")
        return

    # 替换 proxies 中的节点配置
    if "proxies" in config and isinstance(config["proxies"], list):
        for proxy in config["proxies"]:
            # 针对 VLESS 协议的节点进行替换
            if proxy.get("type") == "vless":
                proxy["uuid"] = new_uuid
                proxy["servername"] = new_sni

                # 更新 ws-opts 中的 headers 和 path
                if "ws-opts" in proxy:
                    if "headers" in proxy["ws-opts"]:
                        proxy["ws-opts"]["headers"]["Host"] = new_host
                    proxy["ws-opts"]["path"] = new_path

        # 写回 YAML 文档
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(config, f, allow_unicode=True, sort_keys=False)

        print(f"\n成功更新 {yaml_path}！")
    else:
        print("未在 YAML 中查找到 'proxies' 配置。")


if __name__ == "__main__":
    sub_url = "https://hhsxy.vavava.kdns.fr/sub?token=1a5ea6321998fb41f713e07105aea297"
    yaml_path = "sayuri.yaml"

    print("1. 正在拉取订阅数据...")
    sub_content = fetch_subscription(sub_url)

    if sub_content:
        # 按行分割订阅内容，取第一条有效的 VLESS 节点信息
        lines = [line.strip() for line in sub_content.splitlines() if line.strip()]

        vless_info = None
        for line in lines:
            if line.startswith("vless://"):
                vless_info = parse_vless_url(line)
                if vless_info:
                    break  # 获取到第一个有效的 VLESS 配置后即退出

        if vless_info:
            print("2. 正在更新配置...")
            update_yaml_file(yaml_path, vless_info)
        else:
            print("未在订阅内容中找到有效的 vless:// 节点。")
