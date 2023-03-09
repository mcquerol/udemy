import globals as glob
import numpy as np


class ringbuffer:
    def __init__(rb,size):
        rb.m_size = np.uint32(size)
        rb.m_buff = [None] * rb.m_size
        rb.m_fillLevel = np.uint32(0)
        rb.m_writeIdx = np.uint32(0)
        rb.m_readIdx = np.uint32(0)
    
    def __del__(rb):
        del rb.m_size
        del rb.m_buff
        del rb.m_fillLevel
        del rb.m_writeIdx
        del rb.m_readIdx

    def __str__(rb) -> str:
        return f"size = {rb.m_size}, read index = {rb.m_readIdx}, write index = {rb.m_readIdx}, fill level = {rb.m_fillLevel}"

    def write(rb, data):
        if rb.m_fillLevel > rb.m_size:
            return glob.errcodes.RC_ERROR_BUFFER_FULL
        
        rb.m_buff[rb.m_writeIdx] = data
        rb.m_fillLevel+=1
        rb.m_writeIdx+=1
        rb.m_writeIdx%=rb.m_size
        return glob.errcodes.RC_SUCCESS

    def read(rb):
        if rb.m_fillLevel < rb.m_size:
            return glob.errcodes.RC_ERROR_BUFFER_EMTPY
        
        data = rb.m_buff[rb.m_readIdx]
        rb.m_readIdx+=1
        rb.m_readIdx%=rb.m_size
        return data
        
