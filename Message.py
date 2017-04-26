##erro nos get e set, ver programa que le o xml

import struct
import time

import Constants

class Message():
    def __init__(self):
	
        self.sync = 0
        self.mgid = 0
        self.size = 0
        self.timestamp = 0
        self.src = 0
        self.src_ent = 0
        self.dst = 0
    
        def getName(self):
            return None

        def getId(self):
            return None

        def setTimeStamp(self, ts):
            self.timestamp = ts
            setTimeStampNested(ts)
            return self.timestamp

        def setTimeStamp(self):
            return setTimeStamp(time.time())
        
        def getTimeStamp(self):
            return self.timestamp

        def getSource(self):
            return self.src

        def setSource(self, src):
            self.src = src
            setSourceNested(src)

        def getSourceEntity(self):
            return self.src_ent

        def setSourceEntity(self, src_ent):
            self.src_ent = src_ent
            setSourceEntityNested(src_ent)

        def getDestination(self):
            return self.dst

        def setDestination(self, dst):
            self.dst = dst
            setDestinationNested(dst)

        def getDestinationEntity(self):
            return self.dst_ent

        def setDestinationEntity(dst_ent):
            self.dst_ent = dst_ent
            setDestinationEntityNested(dst_ent)

        def getSubId(self):
            return 0

        def  setSubId(self, subid):
            return None
            
        def getValueFP(self):
            return 0.0

        def setValueFP(self, val):
            return None

        def getSerializationSize(self):
            return DUNE_IMC_CONST_HEADER_SIZE +
        DUNE_IMC_CONST_FOOTER_SIZE +
        getPayloadSerializationSize()

        def getPayloadSerializationSize(self):
            return getFixedSerializationSize() + getVariableSerializationSize()

        def getFixedSerializationSize(self):
            return 0

        def getVariableSerializationSize(self):
            return 0

        def toJSON(self):
            return ""

        def toText(self):
            return toJSON()

        def serializeFields(self):
            self.serialized_fields

        def deserializeFields(self):
            return ""

        def reverseDeserializeFields(self):
            return ""

        def fieldsToJSON(self):
            return ""
         
        def setTimeStampNested(self, value):
            return None

        def setSourceNested(self, value):
            return None

        def setSourceEntityNested(self, value):
            return None

        def setDestinationNested(self, value):
            return None

        def setDestinationEntityNested(self, value):
            return None

        def fieldsEqual(self, other):
            return True 
        


