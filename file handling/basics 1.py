
# File Handling : 

# consists of                 1. methods (functions)         and         2. modes(permissions)
#                                        |                                        |
#                                      read()          -------------------------------------------------
#                                    readline()        |                        |                      |
#                                    readlines()     simple modes            + modes            binary modes
#                                      write()         |                        |                      |
#                                      seek()         r read           r+ (read + write)     wb (write binary)
#                                      close()        w write          w+ (write + read)     rb (read binary)
#                                                     a append         a+ (append + read)  