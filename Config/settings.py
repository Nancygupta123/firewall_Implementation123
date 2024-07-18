class Settings:
    def __init__(self):
        self.whitelist = set()
        self.blacklist = set()

    def add_to_whitelist(self, ip):
        self.whitelist.add(ip)

    def add_to_blacklist(self, ip):
        self.blacklist.add(ip)

    def get_whitelist(self):
        return list(self.whitelist)

    def get_blacklist(self):
        return list(self.blacklist)
