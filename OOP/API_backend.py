class ParsesCookies:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def cookies(self):
        return self.dictionary.get("cookies")

    def is_authed(self):
        return "auth_key" in list(self.cookies().keys())


class ParsesBody:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def body(self):
        return self.dictionary.get("body")


class ParsesHeaders:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def headers(self):
        return self.dictionary.get("headers")

    def need_json(self):
        if self.headers().get("content-type") == "application/json":
            return True
        else:
            return False


if __name__ == "__name__":
    request = {
      "cookies": {'auth_key': 233, "key_2": 1488},
      "body": "a long time ago, in a Galaxy far, far away",
      "headers": {"content-type": "application/json", "Accept": "application/json"}
    }

    handler = ParsesCookies(request)
    print(handler.is_authed())

