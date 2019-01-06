class Solution:
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def decomp(ns):
            if "." in ns:
                ip, dp = ns.split(".")
            else:
                ip = ns
                dp = ""

            while ip.startswith("0") and len(ip) > 1:
                ip = ip[1:]

            if len(dp) > 0:
                if "(" in dp:
                    x = dp.find("(")
                    nrp = dp[:x]
                    rp = dp[x + 1 : -1]
                    if "".join(list(set(list(rp)))) == "0":
                        rp = ""
                        while len(nrp) >= 0 and nrp.endswith("0"):
                            nrp = nrp[:-1]
                else:
                    nrp = dp
                    while len(nrp) >= 0 and nrp.endswith("0"):
                        nrp = nrp[:-1]
                    rp = ""
            else:
                nrp = ""
                rp = ""
            return ip, nrp, rp

        def reduce(ip, nrp, rp):
            if len(rp) == 4:
                if rp[:2] == rp[-2:]:
                    rp = rp[:2]
            if len(rp) == 3:
                if rp[0] == rp[1] == rp[2]:
                    rp = rp[0]
            if len(rp) == 2:
                if rp[0] == rp[1]:
                    rp = rp[0]

            if len(rp) > 0:
                while len(nrp) > 0 and len(rp) > 0 and nrp[-1] == rp[-1]:
                    nrp = nrp[:-1]
                    rp = rp[-1] + rp[:-1]

            if rp == "9":
                if nrp == "":
                    return str(int(ip) + 1), "", ""
                else:
                    nnrp = str(int(nrp) + 1)
                    nrp = "0" * (len(nrp) - len(nnrp)) + nnrp
                    rp = ""

            return ip, nrp, rp

        dS = decomp(S)
        dT = decomp(T)
        rS = reduce(*dS)
        rT = reduce(*dT)

        return rS == rT
