```
  _____  _   _  _____    _____                    __ 
 |  __ \| \ | |/ ____|  / ____|                  / _|
 | |  | |  \| | (___   | (___  _ __   ___   ___ | |_ 
 | |  | | . ` |\___ \   \___ \| '_ \ / _ \ / _ \|  _|
 | |__| | |\  |____) |  ____) | |_) | (_) | (_) | |  
 |_____/|_| \_|_____/  |_____/| .__/ \___/ \___/|_|  
                              | |                    
                              |_|                    
```

### Açıklama
**DNS isteklerini veya trafiği kendi istediğiniz yere yönlendirerek hedef web sitesini manipüle etmenize yarayan bir script.**

**[arp_spoofy.py](https://github.com/mustafadalga/ARP-poisoning-packet-sniffer)** scripti ile hedef bilgisayar üzerinde ARP zehirlemesi yapılırken , **dns_spoof.py** scripti de hedef web sitesi için trafiği istenilen yere yönlendirerek , hedef web sitesini manipüle eder.


#### Kurulacak modüller

* Linux için kurulum
```
sudo pip install -r requirements.txt
```



### ARP Spoof Kullanımı
```
python arp_spoof.py --hedef HEDEFIP --gateway GATEWAY
```


### DNS Spoof Kullanımı
```
 python dns_spoof.py --url www.example.com --redirect ip_adress
```

<hr>

### Örnek Gösterim  - Virtualbox Sanal Makine üzerinde
#### Kali Linux  DNS Spoof İşlemi - Hacker

![2](https://user-images.githubusercontent.com/25087769/59797902-910b8f80-92e9-11e9-90d5-df97fe58e317.PNG)



#### Windows 8 - Hedef Makine

![1](https://user-images.githubusercontent.com/25087769/59797903-91a42600-92e9-11e9-88a2-9f6fc2304c20.PNG)



