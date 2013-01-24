# -*- coding: utf-8 -*-
from twisted.internet import reactor
from twisted.internet import protocol

class BroadcastingDatagramProtocol(protocol.DatagramProtocol):
    """
    Listenning on UDP from a specific port using twisted. Exits with Ctrl-c
    """
    def startProtocol(self):
        print 'Started...'

    def stopProtocol(self):
        print 'Stopped.'

    def datagramReceived(self, data, addr):
        print 'Message received from %s(%s): %s' % (addr[0], addr[1], data)

def startListening(port):
    print 'Listening on port %s' % port
    reactor.listenUDP(port, BroadcastingDatagramProtocol())
    reactor.run()


        
def r_list_items(l, items):
    """
    Remove items from a tree-like list
    """
    r_lst = []
    if isinstance(l, list):
        for o in l:
            r = r_list_items(o, items)
            if r is not None:
                r_lst.append(r)
        return r_lst if len(r_lst) > 0 else None
    else:
        return l if l not in items else None


