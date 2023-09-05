import pyshark

filename = '41.pcap'

cap = pyshark.FileCapture(input_file=filename)
i = 0
for pkt in cap:
    # print pkt

    print (pkt.frame_info._all_fields['frame.time_epoch'])

    # print pkt['IP']._all_fields

    i += 1
    if i == 5:
        break