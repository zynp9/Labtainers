from dnslib import RR, QTYPE, A
from dnslib.server import DNSServer, BaseResolver
import random


class FastFluxResolver(BaseResolver):
    def resolve(self, request, handler):
        reply = request.reply()
        qname = request.q.qname
        randomly_selected = random.sample(pool, 4)
        for picked in randomly_selected:
            reply.add_answer(RR(qname, QTYPE.A, rdata=A(picked), ttl=30))
        print("asked:", qname)
        return reply


def getIps():
    ips = []
    for i in range(15):
        start = "10."
        randomSecond = str(random.randint(1, 254)) + "."
        randomThird = str(random.randint(1, 254)) + "."
        randomLast = str(random.randint(1, 254))
        ips.append(start + randomSecond + randomThird + randomLast)
    return ips


pool = getIps()
server = DNSServer(FastFluxResolver(), port=53, address="0.0.0.0")
server.start()
