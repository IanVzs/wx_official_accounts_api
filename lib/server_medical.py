from helpers import api
class Medical:
    url = "http://127.0.0.1:8000"

    def qa(self, content) -> str:
        url = Medical.url + f"/ask_graph/?content={content}"
        resp = api.request_api(url)
        return resp.get("code") == 200 and resp.get("content", "") or ''