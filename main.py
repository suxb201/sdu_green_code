from mitmproxy.http import flow
from bs4 import BeautifulSoup


def green(html):
    html = html.replace('"if_pass":"2"', '"if_pass":"1"')  # change 1
    html = html.replace('禁止通行', '可通行')  # change 5
    soup = BeautifulSoup(html, "html.parser")

    divs = soup.find_all("div", "security-panel-body")
    del divs[0]["style"]  # change 2
    divs[1]["style"] = "display: none;"  # change 3

    div = soup.find("div", "two-btn")
    del div["style"]  # change 4

    return str(soup)


def response(flow: flow):
    if "https://sdxyt.sdu.edu.cn/tp_jp/jp/temperature?place_id" in flow.request.url:
        print(flow.request.url)
        html = flow.response.get_text()
        html = green(html)
        flow.response.set_text(html)


def request(flow: flow):
    # “进门” “出门” 按钮重定向，避免记录信息（虽然猜测后台不会记录的...
    if '/tp_jp/jp/returnSchool' in flow.request.url:
        flow.request.path = '/tp_jp/jp/mobileHome'
