from Message import *
import Factory

def serialize(msg, bfr):
    msg.serializeHeader(bfr)
    msg.serializeFields(bfr)
    total = msg.getSerializationSize()
    return total
    
def deserialize(msg, bfr):
    sync = struct.unpack_from('<H',bfr,offset = 0)
    offset += struct.calcsize('<' + 'H')
    
    if(hex(sync) == DUNE_IMC_CONST_SYNC):
        vals = struct.unpack_from('<HHdHBHB',bfr, offset)
        mgid = vals[0]
        size = vals[1]
        timestamp = vals[2]
        src = vals[3]
        src_ent = vals[4]
        dst = vals[5]
        dst_ent = vals[6]

    elif(hex(sync) == DUNE_IMC_CONST_SYNC_REV):
        vals = struct.unpack_from('>HHdHBHB',bfr, offset)
        mgid = vals[0]
        size = vals[1]
        timestamp = vals[2]
        src = vals[3]
        src_ent = vals[4]
        dst = vals[5]
        dst_ent = vals[6]
        
    msg = Factory.produce(mgid)
    msg.deserializeFields(bfr)
    
    msg.sync = sync
    msg.mgid = mgid
    msg.size = size
    msg.timestamp = timestamp
    msg.src = src
    msg.src_ent = src_ent
    msg.dst = dst
    msg.dst_ent = dst_ent    
    
    return msg
