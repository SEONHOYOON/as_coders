#!/usr/bin/env python
# coding: utf-8

# In[3]:


def alarm_time_print(time):
    time_split=time.split(' ')
    time_split[0]=int(time_split[0])
    time_split[1]=int(time_split[1])
    time_total=time_split[0]*60+time_split[1]-45
    if time_total<45 :
        time_hour=23
        tmie_min=abs((time_split[0]*60+time_split[1]-45)%60)
    else :
        time_hour=int((time_split[0]*60+time_split[1]-45)/60)
        time_min=(time_split[0]*60+time_split[1]-45)%60
    if time_min==0:
        time_min=str('00')
    else:
        time_min=str(time_min)
    if time_hour==0 :
        time_hour=str('00')
    else :
        time_hour=str(time_hour)
    
    print_time=time_hour+str(' ')+str(time_min)
    return print_time


# In[4]:


alarm_time_print('10 00')


# In[ ]:




