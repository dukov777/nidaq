import nidaqmx 

write_task = nidaqmx.Task() 
read_task = nidaqmx.Task()

write_task.ao_channels.add_ao_voltage_chan('Dev1/ao0','mychannel',0,5) 
read_task.ai_channels.add_ai_voltage_chan("Dev1/ai0", min_val=0, max_val=5, terminal_config=nidaqmx.constants.TerminalConfiguration.RSE)

read_task.start() 

write_task.start() 


write_task.write(2.0) 
print(read_task.read())

write_task.stop() 
write_task.close()

read_task.stop() 
read_task.close()
