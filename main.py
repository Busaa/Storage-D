"""
Test archive in order for me to learn how to use the Wukong Codec
"""
from StorageD.codec import WukongEncode
from StorageD.codec import WukongDecode


#Encode
encode_worker = WukongEncode(input_file_path="tests/testFile/brazil.png", output_dir="tests/testResult/", 
                            sequence_length=200,max_homopolymer=4,min_gc=0.4, max_gc=0.6,rule_num=1, 
                            rs_num=0, add_redundancy=True,add_primer=True, primer_length=20)


res_file = encode_worker.common_encode()

#Decode
decode_worker = WukongDecode(input_file_path='tests/testResult/brazil_wukong.fasta',
                            output_dir="tests/testResult/", rule_num=1)
res_file = decode_worker.common_decode()
