import hashlib

secret_key = 'yzbqklnj'
needed_prefix = '000000'

cnt = 0
while True:
    hex = hashlib.md5(secret_key+'%d'%cnt).hexdigest()
    if hex.startswith(needed_prefix):
        print cnt
        break
    cnt += 1
    if cnt % 10000 == 0:
        print 'processed %d keys' % cnt

