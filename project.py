import numpy as np

total_bytes = 0
total_cost = 0
io_req_rate = 0
processing_time = 0
processing_bytes = 0
download_bytes = 0
upload_bytes = 0
up_dow_cost = 0
number_of_days = 0
space_cost = 0
for _ in range(12):
    np.random.gamma(shape= 2,scale = 0.1, size=1)
    for _ in range(3000):
        rand=np.random.random()
        if(rand<0.5):
            processing_time += np.random.geometric(p=0.2, size = 1)
            processing_bytes += 100
            download_bytes += 100
        elif(rand<0.7):
            upload = np.random.negative_binomial(n=200, p=0.2, size = 1)
            io_req_rate += 1
            processing_time +=1
            if(upload>1300):
                upload = 1300
            elif(upload<100):
                upload = 100
            upload_bytes += upload
            processing_bytes += upload
            number_of_days += 1

        else:
            download = np.random.poisson(lam=700, size = 1)
            if(download>1300):
                download = 1300
            download_bytes += download
            io_req_rate +=1
            processing_bytes += download

upload_bytes =1000000000000
processing_cost = processing_time * 0.1
total_bytes = download_bytes + upload_bytes
up_dow_cost =total_bytes/100000000000
total_cost = processing_cost + up_dow_cost
sapce_cost = (upload_bytes/100 000 000 000) * number_of_days * 0.33
WAN_traffic = (download_bytes + processing_bytes)/100000000000

print("Cost calculation: ")
print("Processing time cost in dollars: ",processing_cost/100)
print("Network traffic costin dollars: ",up_dow_cost)
print("I/O request rate cost in cents: ",io_req_rate/100)
print("Volume data cost: ",space_cost)
print("WAN traffic cost in dollars: ",WAN_traffic)
