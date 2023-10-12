from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet, ethernet

class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)
        self.mac_to_port = {}

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    # def packet_in_handler(self, ev):
    #     msg = ev.msg
    #     dp = msg.datapath
    #     ofp = dp.ofproto
    #     ofp_parser = dp.ofproto_parser
    #
    #     actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]
    #
    #     data = None
    #     if msg.buffer_id == ofp.OFP_NO_BUFFER:
    #          data = msg.data
    #
    #     out = ofp_parser.OFPPacketOut(
    #         datapath=dp, buffer_id=msg.buffer_id, in_port=msg.in_port,
    #         actions=actions, data = data)
    #     dp.send_msg(out)
    def packet_in_handler(self, ev):
        msg = ev.msg
        dp = msg.datapath
        ofp = dp.ofproto
        ofp_parser = dp.ofproto_parser

        # Obtén las direcciones MAC de origen y destino desde el paquete.
        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]
        src = eth.src
        dst = eth.dst

        # Registra la dirección MAC del host en la tabla de direcciones MAC.
        self.mac_to_port[src] = msg.in_port

        if dst in self.mac_to_port:
            out_port = self.mac_to_port[dst]
        else:
            out_port = ofp.OFPP_FLOOD

        actions = [ofp_parser.OFPActionOutput(out_port)]

        data = None
        if msg.buffer_id == ofp.OFP_NO_BUFFER:
            data = msg.data

        out = ofp_parser.OFPPacketOut(
            datapath=dp, buffer_id=msg.buffer_id, in_port=msg.in_port,
            actions=actions, data=data)
        dp.send_msg(out)
