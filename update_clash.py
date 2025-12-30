import requests
import sys
from ruamel.yaml import YAML
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 配置部分
SOURCE_URL = "https://api.v1.mk/sub?target=clash&url=https%3A%2F%2Fns.2026565.xyz%2F66666&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FForkFF%2FFreedom%2Frefs%2Fheads%2Fmain%2Fsubconfig-min.ini&exclude=(%E5%85%8D%E8%B4%B9%7C%E7%8F%8D%E6%83%9C%7C%E7%BE%A4%E7%BB%84%7C%E5%AE%98%E6%96%B9)&emoji=true&list=false&xudp=false&udp=false&tfo=false&expand=true&scv=false&fdn=false&new_name=true"
TARGET_FILE = "sayuri.yaml"

def update_proxies():
    # --- 1. 配置重试策略 ---
    print("正在配置下载会话...")
    
    # 定义重试策略
    retry_strategy = Retry(
        total=5,  # 最大重试次数
        backoff_factor=1,  # 重试间隔因子 (等待时间 = {backoff factor} * (2 ** ({number of total retries} - 1)))
                           # 例如: 0.5s, 1s, 2s, 4s, 8s... 避免瞬间刷死服务器
        status_forcelist=[500, 502, 503, 504], # 遇到这些状态码时强制重试
        allowed_methods=["GET"] # 只对 GET 请求重试
    )
    
    # 创建 Session 并挂载适配器
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # --- 2. 获取源配置 ---
    print("正在下载源订阅配置 (已启用自动重试)...")
    try:
        # 使用 session.get 而不是 requests.get
        response = session.get(SOURCE_URL, timeout=30)
        response.raise_for_status() # 检查 404 等其他非 5xx 错误
        
        # 使用简单的 YAML 加载来读取源数据（不需要保留源格式）
        yaml_loader = YAML(typ='safe') 
        source_data = yaml_loader.load(response.text)
    except Exception as e:
        print(f"下载或解析源订阅失败 (已重试5次): {e}")
        sys.exit(1)

    # 2. 从源配置中提取所需的 vless 参数
    new_uuid = None
    new_servername = None
    new_host = None
    
    found_source = False
    if 'proxies' in source_data:
        for proxy in source_data['proxies']:
            # 找到第一个 vless 节点提取参数
            if proxy.get('type') == 'vless':
                new_uuid = proxy.get('uuid')
                new_servername = proxy.get('servername')
                # 尝试提取 headers 中的 host
                if 'ws-opts' in proxy and 'headers' in proxy['ws-opts']:
                    new_host = proxy['ws-opts']['headers'].get('Host')
                
                if new_uuid and new_servername and new_host:
                    found_source = True
                    print(f"成功提取参数:\nUUID: {new_uuid}\nServerName: {new_servername}\nHost: {new_host}")
                    break
    
    if not found_source:
        print("错误: 在源订阅中未找到包含完整参数的 vless 节点。")
        sys.exit(1)

    # 3. 读取并更新本地 sayuri.yaml
    print(f"正在读取并更新 {TARGET_FILE}...")
    
    # 使用 round-trip 模式以保留格式
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096 # 防止自动换行

    # 保留缩进
    yaml.indent(mapping=2, sequence=4, offset=2)
    
    try:
        with open(TARGET_FILE, 'r', encoding='utf-8') as f:
            target_data = yaml.load(f)
            
        update_count = 0
        if 'proxies' in target_data:
            for proxy in target_data['proxies']:
                # 只修改 type 为 vless 的节点，忽略 ss
                if proxy.get('type') == 'vless':
                    print(f"更新节点: {proxy.get('name')}")
                    proxy['uuid'] = new_uuid
                    proxy['servername'] = new_servername
                    
                    # 确保 ws-opts 结构存在
                    if 'ws-opts' not in proxy:
                        proxy['ws-opts'] = {}
                    if 'headers' not in proxy['ws-opts']:
                        proxy['ws-opts']['headers'] = {}
                        
                    proxy['ws-opts']['headers']['Host'] = new_host
                    update_count += 1
        
        if update_count > 0:
            with open(TARGET_FILE, 'w', encoding='utf-8') as f:
                yaml.dump(target_data, f)
            print(f"更新完成，共修改了 {update_count} 个 vless 节点。")
        else:
            print("未发现需要更新的 vless 节点，文档保持不变。")

    except FileNotFoundError:
        print(f"错误: 找不到文档 {TARGET_FILE}")
        sys.exit(1)
    except Exception as e:
        print(f"更新文档失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    update_proxies()
