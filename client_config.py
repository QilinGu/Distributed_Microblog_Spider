__author__ = 'multiangle'


#========================================================
#
#    This file contains the option info for client.
#
#========================================================
import key_config

# 全局参数              global config info
PROCESS_NUM             =2                #进程数目           number of process
THREAD_NUM              =100                #每个进程最多线程   max thread num per process
NOMAL_INFO_PRINT        =False            #普通信息显示       if print normal information
KEY_INFO_PRINT          =True            #关键信息显示       if print key information
DEBUG_INFO_PRINT        =True            # 调试信息显示
NORMAL_INFO_LOG         =True            #普通信息日志       if output normal info to log
KEY_INFO_LOG            =True            #错误信息日志       if output key info to log
LOG_POS                 ='log\\'          #日志存放点         the address of log
DATA_POS                ='temp\\'       #临时数据存放点
UUID                    =4                #客户端的型号 或者说id
#代理相关               about proxy
USE_PROXY               =True            #是否使用代理        if use proxy
PROXY_POOL_SIZE         =THREAD_NUM*2     #每个进程维持的代理池的大小
CURRENT_YEAR            =2016
LARGEST_TRY_TIMES       =3                # 获取页面或解析失败以后，重新尝试的次数

####-------------------------------------####

SERVER_URL              = key_config.SERVER_URL         #服务器地址,端口号
DATA_SERVER_URL         = key_config.DATA_SERVER_URL    #数据服务器地址，端口号


