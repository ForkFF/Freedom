import re
import urllib.parse
import urllib.request


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
        url_body = vless_url[8:]

        # 解析 # 后的节点名/备注
        if "#" in url_body:
            url_body, _ = url_body.split("#", 1)

        # 解析 userinfo@server:port
        if "@" in url_body:
            uuid, rest = url_body.split("@", 1)
        else:
            return None

        # 解析 server:port?query
        if "?" in rest:
            _, query_str = rest.split("?", 1)
        else:
            query_str = ""

        # 解析查询参数
        params = urllib.parse.parse_qs(query_str)

        sni = params.get("sni", [""])[0]
        host = params.get("host", [""])[0]
        path = params.get("path", ["/"])[0]

        return {
            "uuid": uuid,
            "sni": sni or host,
            "host": host or sni,
            "path": urllib.parse.unquote(path),
        }
    except Exception as e:
        print(f"解析 URL 失败: {e}")
        return None


def update_yaml_with_regex(yaml_path, parsed_info):
    """使用正则替换，100% 保持原 YAML 的所有排版、换行与格式"""
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

    try:
        with open(yaml_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"读取 {yaml_path} 失败: {e}")
        return

    # 正则表达式说明：
    # 替换 uuid: xxx -> uuid: <new_uuid>
    content = re.sub(
        r"(uuid:\s*)[a-f0-9\-]+", rf"\g<1>{new_uuid}", content, flags=re.IGNORECASE
    )

    # 替换 servername: xxx -> servername: <new_sni>
    content = re.sub(
        r"(servername:\s*)[^\s,}]+", rf"\g<1>{new_sni}", content, flags=re.IGNORECASE
    )

    # 替换 Host: xxx -> Host: <new_host>
    content = re.sub(
        r"(Host:\s*)[^\s,}]+", rf"\g<1>{new_host}", content, flags=re.IGNORECASE
    )

    # 替换 path: 'xxx' 或 path: "xxx" 或 path: xxx -> path: '<new_path>'
    content = re.sub(
        r"(path:\s*)[^\s,}]+", rf"\g<1>'{new_path}'", content, flags=re.IGNORECASE
    )

    # 写回文档
    with open(yaml_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n成功更新 {yaml_path}！原格式已绝对保留。")


if __name__ == "__main__":
    sub_url = "https://hhsxy.vavava.kdns.fr/sub?token=1a5ea6321998fb41f713e07105aea297"
    yaml_path = "sayuri.yaml"

    print("1. 正在拉取订阅数据...")
    sub_content = fetch_subscription(sub_url)

    if sub_content:
        lines = [line.strip() for line in sub_content.splitlines() if line.strip()]

        vless_info = None
        for line in lines:
            if line.startswith("vless://"):
                vless_info = parse_vless_url(line)
                if vless_info:
                    break

        if vless_info:
            print("2. 正在更新配置...")
            update_yaml_with_regex(yaml_path, vless_info)
        else:
            print("未在订阅内容中找到有效的 vless:// 节点。")
