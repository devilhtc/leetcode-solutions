# solution by @awice, bit manipulation + greedy

def ip2int(ip):
	out = 0
	for num in ip.split('.'):
		out = out * 256 + int(num)
	return out

def int2ip(num):
	out = []
	for i in [24, 16, 8, 0]:
		out.append(str((num >> i) % 256))
	return '.'.join(out)

class Solution(object):
	def ipToCIDR(self, ip, n):
		s = ip2int(ip)
		out = []
		while n > 0:
			mask = max(33 - (s & -s).bit_length(), 33 - n.bit_length())
			out.append(int2ip(s) + '/' + str(mask))
			s += (1 << (32 - mask))
			n -= (1 << (32 - mask))
		return out
