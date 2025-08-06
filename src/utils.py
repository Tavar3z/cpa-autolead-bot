def parse_proxy(proxy_str):
    try:
        host, port, user, password = proxy_str.strip().split(":")
        return {
            "proxy_host": host,
            "proxy_port": int(port),
            "proxy_user": user,
            "proxy_password": password
        }
    except ValueError:
        raise Exception(f"Formato inválido de proxy: {proxy_str}")
