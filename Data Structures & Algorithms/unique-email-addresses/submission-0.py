class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        u = set()

        for e in emails:
            local, domain = e.split('@')
            local = local.split("+")[0]
            local = local.replace(".", "")
            u.add((local, domain))
        return len(u)