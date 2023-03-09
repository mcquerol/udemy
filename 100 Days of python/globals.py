class errcodes:
	RC_SUCCESS                          =       			"Function was successfully completed."                      
	RC_ERROR                            =    	   			"Non specific error."                                       
	RC_ERROR_NULL                       =    		   		"A pointer was NULL when a non-NULL pointer was expected.",  
	RC_ERROR_ZERO                       =       			"A value was zero when no zero can be accepted.",            
	RC_ERROR_MEMORY                     =       			"Out of memory."                                            
	RC_ERROR_RANGE                      =       			"A value was out of Range."                                 
	RC_ERROR_OVERRUN                    =       			"A value was too big."                                      
	RC_ERROR_UNDERRUN                   =       			"A value was too small"                                     
	RC_ERROR_BUFFER_FULL                =       			"A buffer was full."                                        
	RC_ERROR_BUFFER_EMTPY               =       			"A buffer was empty."                                       
	RC_ERROR_BUSY                       =      			 	"A resource was busy."                                      
	RC_ERROR_TIME_OUT                   =      			 	"Something take too much time."                             
	RC_ERROR_OPEN                       =     			 	"A device can't be opened."                                 
	RC_ERROR_CHECKSUM                   =      			 	"Wrong checksum."                                           
	RC_ERROR_READ_ONLY                  =      			 	"Object is read only."                                      
	RC_ERROR_WRITE_ONLY                 =      			 	"Object is write only."                                     
	RC_ERROR_INVALID                    =      			 	"Object is invalid."                                        
	RC_ERROR_READ_FAILS                 =      			 	"Could not read from object."                               
	RC_ERROR_WRITE_FAILS                =      			 	"Could not write to the object."                            
	RC_ERROR_NOT_MATCH                  =      			 	"Could not write to the object."							
	RC_ERROR_BAD_PARAM                  =     			 	"Parameters passed to the function are invalid or illegal."    
	RC_ERROR_BAD_DATA                   =      			 	"Invalid global data which is required by the function."       
	RC_ERROR_CANCELED                   =      			 	"operation was canceled."                                      
	RC_ERROR_INVALID_STATE              =      			 	"The operation can not be performed because of a FSM-state"    
	RC_ERROR_UNKNOWN                    =      			 	"Unknown error."               
	RC_ERROR_NOT_IMPLEMENTED            =       			"The requested functionality is not implemented."             
