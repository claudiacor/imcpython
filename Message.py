##erro nos get e set, ver programa que le o xml
#!/usr/bin/python
import struct
import time

from Constants import *

class Message():
    def __init__(self):
	
        self.sync = None
        self.mgid = None
        self.size = None
        self.timestamp = None
        self.src = None
        self.src_ent = None
        self.dst = None
        
        def getName(self):
            return None
        
        def getId(self):
            return None
        
        def setTimeStamp(self, ts=time.time()):
            self.timestamp = ts
            setTimeStampNested(ts)
            return self.timestamp
        
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
            return DUNE_IMC_CONST_HEADER_SIZE + DUNE_IMC_CONST_FOOTER_SIZE + getPayloadSerializationSize()

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

        def serializeFields(self, buffer, offset = DUNE_IMC_CONST_HEADER_SIZE):
            self.serialized_fields
            
        def serializeHeader(self, buffer, offset = 0):
            #########################escrever p o buffer
        
	def serializeFooter(self, buffer, offset = DUNE_IMC_CONST_HEADER_SIZE + getPayloadSerializationSize()):
            ###########

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

        
	# @abstract
        def setDestinationNested(self, value):
            return None

        def setDestinationEntityNested(self, value):
            return None

        def fieldsEqual(self, other):
            return True 
        


